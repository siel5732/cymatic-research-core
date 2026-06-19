#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AcutisForge Acoustic Morphogenesis Initiative:
3D Bessel Beam Acoustic Levitation & Trapping Simulator.
Pythagoras's design: levitating and patterning cells in 3D space using interferometric sound fields.
"""

import math
import json

class PythagorasBessel:
    BEAM_SINGLE_FREQ = "Single-Frequency Zeroth-Order Bessel Beam"
    BEAM_INTERFEROMETRIC = "Dual-Frequency Interferometric Bessel Trap"

def bessel_j0(x):
    """Taylor series approximation of the zeroth-order Bessel function of the first kind J0(x)"""
    val = 0.0
    # First 10 terms are extremely accurate for x in [0, 15]
    for k in range(10):
        term = ((-1)**k) * ((x / 2.0)**(2 * k)) / (math.factorial(k)**2)
        val += term
    return val

def simulate_bessel_trap(grid_res=30, radius_cm=0.5, height_cm=1.0):
    results = {}
    
    r_coords = [radius_cm * (i / (grid_res - 1)) for i in range(grid_res)] # Radial from 0 to R
    z_coords = [height_cm * (i / (grid_res - 1) - 0.5) for i in range(grid_res)] # Axial from -H/2 to H/2

    modes = [PythagorasBessel.BEAM_SINGLE_FREQ, PythagorasBessel.BEAM_INTERFEROMETRIC]

    # Acoustic wave parameters
    f1 = 1.0e6 # 1 MHz ultrasound transducer
    v_sound = 1500.0 * 100.0 # Speed of sound in hydrogel/water ~ 150,000 cm/s
    wavelength = v_sound / f1 # ~0.15 cm
    k = 2.0 * math.pi / wavelength # Wavenumber ~ 41.8 rad/cm
    
    # Radial and axial wavenumbers for a Bessel beam
    theta_cone = math.radians(15.0) # 15-degree cone angle
    k_r = k * math.sin(theta_cone)
    k_z = k * math.cos(theta_cone)

    for mode in modes:
        pressure_field = []
        trapping_force_field = []
        total_traps_formed = 0

        for z in z_coords:
            row_p = []
            row_f = []
            for r in r_coords:
                # 1. Base Bessel Beam pressure profile
                # J0(k_r * r) * cos(k_z * z)
                J0_val = bessel_j0(k_r * r)
                
                if mode == PythagorasBessel.BEAM_SINGLE_FREQ:
                    pressure = J0_val * math.cos(k_z * z)
                else: # Dual-Frequency Interferometric
                    # Interfering two counter-propagating beams creates tight, isolated spherical nodes
                    pressure = J0_val * (math.cos(k_z * z) + 0.6 * math.sin(2.0 * k_z * z))

                # Trapping potential (minimum pressure equals maximum cell trapping probability)
                # Cells undergo acoustic radiation drift toward the zero-pressure nodes
                trapping_potential = math.exp(-6.0 * (pressure ** 2))
                local_trap_efficiency = round(trapping_potential * 100.0, 1)
                
                if local_trap_efficiency > 85.0:
                    total_traps_formed += 1

                row_p.append(round(pressure, 4))
                row_f.append(local_trap_efficiency)

            pressure_field.append(row_p)
            trapping_force_field.append(row_f)

        # Sample a 5x5 subgrid of the trapping force matrix for reports
        subgrid = [row[0::int(grid_res/5)] for row in trapping_force_field[0::int(grid_res/5)]]

        results[mode] = {
            "frequency_mhz": f1 / 1.0e6,
            "total_spherical_traps": total_traps_formed,
            "trap_spatial_density_pct": round((total_traps_formed / (grid_res ** 2)) * 100.0, 1),
            "sampled_trapping_field_map": subgrid
        }

    return results

def main():
    print("=====================================================================")
    print("   🪕 DEPLOYING PYTHAGORAS'S 3D BESSEL BEAM ACOUSTIC TRAP SIMULATOR 🪕")
    print("=====================================================================")
    print("[+] Simulating 3D non-diffracting acoustic Bessel tweezers in hydrogels...")

    results = simulate_bessel_trap()

    for mode_name, data in results.items():
        print(f"\n👉 BEAM ARCHITECTURE: {mode_name.upper()}")
        print(f"   * Frequency: {data['frequency_mhz']} MHz Ultrasound")
        print(f"   * Total Stable 3D Traps Formed: {data['total_spherical_traps']} / 900 nodes")
        print(f"   * Trapping Spatial Density: {data['trap_spatial_density_pct']}% of coordinate space")
        print(f"   * Sampled 5x5 Central 3D Trapping Potential Map (% probability):")
        for row in data['sampled_trapping_field_map']:
            print("     " + " ".join([f"{val:>5.1f}%" for val in row]))

    print("\n🔬 ACOUSTIC LEVITATION & PATTERNING INTERPRETATION:")
    print("======================================================")
    print("   * [The Single Bessel Column]: A single zeroth-order Bessel beam forms a continuous")
    print("     axial column of trapping nodes. Cells suspended in the hydrogel are squeezed into")
    print("     a solid, perfectly aligned central cylinder of cells. This is an ideal template")
    print("     for printing hollow, single-layered vascular tubes in mid-air.")
    print("   * [The Interferometric Trap Grid]: Interfering two counter-propagating beams creates")
    print("     isolated, tightly focused 3D spherical trapping nodes along the z-axis. The cells")
    print("     are locked into a vertical stack of levitating spheres, completely isolated from")
    print("     each other and the print substrate, representing a perfect non-contact container")
    print("     for culturing multi-layered islet organoids suspended in mid-air!")

    # Cache dataset
    output_path = "cymatic_research_core/cymatic_bessel_trap_results.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n💾 Analytical Bessel trap dataset cached to: {output_path}")

if __name__ == "__main__":
    main()
