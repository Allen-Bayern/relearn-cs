// Chain of Responsibility Pattern

abstract class Handler<T = unknown> {
  protected nextHandler: Handler | null = null;

  setNext(nextHandler: Handler): Handler {
    this.nextHandler = nextHandler;
    return nextHandler;
  }

  handle(request: T) {
    if (this.nextHandler) {
      this.nextHandler.handle(request);
    } else {
      console.log("Cannot handle");
    }
  }
}

class BuyHandler<T = string> extends Handler<T> {
  handle(request: T): void {
    if (request === "buy") {
      console.log("buy");
    } else {
      super.handle(request);
    }
  }
}

class SelectHandler<T = string> extends Handler<T> {
  handle(request: T): void {
    if (request === "select") {
      console.log("select");
    } else {
      super.handle(request);
    }
  }
}

const buyHandler = new BuyHandler<string>();
buyHandler.setNext(new SelectHandler());

buyHandler.handle("buy");
buyHandler.handle("select");
buyHandler.handle("withdraw");
