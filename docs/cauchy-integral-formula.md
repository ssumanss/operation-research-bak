# Cauchy Integral Formula

## Statement

!!! success "Cauchy Integral Formula"
    Let $f$ is analytic inside and on a positively oriented contour $\gamma$ and a is inside $\gamma$, then
    $$f(a) = \frac{1}{2\pi i} \oint_\gamma \dfrac{f(z)}{z-a}$$

??? note "Click here to see the proof."

    Consider,
    $$
    \begin{align}
        \oint_\gamma \dfrac{f(z)}{z-a} &= \oint_\gamma \dfrac{f(z)}{z-a}dz\\
        &= \oint_\gamma \dfrac{f(z) \color{blue}{- f(a) + f(a)}}{z-a}dz\\
        &= \color{red}{\oint_\gamma \dfrac{f(a)}{z-a}dz} + \oint_\gamma \dfrac{f(z) - f(a)}{z-a}dz\\
        &= \color{red}{f(a) \oint_\gamma \dfrac{1}{z-a}dz} + \oint_\gamma \dfrac{f(z) - f(a)}{z-a}dz\\
        &= \color{red}{f(a)\times 2\pi i} + \oint_\gamma \dfrac{f(z) - f(a)}{z-a}dz\\
        &= \color{red}{f(a)\times 2\pi i} + I\\
    \end{align}
    $$

    Now we will estimate the second part of the expression in RHS. We use deformation theorem to integrate it along a circular path $\overline{\gamma}: \vert z-a \vert = r$, then we get

    $$
    \begin{align}
        \newcommand{\I}{|I|} \I &= \left \vert \oint_{\vert z-a \vert = r} \dfrac{f(z) - f(a)}{z-a}dz \right \vert \\[2pt]
         &\leq  \oint_{\vert z-a \vert = r} \left \vert\dfrac{f(z) - f(a)}{z-a}dz \right \vert \\[2pt]
       &\leq  \oint_{\vert z-a \vert = r} \left \vert\dfrac{f(z) - f(a)}{z-a}dz \right \vert \\[2pt]
    \end{align}
    $$

    Since $f$ is continuous in the disc enlosed by $\overline{\gamma}$,

## Derivatives

The general cauchy integral formula given as follows

!!! success "Cauchy Integral Formula for Derivatives"
    Let $f$ is analytic inside and on a positively oriented contour $\gamma$ and a is inside $\gamma$, then
    $$f^{(n)}(a) = \frac{n!}{2\pi i} \oint_\gamma \dfrac{f(z)}{(z-a)^{n+1}}dz$$

***
## Questions
**Exercise:**
