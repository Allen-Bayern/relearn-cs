# SOLID 原则

SOLID 是面向对象设计的五大基本原则，有助于构建可维护、可扩展、灵活且易于理解的系统。SOLID 分别代表：

## 1. 单一职责原则（Single Responsibility Principle, SRP）

每个类应该只有一个引起它变化的原因。即一个类只负责一项职责。

**示例：**

```typescript
// 不符合 SRP
class User {
  saveToDatabase() {
    /* ... */
  }
  sendEmail() {
    /* ... */
  }
}
// 符合 SRP
class User {
  // 用户相关属性和方法
}
class UserRepository {
  save(user: User) {
    /* ... */
  }
}
class EmailService {
  sendEmail(user: User) {
    /* ... */
  }
}
```

## 2. 开放封闭原则（Open/Closed Principle, OCP）

软件实体（类、模块、函数等）应该对扩展开放，对修改封闭。

**示例：**

```typescript
// 不符合 OCP
function getArea(shape: any) {
  if (shape.type === "circle") {
    return Math.PI * shape.radius * shape.radius;
  } else if (shape.type === "square") {
    return shape.length * shape.length;
  }
}
// 符合 OCP
interface Shape {
  getArea(): number;
}
class Circle implements Shape {
  constructor(public radius: number) {}
  getArea() {
    return Math.PI * this.radius * this.radius;
  }
}
class Square implements Shape {
  constructor(public length: number) {}
  getArea() {
    return this.length * this.length;
  }
}
```

## 3. 里氏替换原则（Liskov Substitution Principle, LSP）

子类对象能够替换父类对象，并且程序的功能不受影响。

**示例：**

```typescript
class Bird {
  fly() {
    /* ... */
  }
}
class Sparrow extends Bird {}
class Ostrich extends Bird {
  // 不应该继承 Bird，因为鸵鸟不会飞
  fly() {
    throw new Error("Ostrich cannot fly");
  }
}
// 更好的做法：
class Bird {}
class FlyingBird extends Bird {
  fly() {
    /* ... */
  }
}
class Sparrow extends FlyingBird {}
class Ostrich extends Bird {}
```

## 4. 接口隔离原则（Interface Segregation Principle, ISP）

不应该强迫客户依赖它们不用的方法。即接口要小而专一。

**示例：**

```typescript
// 不符合 ISP
interface Animal {
  run(): void;
  fly(): void;
}
class Dog implements Animal {
  run() {
    /* ... */
  }
  fly() {
    throw new Error("Dog cannot fly");
  }
}
// 符合 ISP
interface Runnable {
  run(): void;
}
interface Flyable {
  fly(): void;
}
class Dog implements Runnable {
  run() {
    /* ... */
  }
}
class Bird implements Runnable, Flyable {
  run() {
    /* ... */
  }
  fly() {
    /* ... */
  }
}
```

## 5. 依赖倒置原则（Dependency Inversion Principle, DIP）

高层模块不应该依赖低层模块，二者都应该依赖其抽象。抽象不应该依赖细节，细节应该依赖抽象。

**示例：**

```typescript
// 不符合 DIP
class MySQLDatabase {
  connect() {
    /* ... */
  }
}
class UserService {
  db = new MySQLDatabase();
}
// 符合 DIP
interface Database {
  connect(): void;
}**
class MySQLDatabase implements Database {
  connect() {
    /* ... */
  }
}
class UserService {
  constructor(private db: Database) {}
}
```

---

**总结：**
SOLID 原则有助于提升代码的可维护性、可扩展性和健壮性，是优秀软件设计的重要基础。
