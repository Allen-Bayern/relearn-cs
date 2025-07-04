// Strategy Pattern

interface CouponDeliveryStrategy {
  deliverCoupon: (couponNum: number) => void;
}

const createMainCoupon = (): CouponDeliveryStrategy => {
  return {
    deliverCoupon(couponNum) {
      console.log(couponNum);
    },
  };
};

const createPlateCoupon = (): CouponDeliveryStrategy => {
  return {
    deliverCoupon(couponNum) {
      console.log(couponNum);
    },
  };
};

const strategyDict = {
  MAIN: createMainCoupon,
  PLATE: createPlateCoupon,
};

type StrategyList = keyof typeof strategyDict;

// Context
const couponMethod = (opt: { strategy?: StrategyList; couponNum?: number }) => {
  const { strategy = "MAIN", couponNum = 0 } = opt;
  const realStrategy = strategyDict[strategy]();
  realStrategy.deliverCoupon(couponNum);
};
