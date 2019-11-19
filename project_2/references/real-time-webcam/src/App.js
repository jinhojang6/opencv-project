import React, { Component } from "react";
import "@tensorflow/tfjs";
import * as cocoSsd from "@tensorflow-models/coco-ssd";
import "./App.css";


class App extends Component {
  state = {
    model: null,
    stream: null,
    videoElement: null,
    canvasElement: null
  };
  async componentDidMount() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: {
          facingMode: "user"
        },
        audio: false
      });
      console.log(stream)

      const model = await cocoSsd.load();

      await this.setState({
        videoElement: this.refs.video,
        canvasElement: this.refs.canvas,
        stream,
        model
      });

      this.state.videoElement.srcObject = this.state.stream;
      this.predictFrame();
    } catch (err) {
      console.log(err);
    }
  }

  predictFrame = async () => {
    const predictions = await this.state.model.detect(this.refs.video);
    this.drawPredictions(predictions);
    //recursive call
    this.predictFrame();
  };

  drawPredictions = predictions => {
    const ctx = this.state.canvasElement.getContext("2d");
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    const font = "16px sans-serif";
    ctx.font = font;
    ctx.textBaseline = "top";
    predictions.forEach(prediction => {
      const x = prediction.bbox[0];
      const y = prediction.bbox[1];
      const width = prediction.bbox[2];
      const height = prediction.bbox[3];
      // Draw prediction box.
      ctx.strokeStyle = "#fa00ff";
      ctx.lineWidth = 4;
      ctx.strokeRect(x, y, width, height);
      // Draw text box.
      ctx.fillStyle = "#fa00ff";
      const textWidth = ctx.measureText(prediction.class).width;
      const textHeight = parseInt(font, 10); // base 10
      ctx.fillRect(x, y, textWidth + 4, textHeight + 4);
      // Draw text.
      ctx.fillStyle = "#000000";
      ctx.fillText(prediction.class, x, y);
    });
  };

  render() {
    return (
      <div>
        <video
          className="position"
          autoPlay
          playsInline
          muted
          ref="video"
          width="900"
          height="600"
        />
        <canvas className="position" ref="canvas" width="900" height="600" />
      </div>
    );
  }
}

export default App;
