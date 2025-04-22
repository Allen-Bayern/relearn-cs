// 来多少个数组都不怕
const unique = (nums: number[]) => Object.keys(nums.reduce((prev, num) => ({
    ...prev,
    [String(num)]: ''
}), {} as Record<string, string>)).map(num => +num);

const solution = (...args: number[][]): number[] => {
    if (args.map(list => list.length).includes(0)) {
        return [] as number[];
    }

    const res: number[] = [];
    const hashMap = new Map<number, number>();

    args.forEach((list, index) => {
        const uList = unique(list);
        if (!index) {
            uList.forEach(num => {
                hashMap.set(num, 1);
            });
        } else {
            uList.forEach(num => {
                const cur = hashMap.get(num);
                hashMap.set(num, cur ? 1 + cur : 1);
            });
        }
    });

    hashMap.forEach((val, key) => {
        if (val === args.length) {
            res.push(key);
        }
    });

    return res;
};