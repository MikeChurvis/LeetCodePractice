function threeSum(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);

    let validTriples = searchForValidZeroSumTriples(nums);

    return validTriples;
};


function searchForValidZeroSumTriples(nums: number[]): number[][] {
    let validTriples: number[][] = [];

    // Start at the beginning. Keep going until two spaces from the end, or until a positive value is reached.
    for (let iFirstNumber = 0; iFirstNumber < nums.length - 2 && nums[iFirstNumber] <= 0; iFirstNumber++) {

        // Fast-forward past numbers that have already been searched.
        if (iFirstNumber > 0 && nums[iFirstNumber] === nums[iFirstNumber - 1]) {
            continue;
        }

        // Find all tuples in the rest of the array whose sum cancels out firstNumber.
        const firstNumber = nums[iFirstNumber];
        const searchSpace = nums.slice(iFirstNumber + 1)
        const target = -firstNumber;
        const validTuples = searchForValidTargetSumTuples(searchSpace, target);

        validTriples = validTriples.concat(validTuples.map(tuple => [firstNumber, ...tuple]));
    }

    return validTriples;
}


function searchForValidTargetSumTuples(nums: number[], target: number): number[][] {
    let validTuples: number[][] = []

    // Perform an exhaustive two-pointer search.
    let iHead = 0;
    let iTail = nums.length - 1;

    while (iHead < iTail) {
        const sum = nums[iHead] + nums[iTail];

        if (sum < target) {
            iHead++;
            continue;
        }

        if (sum > target) {
            iTail--;
            continue;
        }

        // A valid tuple has been found.
        validTuples.push([nums[iHead], nums[iTail]])

        // Fast-forward both pointers to the nearest number they haven't searched. Look ahead, stop short.
        while (iHead < iTail && nums[iHead] === nums[iHead + 1]) {
            iHead++;
        }
        while (iHead < iTail && nums[iTail] === nums[iTail - 1]) {
            iTail--;
        }

        // Advance both pointers to that next meaningful number.
        iHead++;
        iTail--;
    }

    return validTuples;
}


(() => {

    const testCases = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    for (const testCase of testCases) {
        console.log(threeSum(testCase))
    }

})();