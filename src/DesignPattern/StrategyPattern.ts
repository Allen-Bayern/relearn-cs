// Strategy Pattern

// 定义一个接口，规定所有优惠券发放策略都必须实现 deliverCoupon 方法
interface CouponDeliveryStrategy {
  deliverCoupon: (couponNum: number) => void;
}

// 主优惠券发放策略，实现了 CouponDeliveryStrategy 接口
const mainCoupon: CouponDeliveryStrategy = {
  deliverCoupon(couponNum: number) {
    // 实际发放逻辑，这里用 console.log 代替
    console.log(couponNum);
  },
};

// 盘点优惠券发放策略，同样实现了 CouponDeliveryStrategy 接口
const giftCoupon: CouponDeliveryStrategy = {
  deliverCoupon(couponNum: number) {
    // 实际发放逻辑，这里用 console.log 代替
    console.log(couponNum);
  },
};

// 策略字典，将不同的策略对象以常量形式存储，方便后续查找和使用
const strategyDict = Object.freeze({
  MAIN_COUPON: mainCoupon,
  GIFT_COUPON: giftCoupon,
});

// 优惠券发放方法，接收一个包含策略和优惠券数量的参数对象
const couponMethod = (opt: {
  strategy?: CouponDeliveryStrategy; // 可选，默认使用 mainCoupon
  couponNum?: number; // 可选，默认 0
}) => {
  // 解构参数，设置默认值
  const { strategy: realStrategy = mainCoupon, couponNum = 0 } = opt;
  // 调用对应策略的发放方法
  realStrategy.deliverCoupon(couponNum);
};
