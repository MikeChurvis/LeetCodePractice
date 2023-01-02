function maxArea(height: number[]): number {
    // This is a two-pointer problem. We converge from the edges.

    return 0;
};


(() => {
    const testCases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1]
    ]

    for (const testCase of testCases) {
        console.log(maxArea(testCase));
    }
})();