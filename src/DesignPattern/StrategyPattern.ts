// Strategy Pattern

interface CouponDeliveryStrategy {
  deliverCoupon: (couponNum: number) => void;
}

const mainCoupon: CouponDeliveryStrategy = {
  deliverCoupon(couponNum: number) {
    console.log(couponNum);
  },
};

const plateCoupon: CouponDeliveryStrategy = {
  deliverCoupon(couponNum: number) {
    console.log(couponNum);
  },
};

const strategyDict = {
  MAIN: mainCoupon,
  PLATE: plateCoupon,
};

type StrategyList = keyof typeof strategyDict;

// Context
const couponMethod = (opt: { strategy?: StrategyList; couponNum?: number }) => {
  const { strategy = "MAIN", couponNum = 0 } = opt;
  const realStrategy = strategyDict[strategy];
  realStrategy.deliverCoupon(couponNum);
};
