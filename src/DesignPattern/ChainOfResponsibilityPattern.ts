// Chain of Responsibility Pattern

// 处理请求的抽象处理者
abstract class Handler {
  protected nextHandler: Handler | null = null;

  setNext(handler: Handler): Handler {
    this.nextHandler = handler;
    return handler;
  }

  handle(request: any): void {
    if (this.nextHandler) {
      this.nextHandler.handle(request);
    }
  }
}

// 具体处理者A
class ConcreteHandlerA extends Handler {
  handle(request: any): void {
    if (request === "A") {
      console.log("ConcreteHandlerA handled the request.");
    } else {
      super.handle(request);
    }
  }
}

// 具体处理者B
class ConcreteHandlerB extends Handler {
  handle(request: any): void {
    if (request === "B") {
      console.log("ConcreteHandlerB handled the request.");
    } else {
      super.handle(request);
    }
  }
}

// 客户端代码示例
const handlerA = new ConcreteHandlerA();
const handlerB = new ConcreteHandlerB();

handlerA.setNext(handlerB);

handlerA.handle("A"); // 输出: ConcreteHandlerA handled the request.
handlerA.handle("B"); // 输出: ConcreteHandlerB handled the request.
handlerA.handle("C"); // 无输出
