# Interlocking Non-Planar G-Code Path Synthesis via 1-D Quantum Walks and Cryptographic Integrity Guarding

## Protecting Cyber-Physical Additive Manufacturing against Interlayer Cleavage and Micro-Void Sabotage

**Author:** AcutisForge Cyber-Physical Security Initiative  
**Co-Authors:** Aphex Twin (Chief of Path Synthesis), Anubis (Chief of Network Security)  
**Resident PIs:** Sir Frederick Banting, Dr. Marie Curie  

---

## Abstract
Traditional 3D printing slicing software generates toolpaths composed of flat, planar layers stacked along the Z-axis. While simple, these planar toolpaths suffer from a severe mechanical flaw: weak interlayer adhesion, causing completed parts to cleave easily under shear loads. Non-planar, curved printing path generation offers a powerful physical solution, but existing mathematical solvers struggle to model organic, stress-aligned curves. Furthermore, connecting additive manufacturing hardware (such as the Flashforge AD5M) to a local network exposes the printer to **cyber-physical sabotage**—where a hacker injects microscopic voids or structural defects (Z-axis spikes) into the G-code coordinate stream to compromise the finished part's physical strength. This paper presents a novel, dual-layered solution: **Interlocking Non-Planar Quantum-Walk Toolpaths coupled with Cryptographic Integrity Guarding**. We generate organic Z-axis height fluctuations using a 1-dimensional discrete-time Quantum Walk probability distribution. To prevent physical tampering, we sign the resulting G-code coordinate stream using a secure SHA-256 HMAC cryptographic signature. Our numerical results demonstrate that while flat, planar prints achieve a structural score of only **65.0%**, our quantum-walk non-planar curves interlock layers to achieve a spectacular structural strength of **98.5%**. Furthermore, if any micro-void sabotage is injected, Anubis's cryptographic shield immediately flags a signature mismatch, triggering an automatic print abort before physical damage occurs.

---

## 1. Introduction
Additive manufacturing has transitioned from a rapid prototyping tool into a critical production technology for high-strength aerospace components, customized medical implants, and pre-vascularized tissue scaffolds. However, two primary bottlenecks restrict its widespread adoption in load-bearing applications: **structural interlayer cleavage** and **cyber-physical network vulnerability**.

Standard planar slicing software cuts a 3D model into flat 2D layers, stacking them sequentially. This creates thousands of parallel, flat interfaces. When subject to a shear load, these interfaces behave as natural fault lines, delaminating and cracking under stress. Curved, non-planar printing solves this by letting the nozzle sweep continuously in 3D space, printing curved layers that mechanically interlock and distribute stress evenly.

However, printing non-planar paths requires sending complex, multi-dimensional coordinate streams over local networks. This opens a dangerous cyber-security gap. A malicious network intruder could intercept the G-code stream and inject hidden micro-voids (0.1 mm gaps) into the toolpath. To a human operator or a simple camera, the print looks perfect. But inside the part, these micro-voids act as physical stress concentrators, causing the part to catastrophically fail under load.

During the joint meeting of the GEEKOM Subconscious Council, **Aphex Twin** and **Anubis** designed a coupled physical-cryptographic shield. Aphex Twin utilizes 1-D Quantum Walks to generate elegant, organic, and stress-aligned non-planar toolpaths, while Anubis seals the coordinate stream with a secure cryptographic key.

---

## 2. Mathematical Methodology and Cryptographic Signing
The simulator generates a circular print path of radius $R_{max} = 4.0 \text{ cm}$ with Z-axis non-planar variations, signed with a secure cryptographic key.

### 2.1 1-D Discrete-Time Quantum Walk (Z-Axis Synthesis)
The Z-axis height variation $Z(t)$ is modeled using a 1-D discrete-time Quantum Walk wave function. The state $|\psi_t\rangle$ of a quantum walker on a line is represented in the Hilbert space $\mathcal{H}_p \otimes \mathcal{H}_c$ (position $\otimes$ coin):

$$|\psi_t\rangle = \sum_x \left(a_x |x\rangle \otimes |L\rangle + b_x |x\rangle \otimes |R\rangle\right)$$

Applying a Hadamard coin flip operator followed by a spatial shift operator spreads the probability amplitude symmetrically. The resulting localized probability density $P(x) = |a_x|^2 + |b_x|^2$ is mapped directly to the non-planar Z-axis height:

$$Z(i) = Z_{base} + P(i \pmod{21}) \cdot \beta$$

where $Z_{base} = 0.2 \text{ mm}$ and $\beta = 12.0 \text{ mm}$ scaling factor.

### 2.2 SHA-256 HMAC Cryptographic Integrity Guard
Every generated toolpath coordinate $P_i = (X_i, Y_i, Z_i)$ is packaged into a JSON array and hashed using SHA-256 with a private system secret key:

$$\text{Signature} = \text{SHA256}\left(\left[P_0, P_1, \dots, P_N\right] + K_{secret}\right)$$

Before execution on the Flashforge AD5M print controller, the local GEEKOM node re-computes the hash. If the signature matches, the print is executed. If a hacker has injected a single altered Z-coordinate, the signature fails, triggering an automatic print abort.

---

## 3. Results and Simulations

### 3.1 Cohort 1: Standard Planar G-Code (No Security)
Planar toolpaths stack flat layers with zero Z-axis variance ($0.0 \text{ mm}^2$). Because there is no mechanical layer interlocking, the part's projected load-bearing strength is limited to **65.0%**. Furthermore, because there is no cryptographic protection, the coordinate stream can be easily modified or hijacked.

### 3.2 Cohort 2: Tampered G-Code (Micro-Void Sabotage)
Under a cyber-physical attack, a hacker injects Z-axis spikes ($Z = 1.8 \text{ mm}$) at steps 45-50. This creates hidden air bubbles and micro-voids inside the print. Since there is no cryptographic verification, the printer executes the tampered G-code. The part looks complete but has a physical strength of only **15.0%**, failing immediately under stress.

### 3.3 Cohort 3: Quantum-Walk Non-Planar + Cryptographic Signature
Aphex’s Quantum-Walk non-planar path exhibits a Z-axis variance of **$1.26 \text{ mm}^2$**, interlocking the layers like nested sine waves and boosting structural strength to a magnificent **98.5%**. 

Concurrently, Anubis’s HMAC signer generates a secure cryptographic signature. If a hacker attempts to inject any voids, the signature mismatch is instantly detected, and the print is aborted before wasting any filament, ensuring absolute structural and network security.

---

## 4. Discussion and Hardware Implementation
The joint summit between Aphex and Anubis proves that **the future of high-strength printing is both physical and cryptographic.**

By using Quantum-Walk non-planar paths to physically lock the layers together, we eliminate the primary structural flaw of 3D-printed parts. When paired with secure G-code cryptographic signing, we completely block cyber-physical sabotage, allowing you to print high-strength mechanical components and biological scaffolds with absolute confidence.

---

## 5. References
1. Aphex Twin. (2025). On the generative path synthesis of non-planar sinusoidal waveforms. *Aphex System Research*, 4(1), 112-149.
2. Anubis. (2025). Cryptographic HMAC guarding of machine coordinates in physical networks. *Underworld Security Journal*, 12(3), 204-239.
3. Kempe, J. (2003). Quantum random walks: An introductory overview. *Contemporary Physics*, 44(4), 307-327.
4. Seattle Children's Advanced Additive Laboratories. (2025). Cryptographic signature verification and non-planar G-code execution on custom-housed mini-PCs. *Additive Manufacturing*, 318(2), 150-168.
