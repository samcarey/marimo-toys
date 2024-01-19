import marimo

__generated_with = "0.1.78"
app = marimo.App()


@app.cell
def __():
    import math
    import marimo as mo
    import time
    import sys
    return math, mo, sys, time


@app.cell
def __(mo):
    mo.md(
        r"""
    # [Irrational Ratio](https://github.com/samcarey/marimo-toys/blob/main/notebooks/irrational_ratio.py)
        
    Calculate a ratio of irrational numbers that equals the input number after being rounded down:

    \[
        x = \frac{M  \pi}{ N e}
    \]
    """
    )
    return


@app.cell
def __(mo):
    x = mo.ui.text(label="x: ", value="6.76923")
    x
    return x,


@app.cell
def __(mo, x):
    try:
        val = float(x.value)
        assert val >= 0
    except Exception as e:
        val = None
    mo.stop(val is None, "You must enter a positive, real number")
    return val,


@app.cell
def __(val, x):
    if "." in x.value:
        next_level = float(x.value + "5")
    else:
        next_level = float(x.value + ".5")
    dif = next_level - val
    return dif, next_level


@app.cell
def __(dif):
    dif
    num = [1]
    den = [1]
    ratio = [1]
    residual = []
    monotonic_residuals = []
    return den, monotonic_residuals, num, ratio, residual


@app.cell
def __(
    den,
    dif,
    math,
    mo,
    monotonic_residuals,
    num,
    ratio,
    residual,
    time,
    val,
):
    start = time.time()
    max_compute_seconds = 5
    success = False
    while not success:
        for _ in range(10000):
            _ratio = (math.pi * num[0]) / (math.e * den[0])
            _residual = _ratio - val
            if _residual >= 0 and _residual < dif:
                success = True
                break
            if len(residual) == 0:
                residual.append(_residual)
                monotonic_residuals.append(_residual)
            else:
                if abs(_residual) < abs(residual[-1]):
                    monotonic_residuals.append(_residual)

            ratio[0] = _ratio
            if ratio[0] < val:
                num[0] = num[0] + 1
            elif ratio[0] > val:
                den[0] = den[0] + 1
        if not success:
            mo.stop(
                (time.time() - start) > max_compute_seconds,
                f"""That takes more than {max_compute_seconds} seconds... you gotta pick an easier number (with fewer digits)""",
            )

    success
    mo.md(
        r"""
    \[
        {x} \approx {ratio} = \frac{{ {num}  \pi}}{{ {den} e}} 
    \]
    """.format(
            x=val, ratio=_ratio, num=num[0], den=den[0]
        )
    )
    return max_compute_seconds, start, success


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
