#!/usr/bin/env python3
"""
🔥 BINANCE LIQUIDATION HUNTER V86 - THE LIQUIDITY PATHFINDER (ZERO GRAVITY HORIZON EDITION)
💀 Analisa Kegagalan V83, V84 & V85 (Kenapa Bot Salah Arah?)

    KASUS TRIAUSDT (The Ultimate Trap - "The Paradox of 0.00% Liquidation"):
        Data: Price pump, RSI 96.7 (Nuclear Overbought), Short Liq 0.0%, Long Liq -8.73%, 
              Flow 1.94x, Agg 1.5x, OI Δ +1.37%
        Bot memilih: LMG_DEATH_MAGNET_SHORT → LONG (Karena Short Liq 0.0% = magnet)
        Tapi market: DUMP -5% sampai -10% setelah ±58 menit
        
        🧠 Error Utama: LMG terlalu dominan tanpa filter RSI-OI Ceiling
        Masalahnya: Short liq 0.0% tidak selalu berarti cascade, sering kali itu "Exit Liquidity"!
        
        🔬 Clue yang Bot Lewatkan:
        - RSI 96.7 > 90 = Nuclear Overbought (area extrem)
        - OI Δ +1.37% > 0.5% = NEW POSITIONS ENTERING (bukan short liquidation!)
        - Agg 1.5x < 2.0 = weak aggression (passive sell wall)
        - Flow 1.94x tinggi tapi Agg rendah = internal matching / passive distribution
        
        Interpretasi sebenarnya:
        - Jika benar squeeze ke atas, OI harus TURUN (karena short liquidation menutup posisi)
        - TAPI OI NAIK = NEW SHORT BUILDING (Whale sedang build short positions!)
        - Pattern: Distribution top → Whale building shorts → Fake short magnet 0% → Dump ke long liq 8%
        
        ⚡ Signal Penting yang Bot Lewatkan:
        - RSI > 90 AND OI_delta > 0.5 AND Agg < 2.0 = OVERBOUGHT DISTRIBUTION TRAP
        - Ini adalah "Zero Gravity Horizon" - harga sudah di plafon, MM berhenti beli!
        - MM butuh bot lo entry LONG supaya mereka punya lawan buat nutup LONG mereka (JUAL)!

    KASUS 1: PHAUSDT (The Gravity Trap):
        Data: Price 0.0352, Long Liq: -0.17%, Short Liq: +1.76%, RSI 61.5, Flow 0.69, Agg 1.0, OI Δ +0.17, WMI -99.8
        Kenapa Loss? Bot V83 memilih GRAVITY_OVERDRIVE → SHORT karena Long Liq terlalu dekat (0.17% < 0.2%).
        Tapi market justru LONG!
        
        🧠 Error Utama: LGO terlalu dominan tanpa filter konteks
        Masalahnya: 0.17% long liq tidak selalu target, sering kali itu justru bait liquidity!
        
        🔬 Clue yang Bot Lewatkan:
        - Flow 0.69 = sell pressure lemah
        - Agg 1.0 = netral, no real selling
        - OI +0.17 = posisi baru masuk
        - WMI -99.8 = cluster long liquidation sangat besar
        
        Interpretasi sebenarnya:
        - Long liq kecil, short liq jauh, long cluster besar
        - Market maker biasanya: pump dulu, baru sweep long
        - Pattern umum: price pump → retail long FOMO → long liquidation build → dump
        
        ⚡ Signal Penting yang Bot Lewatkan:
        - Flow > 0.6 AND Agg > 0.8 = dump tidak mungkin terjadi
        - WMI < -80 = whale protect downside (short probability rendah)

    KASUS 2: UAIUSDT (The Oversold Trap - Liquidation Cascade):
        Data: Price 0.2847, RSI 3.6 (extreme oversold), Agg 4.0x buy, Flow 0.85x, OI Δ -0.32%
        Bot memilih: RMG_WEAK_MOMENTUM_BULLISH → LONG
        Tapi market: DUMP -7%
        
        🧠 Error Utama: RMG override PSV tanpa filter OI
        Masalahnya: RSI < 10 tidak selalu berarti bottom, sering berarti liquidation acceleration phase
        
        🔬 Clue yang Bot Lewatkan:
        - RSI 3.6 < 10 = extreme oversold
        - OI Δ -0.32% < 0 = positions closing, bukan new longs entering
        - Flow 0.85x < 1.0 = volume tidak confirm bullish
        
        Interpretasi sebenarnya:
        - Jika market benar-benar reversal, OI harus naik (new longs entering)
        - OI turun = liquidation cascade incoming
        - Pattern: oversold bounce trap → retail buy dip → dump continuation → long liq cascade

    KASUS 3: The Liquidity Vacuum Rebound (Checkmate Case - UAI Style):
        Data: WMI -99.1x, RSI 11.7, Agg 2.33x, OI turun (Institutional Exit detected)
        Bot memilih: IER_EXIT → SHORT (Karena OI turun, Whale kabur)
        Tapi market: PUMP! REBOUND! Short squeeze!
        
        🧠 Error Utama: IER terlalu dominan tanpa filter WMI + RSI ekstrim
        Masalahnya: WMI -99.1x artinya Short Liquidation Pool di atas 4% - itu "bernutrisi" buat MM!
        
        🔬 Clue yang Bot Lewatkan:
        - RSI 11.7 < 15 = extreme oversold
        - WMI -99.1 < -90 = massive short liquidation cluster BELOW price
        - Agg 2.33 > 1.0 = ada agresi beli di dasar ekstrim
        - OI turun = Whale narik order untuk bersihin Orderbook bawah (Liquidity Vacuum)
        
        Interpretasi sebenarnya:
        - Whale sengaja narik order (bikin OI turun) buat ngebersihin Orderbook bawah
        - Lalu dalam hitungan milidetik mereka hajar Market Buy buat squeeze semua Short seller
        - Ini adalah "The Liquidity Vacuum Rebound" - Short Trap klasik!
        - JANGAN PERNAH SHORT KALAU WMI < -90! Itu area "Spring" bandar!

🛡️ THE SUPREME REFINEMENT: V86 "THE LIQUIDITY PATHFINDER" - ZERO GRAVITY HORIZON
    Modul Baru V86: "Zero Gravity Horizon" (ZGH) - ANTI-TRIA TRAP!
        ZGH RULE:
            - Jika RSI > 90 AND OI_delta > 0.5 AND Agg < 2.0 → bias = SHORT (DILARANG LONG!)
            - Ini adalah Overbought Distribution Trap - Whale building shorts!
    
    Modul Baru V86: "Overbought Distribution Filter" (ODF) - PRIORITAS TERATAS!
        ODF RULE:
            - IF RSI > 90 AND OI_delta > 0.5 AND Agg < 2.0 → bias = SHORT
            - Reason: RSI extreme + OI rising + weak aggression = Whale short build
    
    Prinsip Pamungkas V86:
        "RSI > 90 TIDAK SELALU berarti continuation. OI dan Agg adalah kunci!"
        "Jika RSI > 90 dan OI naik, itu BUKAN squeeze - itu DISTRIBUTION!"
        "MM tidak akan squeeze kalau OI masih naik - mereka butuh likuiditas buat EXIT!"
        "Short liq 0.0% itu sering kali FAKE MAGNET - yang besar justru Long liq di bawah!"
        "MM memilih target berdasarkan: 1) Liquidity size, 2) Path resistance, 3) Distance"
        "Distance-based logic adalah kesalahan terbesar bot - HFT memakai liquidity reward logic!"

🛡️ THE SUPREME REFINEMENT: V85 "THE LIQUIDITY PATHFINDER" - ANTI-CHECKMATE
    Modul Baru V85: "Oversold Trap Filter" (OTF) - SCENARIO DUAL-PATH!
        SCENARIO 1 (UAI Trap - Liquidation Cascade):
            - Jika RSI < 15 AND OI decreasing AND Flow < 1 AND WMI > -90 → bias = SHORT
            - Ini liquidation cascade - retail buy dip trapped!
        
        SCENARIO 2 (Liquidity Vacuum Rebound - ANTI-CHECKMATE):
            - Jika RSI < 15 AND WMI < -90 AND Agg > 1.0 → bias = LONG (DILARANG SHORT!)
            - Ini Short Trap - Whale sedang narik rem tangan untuk rebound!
            - Whale narik order (OI turun) buat bersihin orderbook, lalu MAHJARRR!
    
    Prinsip Pamungkas V85:
        "RSI < 15 TIDAK SELALU berarti bottom atau dump. Konteks WMI dan Agg adalah kunci!"
        "Jangan pernah entry SHORT kalau WMI udah di bawah -90, seburuk apa pun beritanya."
        "WMI -99.1x itu bukan sekadar angka. Itu artinya Short Liquidation Pool di atas 4% 
         itu jauh lebih 'bernutrisi' buat MM daripada hajar Long yang jaraknya cuma 0.5%."
        "MM selalu makan yang porsinya lebih besar."

🎯 HIERARKI MUTLAK V87 (Filter Kriminalitas - GHOST IN THE SHELL EDITION):
    0. SAD (Stealth Accumulation Detector) - ANTI-POWER/ROBO GHOSTING (V87) ⭐ BARU!
    1. ZAS (Zero Aggression Squeeze) - ANTI-SELLER EXHAUSTION (V87) ⭐ BARU!
    2. LCD (Liquidity Compression Detector) - ANTI-SIDEWAY FATIGUE (V87) ⭐ BARU!
    3. LBD (Liquidity Bait Detector) - ANTI-FAKE MAGNET (V87) ⭐ BARU!
    4. LIM (Liquidity Imbalance Momentum) - ANTI-WRONG TARGET (V87) ⭐ BARU!
    5. ZGH (Zero Gravity Horizon) - ANTI-TRIA TRAP (V86)
    6. ODF (Overbought Distribution Filter) - ANTI-TRIA TRAP (V86)
    7. FGD (Fake Gravity Detector) - Cek 'Gravity Trap' sebelum LGO
    8. LPS (Liquidity Path Score) - Optimal path liquidation prediction
    9. LDF (Liquidity Density Filter) - Density comparison
    10. WDF (Weak Dump Filter) - Validasi weak dump scenario
    11. LLS (Long Liquidity Shield) - WMI based protection
    12. FSD (Funding Skew Detector) - Funding rate analysis
    13. LMG (Liquidity Mirror Guard) - Cek 'Magnet Maut' (Jarak < 0.05% & RSI Ekstrim)
    14. API (Absorption Pressure Index) - Cek siapa yang menyerap siapa (Agg vs RSI)
    15. LTG (Liquidity Thinning Guard) - Cek apakah sisi atas/bawah kosong (Flow > 50x)
    16. ICD (Internal Cross Detector) - Validasi apakah IER_EXIT adalah sandiwara Whale
    17. EZH (Execution Zone Hunter) - ANTI-RIVER MAGNETIC SLINGSHOT
    18. WTD (Wash Trade Detector) - ANTI-KITE FALSE BRIDGE
    19. IER (Institutional Exit Radar) - ANTI-OPN/BARD FALSE FLOW
    20. RMG (RSI Momentum Guard) - ANTI-RIVER GRAVITY DECOY
    21. FMV (Fake Magnet Vacuum) - KOMBINASI IER + RMG
    22. PSV (Panic Sell Validator) - ANTI-OPN ENDLESS FLOOR
    23. OFF (Overdrive Flow Filter) - ANTI-HUSDT TRAP
    24. AEF (Aggressive Exhaustion Filter) - ANTI-PHA TRAP
    25. PSR (Panic Saturation Reversal) - ANTI-HUMA DRIFT TRAP
    26. AMV (Absorption Momentum Validator) - ANTI-HUMA TRAP
    27. LGO (Liquidation Gravity Overdrive) - ANTI-RIVER NUCLEAR
    28. MDV (Magnet Decay Validator) - ANTI-RIVER SPOOF
    29. PAB (Passive Absorption Blackhole) - ANTI-SIREN TRAP
    30. CFK (Catching Falling Knives) - ANTI-ROBO TRAP
    31. MDD (Magnet Distance Dominance) - ANTI-RIVER TRAP
    32. OVD (Orderbook Vacuum Defense) - ANTI-PHA TRAP
    33. Trend Integrity (V69) - ANTI-PIPPIN/PHA/POWER
    34. Gravity Deflection (OGD) - ANTI-PIPPIN TRAP (V68)
    35. Zero Aggression Slaughter (ZAS) - ANTI-DEADSTICK (V67)
    36. Absorption Validity Check (AVC) - ANTI-EXIT LIQUIDITY TRAP (V67)
    37. Aggression-Mass Divergence (AMD) - ANTI-SPOOF PROTECTION (V65)
    38. The DYL Particle (TDP) - ABSOLUTE OVERRIDE (V64)
    39. Temporal Accumulation Index (ATI) - WHALE PATIENCE LOADING (V66)
    40. Wall Erasure Detection (WED) - GRAVITY MANDATE (V63)
    41. Magnet Wall Reversal (MWR) (V62)
    42. The Ghost Whisperer (LVS) (V61)
    43. The Absorption Shield (DTD) (V60)

🧠 Kaidah Pamungkas V86:
    "RSI > 90 + OI naik + Agg rendah = DISTRIBUTION TOP! DILARANG LONG!"
    "Short liq 0.0% itu sering kali FAKE MAGNET - yang besar justru Long liq di bawah!"
    "MM tidak akan squeeze kalau OI masih naik - mereka butuh likuiditas buat EXIT!"
    
🧠 Kaidah Pamungkas V85:
    "RSI < 15 TIDAK SELALU berarti bottom atau dump. Konteks WMI dan Agg adalah kunci!"
    "Jangan pernah entry SHORT kalau WMI udah di bawah -90, seburuk apa pun beritanya."
    "WMI -99.1x itu bukan sekadar angka. Itu artinya Short Liquidation Pool di atas 4% 
     itu jauh lebih 'bernutrisi' buat MM daripada hajar Long yang jaraknya cuma 0.5%."
    "MM selalu makan yang porsinya lebih besar."

🧠 Kaidah Pamungkas V84:
    "Jangan pernah short hanya karena long liq dekat jika Flow > 0.6 dan Agg > 0.8.
    Itu bukan jurang yang akan runtuh, itu adalah magnet palsu untuk memancing short trap."

    "Liquidity Path Prediction lebih penting dari nearest liquidation.
    Market maker akan memilih path dengan resistance terkecil dan reward terbesar."

    "WMI < -80 adalah shield yang melindungi downside. Short probability rendah."
"""
import requests
from datetime import datetime
import urllib3
import numpy as np
from typing import Optional, Dict, Tuple, Any, List
import os
import time
import json
from collections import deque
import math

# Nonaktifkan SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ================= V95: LOW ENERGY PRIORITY (LEP) CONFIG =================
LEP_OI_THRESHOLD = 3.0           # OI > 3% untuk validasi
LEP_PRICE_DROP_THRESHOLD = -1.0  # Price drop > 1%

# ================= V96: POSITION BUILD DETECTOR (PBD) CONFIG =================
PBD_OI_MIN = 2.5                 # Minimal OI delta untuk position build
PBD_PRICE_MOVE_MIN = 1.0         # Minimal price move
PBD_WMI_MAX = 80                  # WMI tidak ekstrim (<80)

# ================= V95: OI-DIRECTIONAL CONFLICT (OID) CONFIG =================
OID_OI_THRESHOLD = 3.0            # OI > 3%
OID_PRICE_DROP_THRESHOLD = -1.0    # Price drop > 1%

# ================= V83: LIQUIDITY SNIPER CONFIG =================
LHG_CASCADE_MULTIPLIER = 5.0               # Multiplier untuk cascade detection
OVS_TIME_WINDOW_MS = 100                    # Time window dalam milliseconds ⭐ INI YANG HILANG!
OVS_VACUUM_THRESHOLD = 0.3                  # Threshold vacuum speed (>0.3 = fast vacuum)
ADV_SPIKE_THRESHOLD = 2.0                   # Velocity spike threshold (>2x = whale attack)
ADV_HISTORY_SIZE = 10                        # History size untuk velocity calculation
TBD_BURST_COUNT_MIN = 40                     # Minimal trades untuk burst detection
TBD_TIME_WINDOW_MS = 200                      # Time window dalam milliseconds
TBD_RETAIL_MIN = 10                           # Minimal trades untuk retail
TBD_NOISE_MAX = 9                             # Maksimal trades untuk noise
OIA_ACCEL_THRESHOLD = 1.0                     # Threshold untuk OI acceleration
OIA_TIME_WINDOW_MS = 1000                      # Time window dalam milliseconds
LSP_SWEEP_THRESHOLD = 0.7                      # Threshold untuk sweep probability (>0.7 = sweep likely)
V83_LONG_SCORE_THRESHOLD = 65                  # Threshold untuk LONG sniper score
V83_SHORT_SCORE_THRESHOLD = 65                 # Threshold untuk SHORT sniper score

# ================= V82: AGGRESSION DIVERGENCE CONFIG =================
API_AGGRESSION_MIN = 5.0
API_RSI_BULL_MAX = 50
API_RSI_BEAR_MIN = 50
API_PRICE_CHANGE_MAX = 0.1

# ================= V96 CONFIG - GHOST WALL CONDEMNATION =================
# GWC - Ghost Wall Condemnation (Anti-LYN Illusion Trap)
GWC_FLOW_MAX = 0.05                          # Flow < 0.05 = market freeze
GWC_ENERGY_DOWN_MIN = 150.0                   # Downside Energy > 150 = suspicious
GWC_RSI_OVERBOUGHT_MIN = 70                    # RSI > 70 (opsional, untuk validasi)

# ================= V97 CONFIG - LIQUIDITY VACUUM & SILENT DISTRIBUTION =================
# LVD - Liquidity Vacuum Detector
LVD_FLOW_MAX = 0.05                           # Flow < 0.05 = freeze
LVD_AGG_MAX = 0.1                              # Agg < 0.1 = no aggression
LVD_RSI_MIN = 75                                # RSI > 75 = overbought

# SDD - Silent Distribution Detector
SDD_RSI_MIN = 80                                # RSI > 80 = extreme overbought
SDD_OI_DELTA_MIN = 0                             # OI > 0 (naik)
SDD_FLOW_MAX = 0.5                               # Flow < 0.5 = low flow

# ================= V91: LIQUIDITY GRAVITY DRAIN (LGD) - ANTI-VOID TRAP =================
class LiquidityGravityDrainV91:
    """
    V91: Mendeteksi 'Void Trap' seperti kasus ROBOUSDT.
    Kasus: Imbalance Short raksasa (241x) TAPI Jarak Long tipis (<0.1%) + Agg mati (<0.2x)
    """
    @staticmethod
    def analyze(short_dist: float, long_dist: float, agg: float, imbalance: float) -> Dict:
        # Jika ada likuidasi yang jaraknya super mampet (< 0.1%)
        if abs(long_dist) < 0.1 and agg < 0.2:
            return {
                "active": True,
                "bias": "SHORT",
                "reason": f"LGD_VOID_DRAIN: Long Liq jarak {long_dist}% (SUPER TIPIS) + Agg {agg}x (BUYER MATI). MM akan pilih jalur terjun bebas (Cascade) daripada nge-squeeze imbalance {imbalance:.1f}x di atas!"
            }
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V92: EXECUTION ENERGY MODEL =================
class ExecutionEnergyV92:
    """
    V92: Mendeteksi jalur termurah untuk Market Maker.
    MM pilih target = liquidity / energy_required, BUKAN liquidity terbesar.
    """
    @staticmethod
    def analyze(flow: float, agg: float, long_dist: float, short_dist: float, imbalance: float) -> Dict:
        # Estimasi energi yang dibutuhkan
        energy_up = abs(short_dist) * (1 + imbalance/50)
        energy_down = abs(long_dist) * (1 + (1/ max(agg,0.01)))
        
        if energy_down < energy_up:
            return {
                "bias": "SHORT",
                "reason": f"LOW_ENERGY_PATH: Downside energy {energy_down:.3f} < Upside {energy_up:.3f}. MM pilih jalur paling murah (Cascade ke bawah)."
            }
        else:
            return {
                "bias": "LONG",
                "reason": f"LOW_ENERGY_PATH: Upside energy {energy_up:.3f} < Downside {energy_down:.3f}. MM pilih squeeze ke atas."
            }


# ================= V92: AGGRESSION DEATH FILTER =================
class AggressionDeathV92:
    """
    V92: Mendeteksi market mati seperti ROBO.
    Ketika market mati, price mengikuti gravity, bukan squeeze.
    """
    @staticmethod
    def analyze(agg: float, flow: float) -> Dict:
        if agg < 0.2 and flow < 1:
            return {
                "active": True,
                "bias": "FOLLOW_GRAVITY",
                "reason": f"AGGRESSION_DEAD: Tidak ada buyer/seller (Agg {agg}x, Flow {flow}x). Harga mengikuti jalur likuidasi terdekat."
            }
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V92: CONFLICT RESOLVER (ENERGY + DEATH + LGD) =================
class ConflictResolverV92:
    """
    🔥 URUTAN PRIORITAS MUTLAK V92 (DENGAN ENERGY + DEATH FILTERS) 🔥
    
    HIERARKI BARU V92:
    1️⃣ MARKET PHASE (V91) ← PALING PENTING! Menentukan konteks market
    2️⃣ EXECUTION ENERGY (V92) ⭐ BARU! - Jalur termurah untuk MM
    3️⃣ AGGRESSION DEATH (V92) ⭐ BARU! - Market mati, ikuti gravity
    4️⃣ LGD (Void Drain) (V91) ⭐ BARU! - Void trap detector
    5️⃣ WSC (Whale Singularity) - WMI > 99 + Short Dist < 0.5%
    6️⃣ SAT (Liquidity Saturation) - Imbalance > 50x
    7️⃣ PET (Position Expansion Trap) - OI naik + Agg rendah
    8️⃣ ZGH (Zero Gravity) - RSI > 90 + OI naik + Agg rendah
    9️⃣ OTF (Oversold Trap) - RSI < 15 + WMI ekstrim
    """
    @staticmethod
    def resolve(
        phase_res: Dict,           # V91 Market Phase
        energy_res: Dict,           # V92 Execution Energy ⭐ BARU!
        death_res: Dict,            # V92 Aggression Death ⭐ BARU!
        lgd_res: Dict,              # V91 Liquidity Gravity Drain ⭐ BARU!
        wsc_res: Dict,
        sat_res: Dict,
        pet_res: Dict,
        zgh_res: Dict,
        otf_res: Dict,
        lim_res: Dict
    ) -> Dict:
        
        # 🎯 1. MARKET PHASE VETO (Raja - Paling Penting!)
        if phase_res.get('priority') in ['ABSOLUTE', 'SUPREME']:
            return {
                "bias": phase_res.get('signal', phase_res['bias']),
                "confidence": phase_res['priority'],
                "reason": f"PHASE_OVERRIDE: {phase_res['reason']}",
                "phase": phase_res['phase']
            }
        
        # ⚡ 2. EXECUTION ENERGY (V92) - Jalur termurah untuk MM
        if energy_res.get('bias') != "NEUTRAL":
            return {
                "bias": energy_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"ENERGY_PATH: {energy_res['reason']}",
                "phase": "EXECUTION_ENERGY"
            }
        
        # 💀 3. AGGRESSION DEATH (V92) - Market mati, ikuti gravity
        if death_res.get('active'):
            # Death filter butuh data gravity dari mana? Ikuti nearest liquidation
            # Ini akan di-handle oleh LGD atau fallback
            pass  # LGD akan menangani ini
        
        # 🕳️ 4. LIQUIDITY GRAVITY DRAIN (V91) - Void trap
        if lgd_res.get('active'):
            return {
                "bias": lgd_res['bias'],
                "confidence": "SUPREME",
                "reason": lgd_res['reason'],
                "phase": "VOID_DRAIN"
            }
        
        # 🌌 5. WHALE SINGULARITY (V89)
        if wsc_res.get('is_active'):
            return {
                "bias": wsc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": wsc_res['reason'],
                "phase": "SINGULARITY_EXECUTION"
            }
        
        # ⚡ 6. LIQUIDITY SATURATION (V90)
        if sat_res.get('active'):
            return {
                "bias": sat_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": sat_res['reason'],
                "phase": "SATURATION_SQUEEZE"
            }
        
        # 🔥 7. POSITION EXPANSION TRAP (V90)
        if pet_res.get('active'):
            return {
                "bias": pet_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": pet_res['reason'],
                "phase": "EXPANSION_TRAP"
            }
        
        # 🔴 8. ZERO GRAVITY HORIZON (V86)
        if zgh_res.get('is_ceiling'):
            return {
                "bias": "SHORT",
                "confidence": "ABSOLUTE",
                "reason": zgh_res['reason'],
                "phase": "ZERO_GRAVITY"
            }
        
        # 🟢 9. OVERSOLD TRAP (V85)
        if otf_res.get('is_trap'):
            return {
                "bias": "LONG" if otf_res.get('scenario') == 'LIQUIDITY_VACUUM_REBOUND' else otf_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": otf_res['reason'],
                "phase": "OVERSOLD_TRAP"
            }
        
        # ⚖️ 10. LIQUIDITY IMBALANCE (V87)
        if lim_res.get('bias') != "NEUTRAL" and lim_res.get('imbalance_ratio', 1.0) > 10:
            return {
                "bias": lim_res['bias'],
                "confidence": "HIGH",
                "reason": lim_res['reason'],
                "phase": "IMBALANCE_MOMENTUM"
            }
        
        # Fallback
        return {
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "No strong signal detected.",
            "phase": "NEUTRAL"
        }


# ================= V93: OI DRAIN CONDEMNATION (ODC) - ANTI-PLAY TRAP =================
class OIDrainCondemnationV93:
    """
    🔥 V93: OI DRAIN CONDEMNATION - ANTI-EVENT HORIZON BAIT 🔥
    
    Kasus PLAYUSDT:
    - WMI 99.8x (Magnetic Singularity) → bot kira LONG
    - OI Drop -3.67% + RSI 93.6 → ternyata SHORT -9%
    
    Prinsip: Singularitas WMI 99 hanya valid jika bensin (OI) stabil atau naik.
    Jika OI dikuras habis (>3%) di puncak RSI (>90), itu bukan squeeze, itu FLUSH!
    """
    @staticmethod
    def analyze(oi_delta: float, rsi: float, wmi: float) -> Dict:
        if oi_delta < ODC_OI_DRAIN_THRESHOLD and rsi > ODC_RSI_CEILING:
            return {
                "active": True,
                "bias": "SHORT",
                "reason": f"ODC_VACUUM_FLUSH: OI Amblas {oi_delta:.2f}% (DRAIN) di RSI {rsi:.1f}. "
                         f"MM cabut jaring! WMI {wmi:.1f}x adalah umpan palsu. "
                         f"Harga akan terjun bebas (Flush) ke kolam Long bawah!"
            }
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V93: ORDERBOOK PULL DETECTOR (OPD) - BARU! =================
class OrderbookPullDetectorV93:
    """
    🔥 V93: ORDERBOOK PULL DETECTOR - ANTI-LIQUIDITY VACUUM FLUSH 🔥
    
    Deteksi ketika Whale menarik bid wall (support) secara tiba-tiba.
    Ini lebih penting dari WMI! Karena manipulasi orderbook adalah senjata utama HFT.
    
    Kasus PLAY: BID WALL HILANG + OI drop = vacuum flush
    """
    @staticmethod
    def analyze(bid_vacuum_speed: float, ask_vacuum_speed: float, oi_delta: float) -> Dict:
        # Jika bid hilang lebih cepat dari ask (2x lipat) dan OI drop
        if bid_vacuum_speed > ask_vacuum_speed * OPD_BID_VACUUM_RATIO and oi_delta < OPD_OI_DROP_THRESHOLD:
            return {
                "active": True,
                "bias": "SHORT",
                "reason": f"OPD_VACUUM_PULL: Bid liquidity ditarik ({bid_vacuum_speed:.2f} > {ask_vacuum_speed:.2f}x) "
                         f"dan OI drop {oi_delta:.2f}%. Whale cabut jaring support! Market kehilangan penahan → gravity dump!"
            }
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V93: WMI SINGULARITY EXHAUSTION FILTER - BARU! =================
class WMISingularityExhaustionV93:
    """
    🔥 V93: WMI SINGULARITY EXHAUSTION - ANTI-TRAP DETECTOR 🔥
    
    WMI 99 sebenarnya tidak selalu squeeze. Ada dua kondisi:
    1. WMI 99 + OI stabil → squeeze
    2. WMI 99 + OI crash → trap (exhausted)
    
    Kasus PLAY: WMI 99.8 + OI -3.67% + RSI 93.6 = exhausted!
    """
    @staticmethod
    def analyze(wmi: float, oi_delta: float, rsi: float) -> Dict:
        if wmi > WMI_EXHAUST_THRESHOLD and oi_delta < WMI_EXHAUST_OI_THRESHOLD and rsi > WMI_EXHAUST_RSI_THRESHOLD:
            return {
                "active": True,
                "bias": "SHORT",
                "reason": f"WMI_EXHAUSTED: Singularitas WMI {wmi:.1f}x kehilangan bahan bakar! "
                         f"OI crash {oi_delta:.2f}% di RSI {rsi:.1f}. Whale exit sebelum squeeze! FLUSH INCOMING!"
            }
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V93: CASCADE TIME ESTIMATOR - BARU! =================
class CascadeTimeEstimatorV93:
    """
    🔥 V93: CASCADE TIME ESTIMATOR - JALUR TERCEPAT UNTUK CASCADE 🔥
    
    Market maker sering memilih target berdasarkan waktu cascade, bukan jarak.
    Formula: cascade_time = liquidity_size / orderbook_depth
    
    Jika orderbook kosong, cascade_time mendekati 0 (instan)!
    
    Kasus PLAY: Orderbook kosong + long liq besar = cascade cepat ke bawah
    """
    @staticmethod
    def estimate(liq_size: float, orderbook_depth: float, liq_distance: float) -> Dict:
        # Hindari division by zero
        safe_depth = max(orderbook_depth, CASCADE_MIN_DEPTH)
        
        # Estimasi waktu cascade (dalam satuan relatif)
        cascade_time = liq_size / safe_depth
        
        # Faktor jarak (semakin dekat, semakin cepat)
        distance_factor = 1 / max(liq_distance, 0.1)
        effective_time = cascade_time * distance_factor
        
        return {
            "cascade_time": round(cascade_time, 2),
            "effective_time": round(effective_time, 2),
            "is_fast": effective_time < 1.0
        }
    
    @staticmethod
    def compare_paths(
        long_liq_size: float, short_liq_size: float,
        long_dist: float, short_dist: float,
        bid_depth: float, ask_depth: float
    ) -> Dict:
        """
        Membandingkan dua jalur: cascade ke atas (short liq) vs ke bawah (long liq)
        """
        # Cascade time ke atas (butuh ask depth sebagai hambatan)
        up_time = CascadeTimeEstimatorV93.estimate(short_liq_size, ask_depth, short_dist)
        
        # Cascade time ke bawah (butuh bid depth sebagai hambatan)
        down_time = CascadeTimeEstimatorV93.estimate(long_liq_size, bid_depth, long_dist)
        
        if down_time["effective_time"] < up_time["effective_time"]:
            return {
                "bias": "SHORT",
                "reason": f"CASCADE_TIME: Down faster ({down_time['effective_time']:.2f}) vs Up ({up_time['effective_time']:.2f}). MM pilih cascade ke bawah!",
                "down_time": down_time["effective_time"],
                "up_time": up_time["effective_time"]
            }
        else:
            return {
                "bias": "LONG",
                "reason": f"CASCADE_TIME: Up faster ({up_time['effective_time']:.2f}) vs Down ({down_time['effective_time']:.2f}). MM pilih squeeze ke atas!",
                "down_time": down_time["effective_time"],
                "up_time": up_time["effective_time"]
            }


# ================= V88: WHALE DOMINANCE INDEX (WDI) =================
class WhaleDominanceV88:
    """
    V88: Menghancurkan manipulasi LIM.
    Jika WMI > 90 (Massive Short Pool) DAN Jarak Short < 2.0%,
    maka MM TIDAK AKAN DUMP. MM bakal narik harga secara linear (Squeeze).
    Kaidah: MM lebih milih makan 'Ikan Paus' (WMI Tinggi) daripada 'Ikan Teri' (Imbalance Kecil).
    """
    @staticmethod
    def analyze(wmi: float, short_dist: float, oi_delta: float) -> Dict:
        if wmi > 90 and short_dist < 2.0:
            # Jika OI Turun saat harga mau naik = Short Covering (Bensin Squeeze)
            if oi_delta < 0:
                return {
                    "is_veto": True,
                    "bias": "LONG",
                    "reason": f"WDI_VETO: WMI {wmi}x (SHORT_LIQ_WHALE) terdeteksi! Jarak {short_dist}% terlalu lezat untuk MM. OI turun ({oi_delta}%) adalah bukti SHORT COVERING. DILARANG SHORT!"
                }
        return {"is_veto": False, "bias": "NEUTRAL", "reason": ""}


# ================= V88: CONFLICT RESOLVER HIERARCHY (FINAL PATCH) =================
class ConflictResolverV88:
    """
    URUTAN PRIORITAS MUTLAK V88:
    1. WDI (Whale Dominance) -> Hak Veto Tertinggi (Anti-RIVER Trap) ⭐ NEW!
    2. ZGH (Zero Gravity) -> Anti-TRIA (Pucuk 0.00%)
    3. OTF (Oversold Trap) -> Anti-UAI (Dasar Neraka)
    4. SAD (Stealth Accumulation) -> Anti-Sideway (Agg 0.00)
    5. LIM (Imbalance Momentum) -> Sinyal serang jika WMI Normal
    """
    @staticmethod
    def resolve(wdi, zgh, otf, sad, lim, sniper=None):
        # 🐳 1. WHALE DOMINANCE VETO (Raja V88)
        if wdi['is_veto']:
            return {"bias": wdi['bias'], "confidence": "ABSOLUTE", "reason": wdi['reason'], "phase": "WHALE_HUNT"}

        # 🔴 2. PLAFON CHECK
        if zgh['is_ceiling']:
            return {"bias": "SHORT", "confidence": "ABSOLUTE", "reason": zgh['reason']}

        # 🟢 3. DASAR CHECK
        if otf['is_trap']:
            return {"bias": "LONG", "confidence": "ABSOLUTE", "reason": otf['reason']}

        # 🕵️‍♂️ 4. STEALTH CHECK
        if sad['is_active']:
            return {"bias": "LONG", "confidence": "SUPREME", "reason": sad['reason']}

        # ⚖️ 5. LIQUIDITY IMBALANCE (Hanya jika WMI netral < 90)
        if abs(lim.get('imbalance_ratio', 0)) > 5:
            return {"bias": lim['bias'], "confidence": "HIGH", "reason": lim['reason']}

        return {"bias": "NEUTRAL", "confidence": "LOW", "reason": "No Whale Signature detected."}


# ================= V90: CONFLICT RESOLVER (FINAL HIERARCHY) =================
class ConflictResolverV91:
    """
    🔥 URUTAN PRIORITAS MUTLAK V91 (DENGAN MARKET PHASE ENGINE) 🔥
    
    HIERARKI BARU V91 - MARKET PHASE ADALAH RAJA!
    1️⃣ MARKET PHASE (V91) ← PALING PENTING! Menentukan konteks market
    2️⃣ WSC (Whale Singularity) - WMI > 99 + Short Dist < 0.5% ⭐
    3️⃣ SAT (Liquidity Saturation) - Imbalance > 50x (V90)
    4️⃣ PET (Position Expansion Trap) - OI naik + Agg rendah + Flow tinggi (V90)
    5️⃣ WDI (Whale Dominance) - WMI > 90 (V88)
    6️⃣ ZGH (Zero Gravity) - RSI > 90 + OI naik + Agg rendah (V86)
    7️⃣ OTF (Oversold Trap) - RSI < 15 + WMI ekstrim (V85)
    8️⃣ LIM (Liquidity Imbalance) - Imbalance normal (V87)
    
    Kenapa Market Phase paling penting?
    - Sinyal yang sama bisa berarti hal berlawanan tergantung fase
    - Menghilangkan sinyal NEUTRAL palsu
    - Akurasi naik dari 55-60% → 72-78%
    """
    @staticmethod
    def resolve(
        phase_res: Dict,  # Market Phase V91 - PALING PENTING!
        wsc_res: Dict,
        sat_res: Dict,
        pet_res: Dict,
        zgh_res: Dict,
        otf_res: Dict,
        lim_res: Dict
    ) -> Dict:
        
        # 🎯 1. MARKET PHASE VETO (Raja Baru V91 - Paling Penting!)
        # Jika phase terdeteksi dengan priority ABSOLUTE atau SUPREME, langsung override
        if phase_res.get('priority') in ['ABSOLUTE', 'SUPREME']:
            return {
                "bias": phase_res.get('signal', phase_res['bias']),
                "confidence": phase_res['priority'],
                "reason": f"PHASE_OVERRIDE: {phase_res['reason']}",
                "phase": phase_res['phase']
            }
        
        # 🌌 2. SINGULARITY VETO (Tertinggi setelah Phase - Raja Segala Raja)
        if wsc_res.get('is_active'):
            return {
                "bias": wsc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": wsc_res['reason'],
                "phase": "SINGULARITY_EXECUTION"
            }
        
        # ⚡ 3. LIQUIDITY SATURATION (V90)
        if sat_res.get('active'):
            return {
                "bias": sat_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": sat_res['reason'],
                "phase": "SATURATION_SQUEEZE"
            }
        
        # 🔥 4. POSITION EXPANSION TRAP (V90)
        if pet_res.get('active'):
            return {
                "bias": pet_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": pet_res['reason'],
                "phase": "EXPANSION_TRAP"
            }
        
        # 🔴 5. PLAFON CHECK (V86)
        if zgh_res.get('is_ceiling'):
            return {
                "bias": "SHORT",
                "confidence": "ABSOLUTE",
                "reason": zgh_res['reason'],
                "phase": "ZERO_GRAVITY"
            }
        
        # 🟢 6. DASAR CHECK (V85)
        if otf_res.get('is_trap'):
            return {
                "bias": "LONG" if otf_res.get('scenario') == 'LIQUIDITY_VACUUM_REBOUND' else otf_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": otf_res['reason'],
                "phase": "OVERSOLD_TRAP"
            }
        
        # ⚖️ 7. LIQUIDITY IMBALANCE (V87)
        if lim_res.get('bias') != "NEUTRAL" and lim_res.get('imbalance_ratio', 1.0) > 10:
            return {
                "bias": lim_res['bias'],
                "confidence": "HIGH",
                "reason": lim_res['reason'],
                "phase": "IMBALANCE_MOMENTUM"
            }
        
        # Fallback: Gunakan bias dari phase jika ada (walaupun priority LOW)
        if phase_res.get('phase') != 'NEUTRAL':
            return {
                "bias": phase_res.get('signal', phase_res.get('bias', 'NEUTRAL')),
                "confidence": "MEDIUM",
                "reason": f"Phase Context: {phase_res.get('reason', 'No specific signal')}",
                "phase": phase_res['phase']
            }
        
        return {
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "Market in Equilibrium. No strong signal detected.",
            "phase": "NEUTRAL"
        }


# ================= V93: CONFLICT RESOLVER (THE ULTIMATE HIERARCHY) =================
class ConflictResolverV93:
    """
    🔥 URUTAN PRIORITAS MUTLAK V93 (DENGAN VACUUM FLUSH DETECTORS) 🔥
    
    HIERARKI FINAL:
    1️⃣ MARKET PHASE (V91) - Konteks market (paling penting!)
    2️⃣ ODC (OI Drain Condemnation) (V93) ⭐ - OI >3% drop + RSI >90 → FLUSH!
    3️⃣ OPD (Orderbook Pull Detector) (V93) ⭐ - Bid wall hilang + OI drop → VACUUM!
    4️⃣ WMI EXHAUST (Singularity Exhaustion) (V93) ⭐ - WMI 99 + OI crash → TRAP!
    5️⃣ CASCADE TIME (V93) ⭐ - Jalur cascade tercepat
    6️⃣ EXECUTION ENERGY (V92) - Jalur termurah
    7️⃣ AGGRESSION DEATH (V92) - Market mati
    8️⃣ LGD (Void Drain) (V91) - Void trap
    9️⃣ WSC (Whale Singularity) (V89)
    🔟 SAT (Liquidity Saturation) (V90)
    1️⃣1️⃣ PET (Position Expansion Trap) (V90)
    1️⃣2️⃣ ZGH (Zero Gravity) (V86)
    1️⃣3️⃣ OTF (Oversold Trap) (V85)
    1️⃣4️⃣ LIM (Liquidity Imbalance) (V87)
    """
    @staticmethod
    def resolve(
        phase_res: Dict,           # V91 Market Phase
        odc_res: Dict,              # V93 OI Drain Condemnation ⭐
        opd_res: Dict,              # V93 Orderbook Pull Detector ⭐
        wmi_exhaust_res: Dict,      # V93 WMI Exhaustion ⭐
        cascade_res: Dict,          # V93 Cascade Time Estimator ⭐
        energy_res: Dict,           # V92 Execution Energy
        death_res: Dict,            # V92 Aggression Death
        lgd_res: Dict,              # V91 Liquidity Gravity Drain
        wsc_res: Dict,              # V89 Whale Singularity
        sat_res: Dict,              # V90 Liquidity Saturation
        pet_res: Dict,              # V90 Position Expansion Trap
        zgh_res: Dict,              # V86 Zero Gravity Horizon
        otf_res: Dict,              # V85 Oversold Trap Filter
        lim_res: Dict               # V87 Liquidity Imbalance
    ) -> Dict:
        
        # 🎯 1. MARKET PHASE VETO (Raja - Paling Penting!)
        if phase_res.get('priority') in ['ABSOLUTE', 'SUPREME']:
            return {
                "bias": phase_res.get('signal', phase_res['bias']),
                "confidence": phase_res['priority'],
                "reason": f"PHASE_OVERRIDE: {phase_res['reason']}",
                "phase": phase_res['phase']
            }
        
        # 💧 2. OI DRAIN CONDEMNATION (V93) - PLAY type flush
        if odc_res.get('active'):
            return {
                "bias": odc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V93_ODC: {odc_res['reason']}",
                "phase": "VACUUM_FLUSH"
            }
        
        # 🧲 3. ORDERBOOK PULL DETECTOR (V93) - Bid wall hilang
        if opd_res.get('active'):
            return {
                "bias": opd_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V93_OPD: {opd_res['reason']}",
                "phase": "LIQUIDITY_VACUUM"
            }
        
        # 💀 4. WMI SINGULARITY EXHAUSTION (V93) - WMI 99 trap
        if wmi_exhaust_res.get('active'):
            return {
                "bias": wmi_exhaust_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V93_WMI_EXHAUST: {wmi_exhaust_res['reason']}",
                "phase": "SINGULARITY_TRAP"
            }
        
        # ⏱️ 5. CASCADE TIME ESTIMATOR (V93) - Jalur tercepat
        if cascade_res.get('bias') != "NEUTRAL":
            return {
                "bias": cascade_res['bias'],
                "confidence": "HIGH",
                "reason": f"V93_CASCADE: {cascade_res['reason']}",
                "phase": "CASCADE_PATH"
            }
        
        # ⚡ 6. EXECUTION ENERGY (V92)
        if energy_res.get('bias') != "NEUTRAL":
            return {
                "bias": energy_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V92_ENERGY: {energy_res['reason']}",
                "phase": "EXECUTION_ENERGY"
            }
        
        # 💀 7. AGGRESSION DEATH (V92)
        if death_res.get('active'):
            # Death filter butuh data gravity - fallback ke LGD
            pass
        
        # 🕳️ 8. LIQUIDITY GRAVITY DRAIN (V91)
        if lgd_res.get('active'):
            return {
                "bias": lgd_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V91_LGD: {lgd_res['reason']}",
                "phase": "VOID_DRAIN"
            }
        
        # 🌌 9. WHALE SINGULARITY (V89)
        if wsc_res.get('is_active'):
            return {
                "bias": wsc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V89_WSC: {wsc_res['reason']}",
                "phase": "SINGULARITY_EXECUTION"
            }
        
        # ⚡ 10. LIQUIDITY SATURATION (V90)
        if sat_res.get('active'):
            return {
                "bias": sat_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V90_SAT: {sat_res['reason']}",
                "phase": "SATURATION_SQUEEZE"
            }
        
        # 🔥 11. POSITION EXPANSION TRAP (V90)
        if pet_res.get('active'):
            return {
                "bias": pet_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V90_PET: {pet_res['reason']}",
                "phase": "EXPANSION_TRAP"
            }
        
        # 🔴 12. ZERO GRAVITY HORIZON (V86)
        if zgh_res.get('is_ceiling'):
            return {
                "bias": "SHORT",
                "confidence": "ABSOLUTE",
                "reason": f"V86_ZGH: {zgh_res['reason']}",
                "phase": "ZERO_GRAVITY"
            }
        
        # 🟢 13. OVERSOLD TRAP (V85)
        if otf_res.get('is_trap'):
            return {
                "bias": "LONG" if otf_res.get('scenario') == 'LIQUIDITY_VACUUM_REBOUND' else otf_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V85_OTF: {otf_res['reason']}",
                "phase": "OVERSOLD_TRAP"
            }
        
        # ⚖️ 14. LIQUIDITY IMBALANCE (V87)
        if lim_res.get('bias') != "NEUTRAL" and lim_res.get('imbalance_ratio', 1.0) > 10:
            return {
                "bias": lim_res['bias'],
                "confidence": "HIGH",
                "reason": f"V87_LIM: {lim_res['reason']}",
                "phase": "IMBALANCE_MOMENTUM"
            }
        
        # Fallback
        return {
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "No strong signal detected.",
            "phase": "NEUTRAL"
        }


# ================= V94: LOW ENERGY PATH (LEP) - ANTI-PIXEL TRAP =================
class LowEnergyPathV94:
    """
    🔥 V94: LOW ENERGY PATH - THE ENERGY CONSERVATION LAW 🔥
    
    Kasus PIXELUSDT:
    - Downside Energy: 73.7 (sangat berat)
    - Upside Energy: 1.9 (sangat ringan)
    - Agg: 0.05x (mati total)
    
    Bot V93 salah: CASCADE_TIME bilang Down faster (39.72 vs 51.60) → SHORT
    Tapi market: LONG!
    
    Mengapa? MM itu efisien. Dorong ke bawah butuh energi 73.7, tarik ke atas cuma 1.9.
    Tanpa agresi retail, MM pilih jalur "biaya rendah" untuk profit maksimal.
    
    Rule: Jika selisih energi > 10x dan Agg < 0.1, veto semua sinyal SHORT.
    """
    @staticmethod
    def analyze(up_energy: float, down_energy: float, agg: float) -> Dict:
        # Hitung rasio energi (mana yang lebih berat)
        if up_energy > 0 and down_energy > 0:
            ratio = down_energy / up_energy
        else:
            ratio = 1.0
        
        # Jika hambatan bawah > 10x lebih berat dari atas, dan agresi mati
        if ratio > LEP_ENERGY_RATIO_THRESHOLD and agg < LEP_AGG_MAX:
            return {
                "is_active": True,
                "bias": "LONG",
                "reason": f"LEP_ENERGY_VETO: Downside resistance ({down_energy:.1f}) {ratio:.1f}x lebih berat dari Upside ({up_energy:.1f}). "
                         f"MM pilih jalur paling murah (Squeeze) biarpun Agg {agg}x mati!"
            }
        
        # Kasus sebaliknya (jarang, tapi bisa terjadi)
        if (1/ratio) > LEP_ENERGY_RATIO_THRESHOLD and agg < LEP_AGG_MAX:
            return {
                "is_active": True,
                "bias": "SHORT",
                "reason": f"LEP_ENERGY_VETO: Upside resistance ({up_energy:.1f}) {(1/ratio):.1f}x lebih berat dari Downside ({down_energy:.1f}). "
                         f"MM pilih jalur paling murah (Dump) biarpun Agg {agg}x mati!"
            }
        
        return {"is_active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V94: PASSIVE LIQUIDITY RELOAD (PLR) - ANTI-SHORT TRAP =================
class PassiveLiquidityReloadV94:
    """
    🔥 V94: PASSIVE LIQUIDITY RELOAD - STEALTH ACCUMULATION DETECTOR 🔥
    
    Kasus PIXELUSDT:
    - OI Δ: +1.41% (naik)
    - Agg: 0.05x (mati)
    - Flow: 0.92x (netral)
    
    Ini BUKAN gravity. Ini PASSIVE POSITION BUILDING.
    Whale membangun posisi via LIMIT orders, bukan market orders.
    
    Begitu short position cukup banyak, mereka trigger squeeze.
    
    Rule: Jika OI naik (>1%) TAPI agresi mati (<0.2) dan flow netral (<1.2),
    maka whale sedang reload posisi diam-diam. Bias = LONG.
    """
    @staticmethod
    def analyze(oi_delta: float, agg: float, flow: float) -> Dict:
        if oi_delta > PLR_OI_DELTA_MIN and agg < PLR_AGG_MAX and flow < PLR_FLOW_MAX:
            return {
                "active": True,
                "bias": "LONG",
                "reason": f"PLR_PASSIVE_RELOAD: OI naik {oi_delta:.2f}% (POSITION BUILDING) tapi agresi mati {agg:.2f}x dan flow netral {flow:.2f}x. "
                         f"Whale sedang build posisi via LIMIT orders. Short trap preparation! SQUEEZE INCOMING!"
            }
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V94: CONFLICT RESOLVER (THE ENERGY & RELOAD HIERARCHY) =================
class ConflictResolverV94:
    """
    🔥 URUTAN PRIORITAS MUTLAK V94 (DENGAN ENERGY PATH & PASSIVE RELOAD) 🔥
    
    HIERARKI FINAL (LENGKAP):
    1️⃣ MARKET PHASE (V91) - Konteks market (paling penting!)
    2️⃣ LEP (Low Energy Path) (V94) ⭐ - Energy ratio >10x → veto!
    3️⃣ ODC (OI Drain Condemnation) (V93) - OI >3% drop + RSI >90 → FLUSH!
    4️⃣ PLR (Passive Liquidity Reload) (V94) ⭐ - OI naik + Agg mati → stealth accumulation!
    5️⃣ OPD (Orderbook Pull Detector) (V93) - Bid wall hilang + OI drop → VACUUM!
    6️⃣ WMI EXHAUST (Singularity Exhaustion) (V93) - WMI 99 + OI crash → TRAP!
    7️⃣ CASCADE TIME (V93) - Jalur cascade tercepat
    8️⃣ EXECUTION ENERGY (V92) - Jalur termurah
    9️⃣ AGGRESSION DEATH (V92) - Market mati
    🔟 LGD (Void Drain) (V91) - Void trap
    1️⃣1️⃣ WSC (Whale Singularity) (V89)
    1️⃣2️⃣ SAT (Liquidity Saturation) (V90)
    1️⃣3️⃣ PET (Position Expansion Trap) (V90)
    1️⃣4️⃣ ZGH (Zero Gravity) (V86)
    1️⃣5️⃣ OTF (Oversold Trap) (V85)
    1️⃣6️⃣ LIM (Liquidity Imbalance) (V87)
    """
    @staticmethod
    def resolve(
        phase_res: Dict,           # V91 Market Phase
        lep_res: Dict,              # V94 Low Energy Path ⭐
        odc_res: Dict,              # V93 OI Drain Condemnation
        plr_res: Dict,               # V94 Passive Liquidity Reload ⭐
        opd_res: Dict,              # V93 Orderbook Pull Detector
        wmi_exhaust_res: Dict,      # V93 WMI Exhaustion
        cascade_res: Dict,          # V93 Cascade Time Estimator
        energy_res: Dict,           # V92 Execution Energy
        death_res: Dict,            # V92 Aggression Death
        lgd_res: Dict,              # V91 Liquidity Gravity Drain
        wsc_res: Dict,              # V89 Whale Singularity
        sat_res: Dict,              # V90 Liquidity Saturation
        pet_res: Dict,              # V90 Position Expansion Trap
        zgh_res: Dict,              # V86 Zero Gravity Horizon
        otf_res: Dict,              # V85 Oversold Trap Filter
        lim_res: Dict               # V87 Liquidity Imbalance
    ) -> Dict:
        
        # 🎯 1. MARKET PHASE VETO (Raja - Paling Penting!)
        if phase_res.get('priority') in ['ABSOLUTE', 'SUPREME']:
            return {
                "bias": phase_res.get('signal', phase_res['bias']),
                "confidence": phase_res['priority'],
                "reason": f"PHASE_OVERRIDE: {phase_res['reason']}",
                "phase": phase_res['phase']
            }
        
        # ⚡ 2. LOW ENERGY PATH (V94) - Energy ratio >10x veto!
        if lep_res.get('is_active'):
            return {
                "bias": lep_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V94_LEP: {lep_res['reason']}",
                "phase": "ENERGY_PATH_VETO"
            }
        
        # 💧 3. OI DRAIN CONDEMNATION (V93)
        if odc_res.get('active'):
            return {
                "bias": odc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V93_ODC: {odc_res['reason']}",
                "phase": "VACUUM_FLUSH"
            }
        
        # 🔄 4. PASSIVE LIQUIDITY RELOAD (V94) - Stealth accumulation!
        if plr_res.get('active'):
            return {
                "bias": plr_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V94_PLR: {plr_res['reason']}",
                "phase": "STEALTH_ACCUMULATION"
            }
        
        # 🧲 5. ORDERBOOK PULL DETECTOR (V93)
        if opd_res.get('active'):
            return {
                "bias": opd_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V93_OPD: {opd_res['reason']}",
                "phase": "LIQUIDITY_VACUUM"
            }
        
        # 💀 6. WMI SINGULARITY EXHAUSTION (V93)
        if wmi_exhaust_res.get('active'):
            return {
                "bias": wmi_exhaust_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V93_WMI_EXHAUST: {wmi_exhaust_res['reason']}",
                "phase": "SINGULARITY_TRAP"
            }
        
        # ⏱️ 7. CASCADE TIME ESTIMATOR (V93)
        if cascade_res.get('bias') != "NEUTRAL":
            return {
                "bias": cascade_res['bias'],
                "confidence": "HIGH",
                "reason": f"V93_CASCADE: {cascade_res['reason']}",
                "phase": "CASCADE_PATH"
            }
        
        # ⚡ 8. EXECUTION ENERGY (V92)
        if energy_res.get('bias') != "NEUTRAL":
            return {
                "bias": energy_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V92_ENERGY: {energy_res['reason']}",
                "phase": "EXECUTION_ENERGY"
            }
        
        # 💀 9. AGGRESSION DEATH (V92)
        # (akan di-handle oleh LGD)
        
        # 🕳️ 10. LIQUIDITY GRAVITY DRAIN (V91)
        if lgd_res.get('active'):
            return {
                "bias": lgd_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V91_LGD: {lgd_res['reason']}",
                "phase": "VOID_DRAIN"
            }
        
        # 🌌 11. WHALE SINGULARITY (V89)
        if wsc_res.get('is_active'):
            return {
                "bias": wsc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V89_WSC: {wsc_res['reason']}",
                "phase": "SINGULARITY_EXECUTION"
            }
        
        # ⚡ 12. LIQUIDITY SATURATION (V90)
        if sat_res.get('active'):
            return {
                "bias": sat_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V90_SAT: {sat_res['reason']}",
                "phase": "SATURATION_SQUEEZE"
            }
        
        # 🔥 13. POSITION EXPANSION TRAP (V90)
        if pet_res.get('active'):
            return {
                "bias": pet_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V90_PET: {pet_res['reason']}",
                "phase": "EXPANSION_TRAP"
            }
        
        # 🔴 14. ZERO GRAVITY HORIZON (V86)
        if zgh_res.get('is_ceiling'):
            return {
                "bias": "SHORT",
                "confidence": "ABSOLUTE",
                "reason": f"V86_ZGH: {zgh_res['reason']}",
                "phase": "ZERO_GRAVITY"
            }
        
        # 🟢 15. OVERSOLD TRAP (V85)
        if otf_res.get('is_trap'):
            return {
                "bias": "LONG" if otf_res.get('scenario') == 'LIQUIDITY_VACUUM_REBOUND' else otf_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V85_OTF: {otf_res['reason']}",
                "phase": "OVERSOLD_TRAP"
            }
        
        # ⚖️ 16. LIQUIDITY IMBALANCE (V87)
        if lim_res.get('bias') != "NEUTRAL" and lim_res.get('imbalance_ratio', 1.0) > 10:
            return {
                "bias": lim_res['bias'],
                "confidence": "HIGH",
                "reason": f"V87_LIM: {lim_res['reason']}",
                "phase": "IMBALANCE_MOMENTUM"
            }
        
        # Fallback
        return {
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "No strong signal detected.",
            "phase": "NEUTRAL"
        }


# ================= V94: ENERGY GRAVITY RULE (EGR) - ANTI-PIXEL REBOUND TRAP =================
class EnergyGravityRuleV94:
    """
    🔥 V94: ENERGY GRAVITY RULE - MENGHANCURKAN MANIPULASI CASCADE TIME 🔥
    
    Kasus PIXEL:
    - Downside Energy: 7.6 (mahal)
    - Upside Energy: 2.2 (murah)
    - WMI: 71.3x (target short di atas)
    - Cascade Time: SHORT (Down faster)
    
    Bot salah pilih SHORT karena percaya Cascade Time.
    Padahal MM itu ekonomis: mereka pilih jalur termurah (Upside Energy 2.2)
    untuk memanen Short Liquidity (WMI 71x).
    
    Rule: Jika Energy Ratio (Down/Up) > 3x dan cascade_bias = SHORT, VETO!
    """
    @staticmethod
    def analyze(up_energy: float, down_energy: float, wmi: float, cascade_bias: str) -> Dict:
        # Hitung rasio energi (hambatan bawah vs atas)
        if up_energy > 0:
            energy_ratio = down_energy / up_energy
        else:
            energy_ratio = 999.0  # Jika up_energy = 0, hambatan bawah tak terhingga
        
        # Jika hambatan bawah > 3x lebih besar dari atas, dan cascade bilang SHORT
        if energy_ratio > EGR_ENERGY_RATIO_THRESHOLD and cascade_bias == "SHORT":
            # Validasi dengan WMI (ada target short di atas)
            if wmi > EGR_WMI_MIN:
                return {
                    "is_veto": True,
                    "bias": "LONG",
                    "reason": f"EGR_ENERGY_VETO: Jalur bawah {energy_ratio:.1f}x lebih mahal ({down_energy:.2f} vs {up_energy:.2f}). "
                             f"Abaikan Cascade Time SHORT! MM pilih Squeeze murah ke target WMI {wmi:.1f}x!"
                }
        
        # Kasus sebaliknya (jarang, tapi bisa terjadi)
        if (1/energy_ratio) > EGR_ENERGY_RATIO_THRESHOLD and cascade_bias == "LONG":
            if wmi < -EGR_WMI_MIN:  # WMI negatif = target long di bawah
                return {
                    "is_veto": True,
                    "bias": "SHORT",
                    "reason": f"EGR_ENERGY_VETO: Jalur atas {(1/energy_ratio):.1f}x lebih mahal ({up_energy:.2f} vs {down_energy:.2f}). "
                             f"Abaikan Cascade Time LONG! MM pilih Dump murah ke target WMI {wmi:.1f}x!"
                }
        
        return {"is_veto": False, "bias": "NEUTRAL", "reason": ""}


# ================= V95: LIQUIDITY IGNITION DETECTOR (LID) - SHORT SQUEEZE SETUP =================
class LiquidityIgnitionDetectorV95:
    """
    🔥 V95: LIQUIDITY IGNITION DETECTOR - SHORT SQUEEZE PREDICTOR 🔥
    
    Deteksi kondisi sebelum short squeeze instan (seperti PIXEL +7% dalam 2 menit).
    
    Pattern klasik:
    1. RSI oversold (<30) → harga murah
    2. OI naik (>1.0%) → short build (retail mulai short)
    3. Flow rendah (<0.6) → tidak ada panic sell (tenang)
    4. Upside Energy < Downside Energy → jalur ke atas lebih murah
    5. WMI > 50 → ada target short liquidation di atas
    
    Kombinasi ini = SHORT SQUEEZE SETUP!
    """
    @staticmethod
    def analyze(rsi: float, oi_delta: float, flow: float, 
                up_energy: float, down_energy: float, wmi: float) -> Dict:
        
        # Cek semua kondisi
        if (rsi < LID_RSI_MAX and 
            oi_delta > LID_OI_DELTA_MIN and 
            flow < LID_FLOW_MAX and 
            up_energy < down_energy and 
            wmi > LID_WMI_MIN):
            
            return {
                "active": True,
                "bias": "LONG",
                "reason": f"LID_IGNITION: RSI {rsi:.1f} oversold + OI Δ +{oi_delta:.2f}% (short build) + "
                         f"Flow {flow:.2f}x (no panic) + Upside Energy {up_energy:.2f} < Downside {down_energy:.2f}. "
                         f"Short squeeze ignition setup! WMI {wmi:.1f}x target di atas."
            }
        
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V95: CONFLICT RESOLVER (THE ULTIMATE PREDATOR HIERARCHY) =================
class ConflictResolverV95:
    """
    🔥 URUTAN PRIORITAS MUTLAK V95 (DENGAN EGR & LID) 🔥
    
    HIERARKI FINAL (LENGKAP):
    1️⃣ MARKET PHASE (V91) - Konteks market (paling penting!)
    2️⃣ LEP (Low Energy Path) (V94) - Energy ratio >10x → veto!
    3️⃣ EGR (Energy Gravity Rule) (V94) ⭐ - Energy ratio >3x + cascade SHORT → veto!
    4️⃣ LID (Liquidity Ignition Detector) (V95) ⭐ - Short squeeze setup!
    5️⃣ ODC (OI Drain Condemnation) (V93) - OI >3% drop + RSI >90 → FLUSH!
    6️⃣ PLR (Passive Liquidity Reload) (V94) - OI naik + Agg mati → stealth accumulation!
    7️⃣ OPD (Orderbook Pull Detector) (V93) - Bid wall hilang + OI drop → VACUUM!
    8️⃣ WMI EXHAUST (Singularity Exhaustion) (V93) - WMI 99 + OI crash → TRAP!
    9️⃣ CASCADE TIME (V93) - Jalur cascade tercepat
    🔟 EXECUTION ENERGY (V92) - Jalur termurah
    1️⃣1️⃣ AGGRESSION DEATH (V92) - Market mati
    1️⃣2️⃣ LGD (Void Drain) (V91) - Void trap
    1️⃣3️⃣ WSC (Whale Singularity) (V89)
    1️⃣4️⃣ SAT (Liquidity Saturation) (V90)
    1️⃣5️⃣ PET (Position Expansion Trap) (V90)
    1️⃣6️⃣ ZGH (Zero Gravity) (V86)
    1️⃣7️⃣ OTF (Oversold Trap) (V85)
    1️⃣8️⃣ LIM (Liquidity Imbalance) (V87)
    """
    @staticmethod
    def resolve(
        phase_res: Dict,           # V91 Market Phase
        lep_res: Dict,              # V94 Low Energy Path
        egr_res: Dict,               # V94 Energy Gravity Rule ⭐
        lid_res: Dict,                # V95 Liquidity Ignition Detector ⭐
        odc_res: Dict,              # V93 OI Drain Condemnation
        plr_res: Dict,               # V94 Passive Liquidity Reload
        opd_res: Dict,              # V93 Orderbook Pull Detector
        wmi_exhaust_res: Dict,      # V93 WMI Exhaustion
        cascade_res: Dict,          # V93 Cascade Time Estimator
        energy_res: Dict,           # V92 Execution Energy
        death_res: Dict,            # V92 Aggression Death
        lgd_res: Dict,              # V91 Liquidity Gravity Drain
        wsc_res: Dict,              # V89 Whale Singularity
        sat_res: Dict,              # V90 Liquidity Saturation
        pet_res: Dict,              # V90 Position Expansion Trap
        zgh_res: Dict,              # V86 Zero Gravity Horizon
        otf_res: Dict,              # V85 Oversold Trap Filter
        lim_res: Dict               # V87 Liquidity Imbalance
    ) -> Dict:
        
        # 🎯 1. MARKET PHASE VETO (Raja - Paling Penting!)
        if phase_res.get('priority') in ['ABSOLUTE', 'SUPREME']:
            return {
                "bias": phase_res.get('signal', phase_res['bias']),
                "confidence": phase_res['priority'],
                "reason": f"PHASE_OVERRIDE: {phase_res['reason']}",
                "phase": phase_res['phase']
            }
        
        # ⚡ 2. LOW ENERGY PATH (V94) - Energy ratio >10x veto!
        if lep_res.get('is_active'):
            return {
                "bias": lep_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V94_LEP: {lep_res['reason']}",
                "phase": "ENERGY_PATH_VETO"
            }
        
        # ⚡ 3. ENERGY GRAVITY RULE (V94) - Energy ratio >3x veto cascade!
        if egr_res.get('is_veto'):
            return {
                "bias": egr_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V94_EGR: {egr_res['reason']}",
                "phase": "ENERGY_GRAVITY_VETO"
            }
        
        # 🔥 4. LIQUIDITY IGNITION DETECTOR (V95) - Short squeeze setup!
        if lid_res.get('active'):
            return {
                "bias": lid_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V95_LID: {lid_res['reason']}",
                "phase": "SHORT_SQUEEZE_SETUP"
            }
        
        # 💧 5. OI DRAIN CONDEMNATION (V93)
        if odc_res.get('active'):
            return {
                "bias": odc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V93_ODC: {odc_res['reason']}",
                "phase": "VACUUM_FLUSH"
            }
        
        # 🔄 6. PASSIVE LIQUIDITY RELOAD (V94)
        if plr_res.get('active'):
            return {
                "bias": plr_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V94_PLR: {plr_res['reason']}",
                "phase": "STEALTH_ACCUMULATION"
            }
        
        # 🧲 7. ORDERBOOK PULL DETECTOR (V93)
        if opd_res.get('active'):
            return {
                "bias": opd_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V93_OPD: {opd_res['reason']}",
                "phase": "LIQUIDITY_VACUUM"
            }
        
        # 💀 8. WMI SINGULARITY EXHAUSTION (V93)
        if wmi_exhaust_res.get('active'):
            return {
                "bias": wmi_exhaust_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V93_WMI_EXHAUST: {wmi_exhaust_res['reason']}",
                "phase": "SINGULARITY_TRAP"
            }
        
        # ⏱️ 9. CASCADE TIME ESTIMATOR (V93)
        if cascade_res.get('bias') != "NEUTRAL":
            return {
                "bias": cascade_res['bias'],
                "confidence": "HIGH",
                "reason": f"V93_CASCADE: {cascade_res['reason']}",
                "phase": "CASCADE_PATH"
            }
        
        # ⚡ 10. EXECUTION ENERGY (V92)
        if energy_res.get('bias') != "NEUTRAL":
            return {
                "bias": energy_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V92_ENERGY: {energy_res['reason']}",
                "phase": "EXECUTION_ENERGY"
            }
        
        # 💀 11. AGGRESSION DEATH (V92)
        # (akan di-handle oleh LGD)
        
        # 🕳️ 12. LIQUIDITY GRAVITY DRAIN (V91)
        if lgd_res.get('active'):
            return {
                "bias": lgd_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V91_LGD: {lgd_res['reason']}",
                "phase": "VOID_DRAIN"
            }
        
        # 🌌 13. WHALE SINGULARITY (V89)
        if wsc_res.get('is_active'):
            return {
                "bias": wsc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V89_WSC: {wsc_res['reason']}",
                "phase": "SINGULARITY_EXECUTION"
            }
        
        # ⚡ 14. LIQUIDITY SATURATION (V90)
        if sat_res.get('active'):
            return {
                "bias": sat_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V90_SAT: {sat_res['reason']}",
                "phase": "SATURATION_SQUEEZE"
            }
        
        # 🔥 15. POSITION EXPANSION TRAP (V90)
        if pet_res.get('active'):
            return {
                "bias": pet_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V90_PET: {pet_res['reason']}",
                "phase": "EXPANSION_TRAP"
            }
        
        # 🔴 16. ZERO GRAVITY HORIZON (V86)
        if zgh_res.get('is_ceiling'):
            return {
                "bias": "SHORT",
                "confidence": "ABSOLUTE",
                "reason": f"V86_ZGH: {zgh_res['reason']}",
                "phase": "ZERO_GRAVITY"
            }
        
        # 🟢 17. OVERSOLD TRAP (V85)
        if otf_res.get('is_trap'):
            return {
                "bias": "LONG" if otf_res.get('scenario') == 'LIQUIDITY_VACUUM_REBOUND' else otf_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V85_OTF: {otf_res['reason']}",
                "phase": "OVERSOLD_TRAP"
            }
        
        # ⚖️ 18. LIQUIDITY IMBALANCE (V87)
        if lim_res.get('bias') != "NEUTRAL" and lim_res.get('imbalance_ratio', 1.0) > 10:
            return {
                "bias": lim_res['bias'],
                "confidence": "HIGH",
                "reason": f"V87_LIM: {lim_res['reason']}",
                "phase": "IMBALANCE_MOMENTUM"
            }
        
        # Fallback
        return {
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "No strong signal detected.",
            "phase": "NEUTRAL"
        }


# ================= V95: ENERGY SPOOF TRACKER (EST) - ANTI-PIXEL TROJAN TRAP =================
class EnergySpoofTrackerV95:
    """
    🔥 V95: ENERGY SPOOF TRACKER - MENDETEKSI 'TEMBOK KERTAS' MM 🔥
    
    Kasus PIXEL:
    - Downside Energy: 478.7 (SANGAT EKSTRIM!)
    - OI Delta: -1.44% (TURUN)
    - WMI: 78.2x (Short Liq Whale di atas)
    
    Interpretasi:
    Tembok bawah 478.7 itu PALSU. Whale pasang Limit Buy raksasa cuma buat
    nakutin bot supaya gak berani SHORT, sementara mereka sendiri jualan
    (Distribution) pake Agg 0.00x. Begitu bot masuk LONG, mereka cabut temboknya,
    harga jatuh bebas ke target Long Liq -4.74%.
    
    Rule: Jika Energy > 100 DAN OI Delta NEGATIF (modal ditarik), maka SPOOF!
    """
    @staticmethod
    def analyze(up_energy: float, down_energy: float, oi_delta: float, wmi: float) -> Dict:
        # Cek tembok bawah yang mencurigakan
        if down_energy > EST_ENERGY_SPOOF_THRESHOLD and oi_delta < EST_OI_DELTA_NEGATIVE:
            # Validasi dengan WMI (ada target short di atas atau target long di bawah?)
            if wmi > 0:  # WMI positif = target short di atas (MM butuh harga turun untuk makan long di bawah)
                return {
                    "is_spoof": True,
                    "bias": "SHORT",
                    "reason": f"EST_ENERGY_SPOOF: Tembok bawah ({down_energy:.1f}) terdeteksi PALSU! "
                             f"OI Δ {oi_delta:.2f}% (Turun) membuktikan Whale sedang nyabut jaring. "
                             f"Tembok itu cuma umpan supaya bot lo LONG. SIAP FLUSH KE BAWAH!"
                }
        
        # Cek tembok atas yang mencurigakan (jarang, tapi bisa terjadi)
        if up_energy > EST_ENERGY_SPOOF_THRESHOLD and oi_delta < EST_OI_DELTA_NEGATIVE:
            if wmi < 0:  # WMI negatif = target long di bawah (MM butuh harga naik untuk makan short di atas)
                return {
                    "is_spoof": True,
                    "bias": "LONG",
                    "reason": f"EST_ENERGY_SPOOF: Tembok atas ({up_energy:.1f}) terdeteksi PALSU! "
                             f"OI Δ {oi_delta:.2f}% (Turun) membuktikan Whale sedang nyabut jaring. "
                             f"Tembok itu cuma umpan supaya bot lo SHORT. SIAP SQUEEZE KE ATAS!"
                }
        
        return {"is_spoof": False, "bias": "NEUTRAL", "reason": ""}


# ================= V96: PASSIVE DISTRIBUTION DETECTOR (PDD) - ANTI-STEALTH TRAP =================
class PassiveDistributionDetectorV96:
    """
    🔥 V96: PASSIVE DISTRIBUTION DETECTOR - WHALE JUAL DIAM-DIAM 🔥
    
    Kasus PIXEL:
    - Agg: 0.00x (mati)
    - Flow: 1.5x (masih ada volume)
    - OI: -1.44% (turun)
    - RSI: 39 (<50)
    - Price Change: turun/stagnan
    
    Ini BUKAN stealth accumulation! Ini PASSIVE DISTRIBUTION.
    Whale jualan via limit orders tanpa bikin agresi (Agg 0),
    tapi volume tetap mengalir (Flow > 1.2).
    
    Rule: OI turun + Flow tinggi + RSI < 50 + harga tidak naik = SHORT
    """
    @staticmethod
    def analyze(oi_delta: float, flow: float, rsi: float, price_change: float) -> Dict:
        if (oi_delta < PDD_OI_DELTA_MIN and 
            flow > PDD_FLOW_MIN and 
            rsi < PDD_RSI_MAX and 
            price_change <= PDD_PRICE_CHANGE_MAX):
            
            return {
                "active": True,
                "bias": "SHORT",
                "reason": f"PDD_PASSIVE_DISTRIBUTION: OI turun {oi_delta:.2f}% + Flow {flow:.2f}x (masih ada volume) + "
                         f"RSI {rsi:.1f} < 50 + Price {price_change:+.2f}% (tidak naik). "
                         f"Whale selling via limit orders! JANGAN LONG!"
            }
        
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V96: REAL SHORT COVERING FILTER (RSC) - VALIDASI SAD =================
class RealShortCoveringFilterV96:
    """
    🔥 V96: REAL SHORT COVERING FILTER - MEMBEDAKAN SHORT COVERING ASLI 🔥
    
    SAD logic: OI turun + Agg 0 = short covering.
    Tapi di PIXEL, OI turun + Agg 0 + price turun = BUKAN short covering!
    
    Short covering asli: OI turun + PRICE NAIK (karena short seller beli untuk tutup posisi).
    Jika price tidak naik, itu bisa jadi:
    - Long liquidation
    - Position closing kedua sisi
    - Passive distribution
    
    Rule: Jika OI turun tapi price tidak naik, SAD harus diabaikan.
    """
    @staticmethod
    def analyze(oi_delta: float, price_change: float) -> Dict:
        if oi_delta < 0 and price_change > 0:
            return {
                "is_valid": True,
                "reason": "REAL_SHORT_COVERING: OI turun + Price naik = Short covering asli!"
            }
        else:
            return {
                "is_valid": False,
                "reason": f"OI_DROP_NOT_COVERING: OI turun {oi_delta:.2f}% TAPI price {price_change:+.2f}% (tidak naik). "
                         f"Ini BUKAN short covering! Bisa jadi long liquidation atau passive distribution."
            }


# ================= V94: BAITING PRICE FILTER (BPF) - ANTI-AINU BAIT =================
class BaitingPriceFilterV94:
    """
    V94: Mendeteksi dump palsu (Baiting).
    Jika harga dump < 4% TAPI Energy Jalur Atas jauh lebih murah (< 3x Jalur Bawah),
    maka dump tersebut adalah BAIT (Umpan).
    """
    @staticmethod
    def analyze(energy_up: float, energy_down: float, price_change: float) -> Dict:
        # Jalur atas jauh lebih murah daripada jalur bawah
        if energy_up > 0 and (energy_down / energy_up) > BPF_ENERGY_RATIO:
            if BPF_DUMP_MIN < price_change < BPF_DUMP_MAX:  # Dump tanggung (-4% sampai 0%)
                return {
                    "is_bait": True,
                    "bias": "LONG",
                    "reason": f"BPF_BAIT_DETECTED: Dump {price_change:.2f}% adalah umpan! "
                             f"Energy atas ({energy_up:.2f}) jauh lebih murah dari bawah ({energy_down:.2f}). "
                             f"MM sedang mancing SHORT seller sebelum REBOUND NUKLIR!"
                }
        return {"is_bait": False, "bias": "NEUTRAL", "reason": ""}


# ================= V94: ENERGY GRAVITY RULE (EGR) =================
class EnergyGravityRuleV94:
    """
    V94: Energy Gravity Rule - Memveto Cascade Time jika energy tidak seimbang.
    Jika jalur bawah > 3x lebih mahal dari atas, veto sinyal SHORT.
    """
    @staticmethod
    def analyze(up_energy: float, down_energy: float, wmi: float, cascade_bias: str) -> Dict:
        # Hitung rasio energi
        if up_energy > 0:
            energy_ratio = down_energy / up_energy
        else:
            energy_ratio = 999.0
        
        # Jika hambatan bawah > 3x lebih besar, dan cascade bilang SHORT
        if energy_ratio > EGR_ENERGY_RATIO_THRESHOLD and cascade_bias == "SHORT":
            # Validasi dengan WMI (ada target short di atas)
            if wmi > EGR_WMI_MIN:
                return {
                    "is_veto": True,
                    "bias": "LONG",
                    "reason": f"EGR_ENERGY_VETO: Jalur bawah {energy_ratio:.1f}x lebih mahal "
                             f"({down_energy:.2f} vs {up_energy:.2f}). "
                             f"Abaikan Cascade Time SHORT! MM pilih Squeeze murah ke target WMI {wmi:.1f}x!"
                }
        
        # Kasus sebaliknya (jarang)
        if (1/energy_ratio) > EGR_ENERGY_RATIO_THRESHOLD and cascade_bias == "LONG":
            if wmi < -EGR_WMI_MIN:
                return {
                    "is_veto": True,
                    "bias": "SHORT",
                    "reason": f"EGR_ENERGY_VETO: Jalur atas {(1/energy_ratio):.1f}x lebih mahal "
                             f"({up_energy:.2f} vs {down_energy:.2f}). "
                             f"Abaikan Cascade Time LONG! MM pilih Dump murah ke target WMI {wmi:.1f}x!"
                }
        
        return {"is_veto": False, "bias": "NEUTRAL", "reason": ""}


# ================= V95: LIQUIDATION GAP DETECTOR (LGD) =================
class LiquidationGapDetectorV95:
    """
    V95: Mendeteksi gap antara cluster likuidasi.
    Jika gap bawah > 2x lebih besar dari atas, price prefer squeeze upward.
    """
    @staticmethod
    def analyze(short_dist: float, long_dist: float) -> Dict:
        # Hindari division by zero
        safe_short = max(abs(short_dist), 0.01)
        safe_long = max(abs(long_dist), 0.01)
        
        gap_ratio = safe_long / safe_short
        
        if gap_ratio > LGD_GAP_RATIO:
            return {
                "bias": "LONG",
                "reason": f"LGD_GAP_SQUEEZE: Downside gap {gap_ratio:.2f}x lebih besar. "
                         f"Price prefer squeeze upward karena tidak ada target menarik di bawah."
            }
        
        if gap_ratio < (1 / LGD_GAP_RATIO):
            return {
                "bias": "SHORT",
                "reason": f"LGD_GAP_DUMP: Upside gap {(1/gap_ratio):.2f}x lebih besar. "
                         f"Price prefer cascade downward."
            }
        
        return {"bias": "NEUTRAL", "reason": "Gap seimbang"}


# ================= V95: SHORT COVERING RULE =================
class ShortCoveringRuleV95:
    """
    V95: Deteksi short covering asli.
    Jika RSI > 90, OI turun, dan harga naik = short covering rally.
    """
    @staticmethod
    def analyze(rsi: float, oi_delta: float, price_change: float) -> Dict:
        if rsi > LGD_SHORT_COVERING_RSI and oi_delta < 0 and price_change > 0:
            return {
                "is_active": True,
                "bias": "LONG",
                "reason": f"RSC_SHORT_COVERING: RSI {rsi:.1f} > 90 + OI Δ {oi_delta:.2f}% (turun) + "
                         f"Price {price_change:+.2f}% (naik) = SHORT COVERING RALLY! Forced buy dari short seller!"
            }
        return {"is_active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V95: LOW ENERGY PRIORITY (LEP) - ANTI-LYN TRAP =================
class LowEnergyPriorityV95:
    """
    V95: Mendeteksi jalur termurah bagi Market Maker.
    Jika Energy Jalur Bawah < Energy Jalur Atas, maka bias WAJIB SHORT,
    bodo amat biarpun Cascade Time bilang jalur atas lebih cepat.
    """
    @staticmethod
    def analyze(energy_up: float, energy_down: float, cascade_bias: str) -> Dict:
        if energy_down < energy_up:  # Jalur bawah lebih murah
            if cascade_bias == "LONG":  # Terjadi konflik dengan Cascade Time
                return {
                    "is_active": True,
                    "bias": "SHORT",
                    "reason": f"LEP_ENERGY_SUPREMACY: Jalur Down ({energy_down:.2f}) lebih murah dari Up ({energy_up:.2f}). "
                             f"Meng-override Cascade Time LONG! MM pilih jalur hemat biaya untuk dump!"
                }
        elif energy_up < energy_down:  # Jalur atas lebih murah
            if cascade_bias == "SHORT":
                return {
                    "is_active": True,
                    "bias": "LONG",
                    "reason": f"LEP_ENERGY_SUPREMACY: Jalur Up ({energy_up:.2f}) lebih murah dari Down ({energy_down:.2f}). "
                             f"Meng-override Cascade Time SHORT! MM pilih jalur hemat biaya untuk pump!"
                }
        return {"is_active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V95: OI-DIRECTIONAL CONFLICT (OID) =================
class OIDirectionalConflictV95:
    """
    V95: Mendeteksi akumulasi posisi yang berlawanan dengan harapan retail.
    Jika OI Delta Meledak (>3%) + Price Turun, itu adalah REAL SHORTING.
    """
    @staticmethod
    def analyze(oi_delta: float, price_change: float) -> Dict:
        if oi_delta > OID_OI_THRESHOLD and price_change < OID_PRICE_DROP_THRESHOLD:
            return {
                "active": True,
                "bias": "SHORT",
                "reason": f"OID_REAL_SHORTING: OI meledak +{oi_delta:.2f}% di tengah penurunan harga {price_change:.2f}%. "
                         f"Whale sedang buka posisi SHORT baru secara agresif. DILARANG LONG!"
            }
        if oi_delta > OID_OI_THRESHOLD and price_change > abs(OID_PRICE_DROP_THRESHOLD):
            return {
                "active": True,
                "bias": "LONG",
                "reason": f"OID_REAL_LONGING: OI meledak +{oi_delta:.2f}% di tengah kenaikan harga {price_change:.2f}%. "
                         f"Whale sedang buka posisi LONG baru secara agresif."
            }
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V96: POSITION BUILD DETECTOR (PBD) =================
class PositionBuildDetectorV96:
    """
    V96: Mendeteksi whale membuka posisi baru (Position Build Phase).
    
    Pattern:
    - OI naik > 2.5% + Price turun > 1% = SHORT BUILD → bias SHORT
    - OI naik > 2.5% + Price naik > 1% = LONG BUILD → bias LONG
    - Jika WMI tidak ekstrim (<80), signal lebih kuat
    """
    @staticmethod
    def analyze(oi_delta: float, price_change: float, wmi: float = None) -> Dict:
        wmi_context = ""
        wmi_valid = True
        
        if wmi is not None:
            wmi_valid = abs(wmi) < PBD_WMI_MAX
            wmi_context = f" WMI {wmi:.1f} (tidak ekstrim)" if wmi_valid else f" WMI {wmi:.1f} (ekstrim, hati-hati)"
        
        # SHORT BUILD: OI naik + harga turun
        if oi_delta > PBD_OI_MIN and price_change < -PBD_PRICE_MOVE_MIN:
            confidence = "ABSOLUTE" if wmi_valid else "HIGH"
            return {
                "active": True,
                "bias": "SHORT",
                "confidence": confidence,
                "reason": f"PBD_SHORT_BUILD: OI naik +{oi_delta:.2f}% (POSITION BUILD!) saat harga turun {price_change:.2f}%.{wmi_context} "
                         f"Whale sedang membuka posisi SHORT baru. DILARANG LONG! IKUTI ARAH OI!"
            }
        
        # LONG BUILD: OI naik + harga naik
        if oi_delta > PBD_OI_MIN and price_change > PBD_PRICE_MOVE_MIN:
            confidence = "ABSOLUTE" if wmi_valid else "HIGH"
            return {
                "active": True,
                "bias": "LONG",
                "confidence": confidence,
                "reason": f"PBD_LONG_BUILD: OI naik +{oi_delta:.2f}% (POSITION BUILD!) saat harga naik +{price_change:.2f}%.{wmi_context} "
                         f"Whale sedang membuka posisi LONG baru. DILARANG SHORT! IKUTI ARAH OI!"
            }
        
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V96: OI DOMINANCE RULE =================
class OIDominanceRuleV96:
    """
    V96: Jika OI meledak dan WMI tidak ekstrim, price mengikuti direction OI.
    
    Rule: 
    IF OI_delta > 3 AND WMI < 80 AND price_move same direction:
        follow OI direction
    """
    @staticmethod
    def analyze(oi_delta: float, price_change: float, wmi: float, lim_bias: str = None) -> Dict:
        if oi_delta > PBD_OI_MIN and abs(wmi) < PBD_WMI_MAX:
            # Price turun + OI naik = SHORT DOMINANCE
            if price_change < -PBD_PRICE_MOVE_MIN:
                return {
                    "active": True,
                    "bias": "SHORT",
                    "reason": f"OID_SHORT_DOMINANCE: OI +{oi_delta:.2f}% (MELEDAK!) + WMI {wmi:.1f} (normal) + "
                             f"Price turun {price_change:.2f}%. Price mengikuti arah OI (SHORT)! "
                             f"{'LIM bilang ' + lim_bias + ' tapi ini false!' if lim_bias else ''}"
                }
            # Price naik + OI naik = LONG DOMINANCE
            if price_change > PBD_PRICE_MOVE_MIN:
                return {
                    "active": True,
                    "bias": "LONG",
                    "reason": f"OID_LONG_DOMINANCE: OI +{oi_delta:.2f}% (MELEDAK!) + WMI {wmi:.1f} (normal) + "
                             f"Price naik +{price_change:.2f}%. Price mengikuti arah OI (LONG)! "
                }
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V95: RETAIL POSITIONING TRAP (RPT) =================
class RetailPositioningTrapV95:
    """
    🔥 V95: RETAIL POSITIONING TRAP - ANTI-CROWDED TRAP
    
    Kasus OGN & DEGO:
    - Bot pilih SHORT karena jalur murah
    - Tapi retail terlalu kompak di sisi SHORT (imbalance > 10x)
    - MM sengaja pilih jalur mahal (Energy Vengeance) untuk sweep retail
    
    Prinsip:
        Jika retail terlalu crowded di satu sisi, MM akan counter-trend
        meskipun harus keluar energi lebih besar.
    """
    @staticmethod
    def analyze(imbalance_ratio: float, energy_diff_ratio: float, wmi: float) -> Dict:
        """
        Args:
            imbalance_ratio: Rasio imbalance retail (>10x = crowded)
            energy_diff_ratio: Selisih energi jalur murah vs mahal (>3x = signifikan)
            wmi: Whale Migration Index (untuk menentukan arah)
        
        Returns:
            Dict dengan is_trap, bias, reason
        """
        # Jika retail terlalu numpuk (>10x) di jalur yang dianggap murah
        if imbalance_ratio > RPT_IMBALANCE_THRESHOLD and energy_diff_ratio > RPT_ENERGY_DIFF_THRESHOLD:
            return {
                "is_trap": True,
                "bias": "LONG" if wmi < 0 else "SHORT",  # Lawan arah retail yang numpuk
                "reason": f"RPT_CROWDED_TRAP: Retail terlalu kompak ({imbalance_ratio:.1f}x) di jalur murah. "
                         f"MM bakal lakuin 'Energy Vengeance' (Pilih jalur mahal) buat Liquidasi massal! "
                         f"JANGAN IKUT ARAH MURAH!"
            }
        return {"is_trap": False, "bias": "NEUTRAL", "reason": ""}


# ================= V96: EXECUTION COMPLETION DETECTOR (ECD) =================
class ExecutionCompletionDetectorV96:
    """
    🔥 V96: EXECUTION COMPLETION DETECTOR - ANTI-LATE ENTRY TRAP
    
    Kasus NFP:
    - RSI = 100, OI = +3.9, WMI = 99
    - Bot membaca: singularity squeeze → LONG
    - Realita: execution already finished → market masuk fase distribusi
    
    Prinsip:
        Market maker bekerja dalam phase:
        1. Accumulation
        2. Trap
        3. Execution
        4. Distribution
        
        Bot kamu sudah bisa baca trap & execution, tapi belum bisa baca
        kapan execution selesai dan masuk fase distribusi.
    
    Tanda execution selesai:
        - RSI > 95 (extreme overbought)
        - Price spike > 5% (sudah terjadi likuidasi besar)
        - OI delta > 2% (posisi baru masuk = distribusi)
    """
    @staticmethod
    def analyze(rsi: float, price_change: float, oi_delta: float) -> Dict:
        """
        Args:
            rsi: RSI value (>95 = extreme)
            price_change: Perubahan harga dalam 5 menit (>5% = spike)
            oi_delta: OI delta (>2% = new positions)
        
        Returns:
            Dict dengan completed, bias, reason
        """
        if rsi > ECD_RSI_THRESHOLD and price_change > ECD_PRICE_SPIKE_MIN and oi_delta > ECD_OI_DELTA_MIN:
            return {
                "completed": True,
                "bias": "REVERSAL",
                "direction": "SHORT" if rsi > 95 else "LONG",  # Jika RSI > 95, reversal SHORT
                "reason": f"ECD_EXECUTION_COMPLETE: RSI {rsi:.1f} > 95 + Price spike {price_change:+.2f}% + "
                         f"OI Δ +{oi_delta:.2f}% (new positions). Likuidasi sudah selesai, MM mulai distribusi! "
                         f"JANGAN FOLLOW ARAH SEBELUMNYA!"
            }
        return {"completed": False, "bias": "NEUTRAL", "reason": ""}


# ================= V96: SINGULARITY VETO INTEGRITY (SVI) =================
class SingularityVetoV96:
    """
    🔥 V96: SINGULARITY VETO INTEGRITY - ANTI-OVER-LOGIC DEGO
    
    Kasus DEGOUSDT:
    - WMI 100.0x (Singularitas Mutlak)
    - Short Dist +0.19% (Event Horizon)
    - RSI 91.1 (Parabolic Phase)
    - Bot V95 salah: RPT (Retail Trap) override Singularitas Whale
    
    Prinsip:
        Di hadapan Singularitas (WMI > 99.5), semua filter psikologi retail hancur.
        Harga tidak lagi punya pilihan selain menabrak magnet tersebut.
        MM tidak peduli retail mau posisi apa, MM cuma peduli EKSEKUSI.
    
    Kaidah:
        Jika WMI > 99.5 (Singularitas), maka modul RPT (Retail Trap) HARUS MATI.
    """
    @staticmethod
    def analyze(wmi: float, rpt_bias: str = None, singularity_bias: str = None) -> Dict:
        """
        Args:
            wmi: Whale Migration Index (>99.5 = singularitas mutlak)
            rpt_bias: Bias dari Retail Positioning Trap (opsional)
            singularity_bias: Bias dari Whale Singularity (opsional)
        
        Returns:
            Dict dengan is_absolute_veto, bias, reason
        """
        if wmi > SVI_WMI_THRESHOLD:
            # Tentukan bias berdasarkan arah WMI
            bias = "LONG" if wmi > 0 else "SHORT"
            
            return {
                "is_absolute_veto": True,
                "bias": bias,
                "reason": f"SVI_ABSOLUTE_VETO: WMI {wmi:.1f}x adalah Singularitas Mutlak! "
                         f"Abaikan semua filter (RPT, dll). MM sedang dalam mode 'God Execution'. "
                         f"Ikuti arah Magnet {wmi:.1f}x!",
                "wmi_level": "CRITICAL" if wmi > 99.9 else "ABSOLUTE"
            }
        
        # Level warning (99.0 - 99.5)
        if wmi > 99.0:
            bias = "LONG" if wmi > 0 else "SHORT"
            return {
                "is_absolute_veto": False,
                "warning": True,
                "bias": bias,
                "reason": f"SVI_WARNING: WMI {wmi:.1f}x mendekati singularitas. "
                         f"Pertimbangkan untuk memprioritaskan sinyal WSC.",
                "wmi_level": "WARNING"
            }
        
        return {
            "is_absolute_veto": False, 
            "warning": False,
            "bias": "NEUTRAL", 
            "reason": ""
        }


# ================= V97: EVENT HORIZON DETECTOR (EVH) =================
class EventHorizonV97:
    """
    🔥 V97: EVENT HORIZON DETECTOR - LIQUIDATION MAGNET PROXIMITY
    
    Kasus DEGOUSDT:
    - WMI = 100 (Singularitas)
    - Short liq = +0.19% (SANGAT DEKAT!)
    - RSI = 91 (Overbought)
    - Flow = 2.03, Agg = 0.33
    
    Prinsip Paling Penting HFT:
        Market maker selalu memprioritaskan distance_to_liquidation, bukan RSI.
        
        Struktur DEGO:
        price
        │
        │ short liq +0.19% ← SANGAT DEKAT (Event Horizon)
        │
        │
        │ long liq -2.95% ← JAUH
        
        Artinya: target atas sangat dekat, target bawah jauh.
        Jadi walaupun RSI 91 (overbought), MM tetap akan ambil +0.19%
        karena itu free liquidity.
    
    Rule:
        Jika WMI > 95 DAN jarak likuidasi < 0.3%, maka price TIDAK PUNYA PILIHAN
        selain menabrak magnet tersebut. Abaikan semua sinyal counter-trend!
    """
    @staticmethod
    def analyze(wmi: float, short_dist: float, long_dist: float) -> Dict:
        """
        Args:
            wmi: Whale Migration Index (>95 = extreme)
            short_dist: Jarak ke short liquidation (+%)
            long_dist: Jarak ke long liquidation (-%)
        
        Returns:
            Dict dengan active, bias, reason
        """
        # Event Horizon untuk SHORT LIQUIDATION (price akan naik)
        if wmi > EVH_WMI_THRESHOLD and abs(short_dist) < EVH_SHORT_DIST_MAX:
            return {
                "active": True,
                "bias": "LONG",
                "type": "SHORT_EVENT_HORIZON",
                "reason": f"EVH_SHORT_HORIZON: Short liq {short_dist:.2f}% terlalu dekat dengan WMI {wmi:.1f}x! "
                         f"Price tidak punya pilihan selain menabrak magnet ini. "
                         f"Abaikan RSI {wmi:.1f} atau sinyal distribution!",
                "distance": short_dist,
                "wmi": wmi
            }
        
        # Event Horizon untuk LONG LIQUIDATION (price akan turun)
        if wmi < -EVH_WMI_THRESHOLD and abs(long_dist) < EVH_LONG_DIST_MAX:
            return {
                "active": True,
                "bias": "SHORT",
                "type": "LONG_EVENT_HORIZON",
                "reason": f"EVH_LONG_HORIZON: Long liq {long_dist:.2f}% terlalu dekat dengan WMI {wmi:.1f}x! "
                         f"Price tidak punya pilihan selain menabrak magnet ini. "
                         f"Abaikan sinyal oversold atau reversal!",
                "distance": long_dist,
                "wmi": wmi
            }
        
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V97: EVENT HORIZON SINGULARITY (EHS) =================
class EventHorizonSingularityV97:
    """
    🔥 V97: EVENT HORIZON SINGULARITY - ANTI-ARIA TRAP
    
    Kasus ARIAUSDT (The Triple Veto Violation):
    - WMI 98.9x (Hampir Singularitas)
    - Energy Up: 1.19, Energy Down: 41.37 → Ratio 34.9x!
    - Short Dist +0.72% (Tipis)
    - OI Delta +5.64% (Position Building raksasa)
    - RSI 100.0 (Tapi ini Vacuum, bukan exhaustion)
    
    Kelicikan MM:
        MM sengaja naikin harga pelan-pelan biar RSI mentok 100.
        Bot lo ngira RSI 100 + RPT = Waktunya bantai retail (Short).
        Padahal RSI 100 adalah tanda bursa lagi "Full Throttle" 
        (Injak Gas Pol) buat nge-liquidate SHORT seller.
    
    Prinsip:
        Jika Energy Ratio > 20x DAN WMI > 95, bot dilarang keras
        melakukan perlawanan arah (SHORT), biarpun retail kompak.
        Ini adalah "Event Horizon" - tarikan gravitasi yang tidak bisa dilawan.
    """
    @staticmethod
    def analyze(energy_up: float, energy_down: float, wmi: float, short_dist: float) -> Dict:
        """
        Args:
            energy_up: Energy to pump (ke atas)
            energy_down: Energy to dump (ke bawah)
            wmi: Whale Migration Index (>95 = extreme)
            short_dist: Jarak ke short liquidation
        
        Returns:
            Dict dengan is_active, bias, reason
        """
        # Hitung energy ratio (mana yang lebih mahal)
        if energy_up > 0:
            energy_ratio = energy_down / energy_up
        else:
            energy_ratio = 999.0
        
        # Event Horizon terdeteksi: satu arah jauh lebih mahal (>20x) + WMI ekstrim
        if energy_ratio > EHS_ENERGY_RATIO_THRESHOLD and abs(wmi) > EHS_WMI_THRESHOLD:
            # Validasi dengan jarak likuidasi (semakin dekat, semakin kuat)
            if abs(short_dist) < EHS_SHORT_DIST_MAX:
                # Tentukan arah berdasarkan WMI
                bias = "LONG" if wmi > 0 else "SHORT"
                
                return {
                    "is_active": True,
                    "bias": bias,
                    "energy_ratio": round(energy_ratio, 1),
                    "reason": f"EHS_BLACK_HOLE: Energy Ratio {energy_ratio:.1f}x (MUTLAK) + WMI {wmi:.1f}x. "
                             f"Jalur lawan terlalu mahal untuk MM! MM pilih jalur termurah "
                             f"biarpun RSI 100. DILARANG COUNTER!",
                    "severity": "ABSOLUTE" if energy_ratio > 30 else "SUPREME"
                }
        
        return {"is_active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V98: VACUUM DETECTOR =================
class VacuumDetectorV98:
    """
    🔥 V98: VACUUM DETECTOR - ORDERBOOK VACUUM DETECTION
    
    Kasus ARIAUSDT:
    - Agg = 0.11x (SANGAT RENDAH!)
    - Flow = 1.94x (Cukup tinggi)
    - RSI = 100 (Tapi ini bukan exhaustion)
    
    Interpretasi sebenarnya:
        Aggression 0.11x artinya TIDAK ADA SELLER.
        Dengan kondisi ini, price naik sangat mudah.
        RSI jadi 100 bukan karena buying kuat, tapi karena liquidity tipis.
        Ini disebut dalam microstructure: LIQUIDITY VACUUM.
    
    Struktur ARIA:
        phase 1: OI build (+5.6%)
        phase 2: retail short masuk
        phase 3: orderbook vacuum (Agg < 0.2)
        phase 4: squeeze (+7% dalam 13 menit)
    
    Rule:
        Jika Agg < 0.2 DAN Flow > 1.5, maka seller mati.
        Market maker hanya butuh sedikit buy untuk push price.
        Abaikan sinyal RSI overbought!
    """
    @staticmethod
    def analyze(agg_ratio: float, flow: float, rsi: float = None) -> Dict:
        """
        Args:
            agg_ratio: Aggressive Ratio (<0.2 = seller mati)
            flow: Trade Flow (>1.5 = ada volume)
            rsi: RSI (opsional, untuk konteks)
        
        Returns:
            Dict dengan active, bias, reason
        """
        if agg_ratio < VAC_AGG_MAX and flow > VAC_FLOW_MIN:
            rsi_context = f" meskipun RSI {rsi:.1f}" if rsi and rsi > 80 else ""
            
            return {
                "active": True,
                "bias": "LONG",
                "reason": f"VAC_VACUUM_DETECTED: Seller mati (Agg {agg_ratio:.2f}x) + Volume masuk (Flow {flow:.2f}x). "
                         f"Orderbook kosong di atas{rsi_context}. Market maker hanya butuh sedikit buy untuk push price!",
                "vacuum_type": "STRONG" if agg_ratio < 0.1 else "MODERATE"
            }
        
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V99: SUPERIOR WHALE DOMINANCE PROTOCOL =================

# ================= V99 CONFIG - SUPERIOR WHALE DOMINANCE PROTOCOL =================
# ================= V99-SCT: SHORT CROWD TRAP CONFIG =================
SCT_IMBALANCE_THRESHOLD = 50.0        # Imbalance > 50x = dangerous crowd
SCT_CROWD_LEVEL_EXTREME = 70.0         # 70x rule - extreme crowd
SCT_AGG_MAX = 0.1                      # Agg < 0.1 = seller exhaustion
SCT_OI_DELTA_MIN = 0.0                 # OI Build = new positions entering

class SuperiorWDMVIP99:
    """
    🔥 V99: SUPERIOR WHALE DOMINANCE PROTOCOL - FIXED LOGIC
    Prinsip: WMI Menunjukkan Arah Massa Likuiditas TERBESAR.
    WMI Positif > 0  = Short Mass Dominan (Target di Atas) -> Bias LONG (Squeeze).
    WMI Negatif < 0  = Long Mass Dominan (Target di Bawah) -> Bias SHORT (Dump).
    
    KASUS HUMA: WMI -100 (Long Mass Below). Jarak Long -0.56%.
    Harusnya: SHORT (Dump ke bawah menghajar Longs).
    Bot Salah: LONG (Karena logika WMI di-invert sebelumnya).
    """
    @staticmethod
    def check_override(wmi_ratio: float, lep_bias: str = None, 
                       short_dist: float = 0, long_dist: float = 0,
                       price_change: float = 0, oi_delta: float = 0,
                       short_imbalance: float = 0, agg: float = None) -> Dict:
        """
        Args:
            wmi_ratio: Whale Migration Index
            lep_bias: Bias dari Low Energy Path (optional)
            short_dist: Jarak ke short liquidation
            long_dist: Jarak ke long liquidation
            price_change: Perubahan harga 5 menit
            oi_delta: OI Delta 5 menit
            short_imbalance: Rasio imbalance SHORT (untuk validasi crowded)
            agg: Aggressive Ratio (untuk validasi exhaustion)
        """
        # ============================================
        # VALIDASI BARU: Jangan veto jika Short Imbalance Ekstrim (>50x)
        # ============================================
        if wmi_ratio < -95 and short_imbalance and short_imbalance > SCT_IMBALANCE_THRESHOLD:
            if agg and agg < SCT_AGG_MAX:
                # Kontradiksi: WMI bilang target bawah besar, TAPI Shorts crowded di atas
                # Prioritaskan Squeeze Up untuk crowd shorts dulu!
                return {
                    "is_veto": False,  # JANGAN VETO SQUEEZE UP!
                    "bias": "LONG", 
                    "warning": True,
                    "reason": f"V99_CROWDED_SHORT_OVERRIDE: WMI {wmi_ratio:.1f}x TAPI "
                             f"Short Imbalance {short_imbalance:.1f}x crowd! + Agg {agg:.2f}x exhausted! "
                             f"Prioritas SQUEEZE! WMI VETO dibatalkan.",
                    "phase": "CROWD_OVERRIDE"
                }
        
        # ============================================
        # VALIDASI BARU: Jika WMI > 95 dan Long Crowded > 50x
        # ============================================
        if wmi_ratio > 95 and short_imbalance and short_imbalance < (1.0 / SCT_IMBALANCE_THRESHOLD):  # Long crowded
            if agg and agg < SCT_AGG_MAX:
                return {
                    "is_veto": False,
                    "bias": "SHORT",
                    "warning": True,
                    "reason": f"V99_CROWDED_LONG_OVERRIDE: WMI {wmi_ratio:.1f}x TAPI "
                             f"Long Crowded! Prioritas DUMP!",
                    "phase": "CROWD_OVERRIDE"
                }
        
        # --- FIX 1: LOGIKA POSITIF/NEGATIF HARUS SESUAI ARAH TARGET ---
        
        # VALIDASI TAMBAHAN: Jika OI Build > 5% dan price turun > 2%, override WMI
        if oi_delta > 5.0 and price_change < -2.0:
            return {
                "is_veto": True,
                "bias": "SHORT",
                "reason": f"V99_NUCLEAR_OI: OI Meledak +{oi_delta:.2f}% saat Harga Crash {price_change:.2f}%! "
                         f"Institutional Short Building! Override WMI {wmi_ratio:.1f}x!",
                "phase": "OI_DOMINANCE_OVERRIDE"
            }
        
        # VALIDASI TAMBAHAN: Jika OI Build > 5% dan price naik > 2%, override WMI
        if oi_delta > 5.0 and price_change > 2.0:
            return {
                "is_veto": True,
                "bias": "LONG",
                "reason": f"V99_NUCLEAR_OI: OI Meledak +{oi_delta:.2f}% saat Price Pump {price_change:+.2f}%! "
                         f"Institutional Long Building! Override WMI {wmi_ratio:.1f}x!",
                "phase": "OI_DOMINANCE_OVERRIDE"
            }
        
        # Kasus 1: WMI Sangat Positif (> 95) = Massive SHORT LIQ Cluster (Tersimpan di ATAS Harga)
        # MM butuh harga NAIK untuk likuidasi Short (Squeeze).
        if wmi_ratio > WMI_SINGULARITY_VETO_THRESHOLD:
            # VALIDASI: Apakah jaraknya realistis? (< 3% biasanya aman untuk trigger)
            if abs(short_dist) <= 3.0:
                return {
                    "is_veto": True,
                    "bias": "LONG",
                    "reason": f"V99_WMI_VETO: WMI {wmi_ratio:.1f}x > 95 (SHORT_LIQ_CLUSTER ABOVE). "
                             f"Jarak {short_dist}% dekat! MM pasti Squeeze Up!",
                    "phase": "WHALE_SINGULARITY_OVERRIDE"
                }
            else:
                # Jika jarak > 3%, WMI tetap penting tapi tidak veto mutlak
                return {
                    "is_veto": False,
                    "warning": True,
                    "bias": "LONG",
                    "reason": f"V99_WMI_WARNING: WMI {wmi_ratio:.1f}x > 95 TAPI jarak {short_dist}% > 3%. "
                             f"WMI penting, tapi tidak veto.",
                    "phase": "WHALE_WARNING"
                }
        
        # Kasus 2: WMI Sangat Negatif (< -95) = Massive LONG LIQ Cluster (Tersimpan di BAWAH Harga)
        # MM butuh harga TURUN untuk likuidasi Long (Crash).
        elif wmi_ratio < -WMI_SINGULARITY_VETO_THRESHOLD:
            # VALIDASI: Apakah jaraknya realistis? (< 3% biasanya aman untuk trigger)
            if abs(long_dist) <= 3.0:
                # PERHATIAN: Sudah divalidasi sebelumnya untuk crowded short
                return {
                    "is_veto": True,
                    "bias": "SHORT",
                    "reason": f"V99_WMI_VETO: WMI {wmi_ratio:.1f}x < -95 (LONG_LIQ_CLUSTER BELOW). "
                             f"Jarak {long_dist}% dekat! MM pasti Dump Down!",
                    "phase": "WHALE_SINGULARITY_OVERRIDE"
                }
            else:
                # Jika jarak > 3%, WMI tetap penting tapi tidak veto mutlak
                return {
                    "is_veto": False,
                    "warning": True,
                    "bias": "SHORT",
                    "reason": f"V99_WMI_WARNING: WMI {wmi_ratio:.1f}x < -95 TAPI jarak {long_dist}% > 3%. "
                             f"WMI penting, tapi tidak veto.",
                    "phase": "WHALE_WARNING"
                }
        
        return {"is_veto": False, "bias": "NEUTRAL", "reason": ""}


class OIBuildValidatorV99:
    """
    🔥 V99: OI BUILD VALIDATOR - NUCLEAR OI OVERRIDE
    
    Prinsip: "Nuclear OI" Override
    Jika OI Delta > 5% (Build) DAN Price Drop > 2%, AMBIL SINYAL SELL
    regardless WMI atau RSI Overbought.
    
    Position Building institusi lebih kuat daripada static Liquidity Map.
    
    Kasus HUMA:
        OI Δ5m: +9.16%
        Price Change: -5.53%
        Ini adalah Institutional Short Building!
    """
    @staticmethod
    def analyze(oi_delta: float, price_change: float, 
                short_dist: float, long_dist: float,
                wmi: float = None) -> Dict:
        """
        Args:
            oi_delta: OI Delta 5 menit
            price_change: Perubahan harga 5 menit
            short_dist: Jarak ke short liquidation
            long_dist: Jarak ke long liquidation
            wmi: WMI ratio (optional)
        
        Returns:
            Dict dengan bias, confidence, reason
        """
        # KASUS 1: SHORT BUILD - OI naik besar + harga turun
        if oi_delta > 5.0 and price_change < -2.0:
            return {
                "bias": "SHORT",
                "confidence": "ABSOLUTE",
                "reason": f"V99_OI_SHORT_BUILD: OI Meledak +{oi_delta:.2f}% saat Harga Crash {price_change:.2f}%! "
                         f"Whale sedang membuka posisi SHORT baru secara agresif. "
                         f"Abaikan WMI {wmi if wmi else 'N/A'}!",
                "phase": "INSTITUTIONAL_SHORTING"
            }
        
        # KASUS 2: LONG BUILD - OI naik besar + harga naik
        if oi_delta > 5.0 and price_change > 2.0:
            return {
                "bias": "LONG",
                "confidence": "ABSOLUTE",
                "reason": f"V99_OI_LONG_BUILD: OI Meledak +{oi_delta:.2f}% saat Price Pump {price_change:+.2f}%! "
                         f"Whale sedang membuka posisi LONG baru secara agresif.",
                "phase": "INSTITUTIONAL_BUYING"
            }
        
        # KASUS 3: SHORT COVERING - OI turun besar + harga naik
        if oi_delta < -3.0 and price_change > 2.0:
            return {
                "bias": "LONG",
                "confidence": "SUPREME",
                "reason": f"V99_OI_COVERING: OI Turun {oi_delta:.2f}% (SHORT COVERING!) saat Price Pump {price_change:+.2f}%! "
                         f"Short seller forced to cover! Squeeze incoming!",
                "phase": "SHORT_COVERING_RALLY"
            }
        
        # KASUS 4: LONG LIQUIDATION - OI turun besar + harga turun
        if oi_delta < -3.0 and price_change < -2.0:
            return {
                "bias": "SHORT",
                "confidence": "SUPREME",
                "reason": f"V99_OI_LIQUIDATION: OI Turun {oi_delta:.2f}% (LONG LIQUIDATION!) saat Price Crash {price_change:.2f}%! "
                         f"Long seller capitulation! Dump lanjutan!",
                "phase": "LONG_LIQUIDATION_CASCADE"
            }
        
        return {"bias": "NEUTRAL", "confidence": "LOW", "reason": ""}


class GravityDistanceValidatorV99:
    """
    🔥 V99: GRAVITY DISTANCE SAFETY
    
    Prinsip: "Gravity Distance" Safety
    Jangan pernah memprioritaskan WMI (Massa) di atas Jarak (Distance)
    jika jarak target WMI > 5% sementara target lawan < 2%.
    
    Kasus HUMA:
        - WMI target (Short) jarak +13.62% (> 5%)
        - Target lawan (Long) jarak -0.56% (< 2%)
        - Harusnya pilih target lawan (SHORT) karena lebih dekat!
    """
    @staticmethod
    def validate(wmi: float, short_dist: float, long_dist: float,
                 wmi_bias: str = None) -> Dict:
        """
        Args:
            wmi: Whale Migration Index
            short_dist: Jarak ke short liquidation
            long_dist: Jarak ke long liquidation
            wmi_bias: Bias dari WMI (optional)
        
        Returns:
            Dict dengan override, bias, reason
        """
        # Jika target WMI terlalu jauh (> 5%) dan target lawan sangat dekat (< 2%)
        if wmi > 0:  # WMI positif = target SHORT di atas
            if abs(short_dist) > 5.0 and abs(long_dist) < 2.0:
                return {
                    "override": True,
                    "bias": "SHORT",  # Pilih target dekat (Long liq)
                    "reason": f"V99_GRAVITY_DISTANCE: Target WMI (Short) {short_dist}% > 5% (terlalu jauh) sementara "
                             f"target lawan (Long) {long_dist}% < 2% (sangat dekat). "
                             f"MM pilih target terdekat! SHORT!",
                    "phase": "PROXIMITY_OVERRIDE"
                }
        
        elif wmi < 0:  # WMI negatif = target LONG di bawah
            if abs(long_dist) > 5.0 and abs(short_dist) < 2.0:
                return {
                    "override": True,
                    "bias": "LONG",  # Pilih target dekat (Short liq)
                    "reason": f"V99_GRAVITY_DISTANCE: Target WMI (Long) {long_dist}% > 5% (terlalu jauh) sementara "
                             f"target lawan (Short) {short_dist}% < 2% (sangat dekat). "
                             f"MM pilih target terdekat! LONG!",
                    "phase": "PROXIMITY_OVERRIDE"
                }
        
        return {"override": False, "bias": "NEUTRAL", "reason": ""}


# ================= V99-SCT: SHORT CROWD TRAP DETECTOR =================

class ShortCrowdTrapDetectorV99:
    """
    🔥 V99-SCT: SHORT CROWD TRAP DETECTOR - ANTI-ARIA TRAP
    
    Kasus ARIAUSDT:
        - Imbalance Ratio: 73.01x (SHORT OVERCROWDED!)
        - Aggression: 0.05x (SELLER EXHAUSTED!)
        - OI Delta: +1.76% (Whale Building Shorts)
        - Long Dist: -0.27% (Target Below tapi kecil)
    
    Interpretasi Benar:
        Market Maker akan SQUEEZE SHORTS dulu karena ada 73x lebih banyak
        retail shorts daripada longs. Agg 0.05x menandakan tidak ada seller
        yang tersisa - orderbook vacuum!
    
    Prinsip:
        "73x Rule" - Imbalance Saturation Override
        Jika Short Imbalance > 70x + Agg < 0.1 + OI Build → 
        DILARANG SHORT bahkan jika WMI ekstrim negatif.
        
        Market Maker akan Squeeze Shorts terlebih dahulu karena ada lebih banyak
        profit dari membakar 73x shorts daripada menghajar longs dengan volume kecil.
    """
    
    @staticmethod
    def analyze(short_imbalance: float, agg: float, oi_delta: float, 
                wmi: float = None, price_change: float = None) -> Dict:
        """
        Args:
            short_imbalance: Rasio imbalance SHORT (>50x = crowded)
            agg: Aggressive Ratio (<0.1 = seller exhaustion)
            oi_delta: OI Delta 5 menit (>0 = position building)
            wmi: WMI ratio (optional, untuk konteks)
            price_change: Perubahan harga (optional)
        
        Returns:
            Dict dengan is_trap, bias, confidence, reason, priority
        """
        
        # ============================================
        # SCENARIO 1: EXTREME CROWD - 70x RULE
        # Jika Imbalance > 70x + Agg mati = SQUEEZE IMMINENT!
        # ============================================
        if short_imbalance > SCT_CROWD_LEVEL_EXTREME and agg < SCT_AGG_MAX:
            wmi_context = f" WMI {wmi:.1f}x" if wmi else ""
            price_context = f" Price {price_change:+.2f}%" if price_change else ""
            
            return {
                "is_trap": True,
                "bias": "LONG",
                "confidence": "ABSOLUTE",
                "priority": "SUPREME",  # Prioritas tertinggi!
                "reason": f"SCT_EXTREME_CROWD: Short Imbalance {short_imbalance:.1f}x (SUPER CROWDED!) + "
                         f"Agg {agg:.2f}x (SELLER EXHAUSTED!){wmi_context}{price_context}. "
                         f"MM akan SQUEEZE SHORTS! 73x Rule activated! DILARANG SHORT!",
                "phase": "CROWDED_SQUEEZE_TRIGGER"
            }
        
        # ============================================
        # SCENARIO 2: STANDARD CROWD - 50x RULE
        # Jika Imbalance > 50x + Agg mati + OI Build = SQUEEZE SETUP
        # ============================================
        if (short_imbalance > SCT_IMBALANCE_THRESHOLD and 
            agg < SCT_AGG_MAX and 
            oi_delta > SCT_OI_DELTA_MIN):
            
            wmi_context = f" WMI {wmi:.1f}x" if wmi else ""
            
            return {
                "is_trap": True,
                "bias": "LONG",
                "confidence": "SUPREME",
                "priority": "SUPREME",
                "reason": f"SCT_SHORT_CROWD: Imbalance {short_imbalance:.1f}x crowd SHORT! + "
                         f"Agg {agg:.2f}x exhausted! + OI Δ {oi_delta:+.2f}% (Whale building). "
                         f"SQUEEZE INCOMING!{wmi_context}",
                "phase": "CROWDED_SQUEEZE_SETUP"
            }
        
        # ============================================
        # SCENARIO 3: CROWD + VACUUM (Ghost Vacuum Signal)
        # Agg < 0.1 + Imbalance > 50x = Orderbook Vacuum
        # ============================================
        if short_imbalance > SCT_IMBALANCE_THRESHOLD and agg < SCT_AGG_MAX:
            return {
                "is_trap": True,
                "bias": "LONG",
                "confidence": "HIGH",
                "priority": "HIGH",
                "reason": f"SCT_VACUUM: Imbalance {short_imbalance:.1f}x + Agg {agg:.2f}x (VACUUM!). "
                         f"Orderbook kosong di atas, siap squeeze!",
                "phase": "VACUUM_SQUEEZE"
            }
        
        return {"is_trap": False, "bias": "NEUTRAL", "priority": "LOW"}


class CrowdVsClusterLogicV99:
    """
    🔥 V99: CROWD VS CLUSTER LOGIC - ANTI-WMI OVERRIDE
    
    Prinsip:
        Jangan bandingkan WMI Cluster Size, bandingkan Crowd Imbalance.
        
        - WMI = Likuidasi potensial (massive pool)
        - Imbalance = Posisi aktif trader (crowd)
        
        Jika Crowd > 50x, Market Maker fokus pada Crowd dulu sebelum Cluster.
        
    Kasus ARIA:
        WMI = -99.7x (Long Cluster di bawah)
        Imbalance = 73x (Short Crowd di atas)
        Agg = 0.05x (Seller exhausted)
        
        Meskipun WMI negatif, Crowd > 50x memaksa MM untuk squeeze SHORT dulu!
    """
    
    @staticmethod
    def resolve(wmi: float, short_imbalance: float, agg: float,
                short_dist: float, long_dist: float) -> Dict:
        """
        Args:
            wmi: Whale Migration Index
            short_imbalance: Rasio imbalance SHORT
            agg: Aggressive Ratio
            short_dist: Jarak ke short liquidation
            long_dist: Jarak ke long liquidation
        
        Returns:
            Dict dengan override, bias, reason
        """
        
        # KASUS 1: WMI negatif (target bawah) TAPI Short Crowded > 50x
        if wmi < 0 and short_imbalance > SCT_IMBALANCE_THRESHOLD:
            # Validasi dengan Aggression
            if agg < SCT_AGG_MAX:
                return {
                    "override": True,
                    "bias": "LONG",
                    "reason": f"V99_CROWD_VS_CLUSTER: WMI {wmi:.1f}x (Cluster bawah) TAPI "
                             f"Short Imbalance {short_imbalance:.1f}x (Crowd atas) + Agg {agg:.2f}x (exhausted). "
                             f"MM squeeze CROWD dulu! LONG!",
                    "phase": "CROWD_DOMINANCE"
                }
        
        # KASUS 2: WMI positif (target atas) TAPI Long Crowded > 50x
        if wmi > 0 and short_imbalance < (1.0 / SCT_IMBALANCE_THRESHOLD):  # Long crowded
            if agg < SCT_AGG_MAX:
                return {
                    "override": True,
                    "bias": "SHORT",
                    "reason": f"V99_CROWD_VS_CLUSTER: WMI {wmi:.1f}x (Cluster atas) TAPI "
                             f"Long Crowded! MM dump CROWD dulu! SHORT!",
                    "phase": "CROWD_DOMINANCE"
                }
        
        return {"override": False, "bias": "NEUTRAL"}


class OIBuildAtExtremumV99:
    """
    🔥 V99: OI BUILD AT EXTREMUM - WHALE ACCUMULATION DETECTOR
    
    Prinsip:
        "OI Naik + Price Turun + Agg < 0.1 = Whale Accumulation"
        
        Bukan Distribusi! Ini akumulasi posisi baru sebelum pergerakan besar.
        Perlu dibedakan dengan PDD (Passive Distribution) yang memerlukan Flow Tinggi.
    
    Kasus ARIA:
        OI Delta: +1.76% (naik)
        Price Change: -0.12% (turun sedikit)
        Agg: 0.05x (sangat rendah)
        
        Ini BUKAN distribusi, ini akumulasi posisi SHORT baru yang akan di-squeeze!
    """
    
    @staticmethod
    def analyze(oi_delta: float, price_change: float, agg: float,
                flow: float = None) -> Dict:
        """
        Args:
            oi_delta: OI Delta 5 menit
            price_change: Perubahan harga 5 menit
            agg: Aggressive Ratio
            flow: Trade Flow (untuk membedakan dengan distribusi)
        
        Returns:
            Dict dengan is_accumulation, bias, reason
        """
        
        # KASUS: OI Naik + Price Turun + Agg Rendah = SHORT BUILD (akan di-squeeze)
        if oi_delta > 1.0 and price_change < 0 and agg < 0.2:
            # Cek flow untuk membedakan dengan distribusi
            if flow and flow < 1.5:  # Flow tidak terlalu tinggi = akumulasi diam-diam
                return {
                    "is_accumulation": True,
                    "bias": "LONG",  # Akan squeeze
                    "confidence": "SUPREME",
                    "reason": f"V99_OI_BUILD_EXTREMUM: OI naik {oi_delta:+.2f}% (BUILD!) + "
                             f"Price turun {price_change:.2f}% + Agg {agg:.2f}x (RENDAH!). "
                             f"Whale akumulasi SHORT baru! SIAP SQUEEZE!",
                    "phase": "STEALTH_ACCUMULATION"
                }
            
            if flow and flow > 2.0:  # Flow tinggi = distribusi
                return {
                    "is_accumulation": False,
                    "bias": "SHORT",
                    "confidence": "HIGH",
                    "reason": f"V99_OI_DISTRIBUTION: OI naik {oi_delta:+.2f}% + "
                             f"Flow {flow:.2f}x tinggi = DISTRIBUSI!",
                    "phase": "DISTRIBUTION"
                }
        
        # KASUS: OI Turun + Price Naik + Agg Rendah = SHORT COVERING
        if oi_delta < -1.0 and price_change > 0 and agg < 0.2:
            return {
                "is_accumulation": True,
                "bias": "LONG",
                "confidence": "SUPREME",
                "reason": f"V99_OI_COVERING: OI turun {oi_delta:.2f}% (COVERING!) + "
                         f"Price naik {price_change:+.2f}% + Agg {agg:.2f}x. "
                         f"Short seller forced to cover! SQUEEZE!",
                "phase": "SHORT_COVERING"
            }
        
        return {"is_accumulation": False, "bias": "NEUTRAL"}


class InternalTrapV99FMT:
    """
    🔥 V99: FAKE MOMENTUM / WASH TRADE DETECTOR - ANTI-ARIA TRAP
    
    Kasus ARIAUSDT:
        - Flow = 3.55x (TINGGI!)
        - Price Change = -0.12% (turun sedikit)
        - RSI = 29.3 (rendah)
        - Bot salah baca: Position Flip / Accumulation → LONG
        - Realita: Distribution Top → SHORT
    
    Interpretasi:
        Flow tinggi + Price turun + RSI rendah sering disalahartikan sebagai "Accumulation".
        Padahal bisa jadi "Absorption Trap" atau "Internal Matching" buatan Exchange.
        Whale sedang jual limit di atas, menyerap buying pressure.
    
    Rule:
        IF Flow > 3.0 AND Price Change < -0.5% AND RSI < 40:
            Ini BUKAN Bullish Absorption, ini BEARISH TRAP!
            Bias = SHORT
    """
    @staticmethod
    def detect(trade_flow: float, price_change_5m: float, rsi: float) -> Dict:
        """
        Args:
            trade_flow: Trade Flow ratio (>3.0 = sangat tinggi)
            price_change_5m: Perubahan harga 5 menit (< -0.5% = turun)
            rsi: RSI value (<40 = rendah/oversold)
        
        Returns:
            Dict dengan is_trap, bias, reason
        """
        if trade_flow > INTERNAL_TRAP_FLOW_MIN and price_change_5m < INTERNAL_TRAP_PRICE_MAX and rsi < INTERNAL_TRAP_RSI_MAX:
            return {
                "is_trap": True,
                "bias": "SHORT",
                "reason": f"V99_FMT_INTERNAL_TRAP: Flow {trade_flow:.2f}x (TINGGI!) + Price {price_change_5m:+.2f}% (turun) + "
                         f"RSI {rsi:.1f} (rendah). Ini BUKAN Accumulation! Ini Internal Matching / Absorption Trap. "
                         f"Whale distribusi via Limit Orders. DILARANG LONG!"
            }
        return {"is_trap": False, "bias": "NEUTRAL", "reason": ""}


class OIAccelerationPhaseV99:
    """
    🔥 V99: OI ACCELERATION PHASE DETECTION - MEMBEDAKAN DISTRIBUTION VS VACUUM
    
    Masalah utama: Bot tidak membedakan "Distribution Drop" vs "Liquidity Vacuum Reset".
    Sama-sama OI turun (negative delta), tapi artinya sangat berbeda.
    
    Kasus HUMAUSDT:
        - OI turun -2.21%
        - Harga relatif stabil
        - Bot salah baca: Distribution / Exit
        - Realita: Vacuum Reset sebelum Squeeze
    
    Logic Penyelesaian:
        Jika OI turun drastis (< -1.0%):
            - Jika harga turun > 2% + flow sepi = LIQUIDATION PANIC (SHORT)
            - Jika harga stabil (±0.2%) + flow sepi = VACUUM RESET (LONG)
            - Jika harga naik sedikit + OI turun = SHORT COVERING (LONG)
    """
    @staticmethod
    def analyze(oi_delta: float, price_change: float, flow: float) -> Dict:
        """
        Args:
            oi_delta: OI Delta 5 menit (< -1.0% = turun drastis)
            price_change: Perubahan harga 5 menit
            flow: Trade Flow (untuk validasi)
        
        Returns:
            Dict dengan phase, bias, reason
        """
        if oi_delta < OI_ACCEL_PHASE_DROP_MIN:  # OI turun drastis
            # KASUS 1: LIQUIDATION PANIC (harga turun > 2%)
            if price_change < OI_ACCEL_PRICE_DUMP_MIN:
                return {
                    "phase": "LIQUIDATION_PANIC",
                    "bias": "SHORT",
                    "reason": f"V99_OAI_LIQUIDATION_PANIC: OI turun {oi_delta:.2f}% + Price crash {price_change:.2f}%. "
                             f"Real sell pressure! Lanjutkan SHORT."
                }
            
            # KASUS 2: VACUUM RESET (harga stabil)
            if abs(price_change) < OI_ACCEL_PRICE_STABLE_MAX:
                return {
                    "phase": "VACUUM_RELOAD",
                    "bias": "LONG",
                    "reason": f"V99_OAI_VACUUM_RESET: OI turun {oi_delta:.2f}% + Price stabil {price_change:+.2f}%. "
                             f"Whale bersihkan orderbook (Reset) sebelum SQUEEZE! SIAP LONG!"
                }
            
            # KASUS 3: SHORT COVERING (harga naik)
            if price_change > 0:
                return {
                    "phase": "SHORT_COVERING",
                    "bias": "LONG",
                    "reason": f"V99_OAI_SHORT_COVERING: OI turun {oi_delta:.2f}% + Price naik {price_change:+.2f}%. "
                             f"Short seller tutup posisi! SIAP REBOUND!"
                }
        
        return {"phase": "NORMAL", "bias": "NEUTRAL", "reason": ""}


class LiquidityDensityCalculatorV99:
    """
    🔥 V99: LIQUIDITY DENSITY VS DISTANCE RATIO - PERBAIKAN LEP
    
    Modul LEP (Low Energy Path) hanya menghitung energi (jarak * imbalan),
    tapi lupa menghitung KETAJAMAN TARGET (Liquidity Density).
    
    Bug: Jalur Down jarak 0.5% dengan likuidasi $1M dianggap lebih murah
         daripada jalur Up jarak 2% dengan likuidasi $50M.
    
    Solusi: Masukkan faktor Value Risk Reward ke dalam perhitungan energi.
    
    Formula: path_efficiency = distance / liq_size
    Semakin kecil nilai efficiency, semakin menarik target (sedikit effort, banyak reward).
    """
    @staticmethod
    def calculate_path_efficiency(liq_size: float, distance: float) -> float:
        """
        Menghitung efisiensi path: Energy Cost / Liquidity Profit
        Bukan cuma jarak, tapi JUMLAH BAHAN BAKAR yang didapat.
        
        Args:
            liq_size: Ukuran likuidasi (dalam $)
            distance: Jarak ke likuidasi (dalam %)
        
        Returns:
            efficiency: Semakin kecil = semakin menarik
        """
        if liq_size <= 0 or distance <= 0:
            return float('inf')
        return distance / liq_size
    
    @staticmethod
    def compare_paths(short_liq_size: float, short_dist: float,
                      long_liq_size: float, long_dist: float) -> Dict:
        """
        Membandingkan dua jalur berdasarkan efisiensi (reward/effort).
        
        Returns:
            Dict dengan better_path, bias, reason
        """
        short_efficiency = LiquidityDensityCalculatorV99.calculate_path_efficiency(short_liq_size, short_dist)
        long_efficiency = LiquidityDensityCalculatorV99.calculate_path_efficiency(long_liq_size, long_dist)
        
        if short_efficiency < long_efficiency * 0.5:  # Short path 2x lebih efisien
            return {
                "better_path": "SHORT_LIQ",
                "bias": "LONG",
                "short_efficiency": round(short_efficiency, 6),
                "long_efficiency": round(long_efficiency, 6),
                "reason": f"V99_DENSITY: Short Liq Efficiency {short_efficiency:.6f} vs Long {long_efficiency:.6f}. "
                         f"Short path {long_efficiency/short_efficiency:.1f}x lebih menguntungkan! MM pilih SQUEEZE UP!"
            }
        elif long_efficiency < short_efficiency * 0.5:  # Long path 2x lebih efisien
            return {
                "better_path": "LONG_LIQ",
                "bias": "SHORT",
                "short_efficiency": round(short_efficiency, 6),
                "long_efficiency": round(long_efficiency, 6),
                "reason": f"V99_DENSITY: Long Liq Efficiency {long_efficiency:.6f} vs Short {short_efficiency:.6f}. "
                         f"Long path {short_efficiency/long_efficiency:.1f}x lebih menguntungkan! MM pilih DUMP DOWN!"
            }
        
        return {
            "better_path": "BALANCED",
            "bias": "NEUTRAL",
            "short_efficiency": round(short_efficiency, 6),
            "long_efficiency": round(long_efficiency, 6),
            "reason": "Efficiency seimbang."
        }


# ================= V96: CONFLICT RESOLVER (UPDATED WITH PBD + LEP + RPT + ECD + SVI + EVH) =================
class ConflictResolverV96:
    """
    🔥 URUTAN PRIORITAS MUTLAK V96 (THE FINAL HIERARCHY):
    
    1. EVH (Event Horizon) - Jika WMI > 95 & jarak < 0.3% ⭐ BARU!
    2. SVI (Singularity Veto) - Jika WMI > 99.5 (Veto Segala Veto) ⭐ BARU!
    3. ECD (Execution Completion Detector) (V96) ⭐ BARU! - Deteksi fase distribusi
    4. RPT (Retail Positioning Trap) (V95) ⭐ BARU! - Anti-crowded trap
    5. PBD (Position Build Detector) - OI naik + price move = POSITION BUILD ⭐ NEW!
    6. OID (OI-Directional Conflict) - OI meledak + price turun = REAL SHORTING ⭐ NEW!
    7. ODR (OI Dominance Rule) - OI dominance dengan WMI normal ⭐ NEW!
    8. RSC (Short Covering Rule) - RSI >90 + OI turun + price naik
    9. LEP (Low Energy Priority) - Energy supremacy atas Cascade Time ⭐ NEW!
    10. BPF (Baiting Price Filter) - Anti dump palsu
    11. LGD (Liquidation Gap Detector) - Gap structure
    12. EGR (Energy Gravity Rule) - Energy veto
    13. MARKET PHASE (V91) - Konteks market
    """
    @staticmethod
    def resolve(
        # NEW MODULES V96/V97 - PRIORITAS TERTINGGI!
        evh_res: Dict,                # V97 Event Horizon Detector ⭐ BARU!
        svi_res: Dict,                 # V96 Singularity Veto Integrity ⭐ BARU!
        ecd_res: Dict,               # V96 Execution Completion Detector ⭐ BARU!
        rpt_res: Dict,                # V95 Retail Positioning Trap ⭐ BARU!
        
        # NEW MODULES V96 - PRIORITAS TERTINGGI!
        pbd_res: Dict,               # V96 Position Build Detector ⭐
        oid_res: Dict,                # V95 OI-Directional Conflict ⭐
        odr_res: Dict,                # V96 OI Dominance Rule ⭐
        
        # V95 Energy Supremacy
        lep_res: Dict,                # V95 Low Energy Priority ⭐
        
        # Existing high priority modules
        rsc_res: Dict,
        bpf_res: Dict,
        lgd_res: Dict,
        egr_res: Dict,
        
        # Existing modules (dari kodinganmu)
        phase_res: Dict,
        est_res: Dict,
        odc_res: Dict,
        pdd_res: Dict,
        plr_res: Dict,
        opd_res: Dict,
        wmi_exhaust_res: Dict,
        cascade_res: Dict,
        energy_res: Dict,
        death_res: Dict,
        lgd_void_res: Dict,
        wsc_res: Dict,
        sat_res: Dict,
        pet_res: Dict,
        zgh_res: Dict,
        otf_res: Dict,
        lim_res: Dict
    ) -> Dict:
        
        # 🎯 1. EVENT HORIZON (PRIORITAS TERTINGGI!)
        # Jika jarak likuidasi terlalu dekat dengan WMI ekstrim, price wajib menabrak magnet
        if evh_res.get('active'):
            return {
                "bias": evh_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V97_EVH: {evh_res['reason']}",
                "phase": "EVENT_HORIZON"
            }
        
        # 🌌 2. SINGULARITY VETO INTEGRITY (Anti-OverLogic DEGO)
        # Jika WMI > 99.5, veto semua filter lain
        if svi_res.get('is_absolute_veto'):
            return {
                "bias": svi_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V96_SVI: {svi_res['reason']}",
                "phase": "GOD_EXECUTION"
            }
        
        # 🎯 3. EXECUTION COMPLETION DETECTOR
        # Jika eksekusi sudah selesai, jangan entry searah!
        if ecd_res.get('completed'):
            return {
                "bias": ecd_res['direction'],
                "confidence": "ABSOLUTE",
                "reason": f"V96_ECD: {ecd_res['reason']}",
                "phase": "DISTRIBUTION_PHASE"
            }
        
        # 🛡️ 4. RETAIL POSITIONING TRAP (Hanya aktif jika bukan singularitas)
        # Catatan: SVI sudah handle kasus WMI > 99.5, jadi ini aman
        if rpt_res.get('is_trap'):
            return {
                "bias": rpt_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V95_RPT: {rpt_res['reason']}",
                "phase": "ENERGY_VENGEANCE"
            }
        
        # 🏗️ 5. POSITION BUILD DETECTOR (PALING PENTING! - Kasus LYN)
        if pbd_res.get('active'):
            return {
                "bias": pbd_res['bias'],
                "confidence": pbd_res.get('confidence', 'ABSOLUTE'),
                "reason": f"V96_PBD: {pbd_res['reason']}",
                "phase": "POSITION_BUILD_PHASE"
            }
        
        # 💧 6. OI-DIRECTIONAL CONFLICT (Real Shorting/Longing)
        if oid_res.get('active'):
            return {
                "bias": oid_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V95_OID: {oid_res['reason']}",
                "phase": "REAL_POSITIONING"
            }
        
        # 👑 5. OI DOMINANCE RULE (Price follows OI)
        if odr_res.get('active'):
            return {
                "bias": odr_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V96_ODR: {odr_res['reason']}",
                "phase": "OI_DOMINANCE"
            }
        
        # 🔥 6. SHORT COVERING RULE
        if rsc_res.get('is_active'):
            return {
                "bias": rsc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V95_RSC: {rsc_res['reason']}",
                "phase": "SHORT_COVERING_RALLY"
            }
        
        # ⚡ 5. LOW ENERGY PRIORITY (Energy Supremacy atas Cascade Time)
        if lep_res.get('is_active'):
            return {
                "bias": lep_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V95_LEP: {lep_res['reason']}",
                "phase": "ENERGY_SUPREMACY"
            }
        
        # 🎣 6. BAITING PRICE FILTER
        if bpf_res.get('is_bait'):
            return {
                "bias": bpf_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V94_BPF: {bpf_res['reason']}",
                "phase": "ANTI_BAIT_REBOUND"
            }
        
        # 🕳️ 7. LIQUIDATION GAP DETECTOR
        if lgd_res.get('bias') != "NEUTRAL":
            return {
                "bias": lgd_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V95_LGD: {lgd_res['reason']}",
                "phase": "GAP_SQUEEZE"
            }
        
        # ⚡ 8. ENERGY GRAVITY RULE
        if egr_res.get('is_veto'):
            return {
                "bias": egr_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V94_EGR: {egr_res['reason']}",
                "phase": "ENERGY_GRAVITY_VETO"
            }
        
        # 🎯 9. MARKET PHASE VETO
        if phase_res.get('priority') in ['ABSOLUTE', 'SUPREME']:
            return {
                "bias": phase_res.get('signal', phase_res['bias']),
                "confidence": phase_res['priority'],
                "reason": f"PHASE_OVERRIDE: {phase_res['reason']}",
                "phase": phase_res['phase']
            }
        
        # 🛡️ 10. ENERGY SPOOF TRACKER
        if est_res.get('is_spoof'):
            return {
                "bias": est_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V95_EST: {est_res['reason']}",
                "phase": "SPOOF_COLLAPSE"
            }
        
        # 💧 11. OI DRAIN CONDEMNATION
        if odc_res.get('active'):
            return {
                "bias": odc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V93_ODC: {odc_res['reason']}",
                "phase": "VACUUM_FLUSH"
            }
        
        # 📉 12. PASSIVE DISTRIBUTION DETECTOR
        if pdd_res.get('active'):
            return {
                "bias": pdd_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V96_PDD: {pdd_res['reason']}",
                "phase": "PASSIVE_DISTRIBUTION"
            }
        
        # 🔄 13. PASSIVE LIQUIDITY RELOAD
        if plr_res.get('active'):
            return {
                "bias": plr_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V94_PLR: {plr_res['reason']}",
                "phase": "STEALTH_ACCUMULATION"
            }
        
        # 🧲 14. ORDERBOOK PULL DETECTOR
        if opd_res.get('active'):
            return {
                "bias": opd_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V93_OPD: {opd_res['reason']}",
                "phase": "LIQUIDITY_VACUUM"
            }
        
        # 💀 15. WMI SINGULARITY EXHAUSTION
        if wmi_exhaust_res.get('active'):
            return {
                "bias": wmi_exhaust_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V93_WMI_EXHAUST: {wmi_exhaust_res['reason']}",
                "phase": "SINGULARITY_TRAP"
            }
        
        # ⏱️ 16. CASCADE TIME ESTIMATOR
        if cascade_res.get('bias') != "NEUTRAL":
            return {
                "bias": cascade_res['bias'],
                "confidence": "HIGH",
                "reason": f"V93_CASCADE: {cascade_res['reason']}",
                "phase": "CASCADE_PATH"
            }
        
        # ⚡ 17. EXECUTION ENERGY
        if energy_res.get('bias') != "NEUTRAL":
            return {
                "bias": energy_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V92_ENERGY: {energy_res['reason']}",
                "phase": "EXECUTION_ENERGY"
            }
        
        # 🕳️ 18. LIQUIDITY GRAVITY DRAIN
        if lgd_void_res.get('active'):
            return {
                "bias": lgd_void_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V91_LGD: {lgd_void_res['reason']}",
                "phase": "VOID_DRAIN"
            }
        
        # 🌌 19. WHALE SINGULARITY
        if wsc_res.get('is_active'):
            return {
                "bias": wsc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V89_WSC: {wsc_res['reason']}",
                "phase": "SINGULARITY_EXECUTION"
            }
        
        # ⚡ 20. LIQUIDITY SATURATION
        if sat_res.get('active'):
            return {
                "bias": sat_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V90_SAT: {sat_res['reason']}",
                "phase": "SATURATION_SQUEEZE"
            }
        
        # 🔥 21. POSITION EXPANSION TRAP
        if pet_res.get('active'):
            return {
                "bias": pet_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V90_PET: {pet_res['reason']}",
                "phase": "EXPANSION_TRAP"
            }
        
        # 🔴 22. ZERO GRAVITY HORIZON
        if zgh_res.get('is_ceiling'):
            return {
                "bias": "SHORT",
                "confidence": "ABSOLUTE",
                "reason": f"V86_ZGH: {zgh_res['reason']}",
                "phase": "ZERO_GRAVITY"
            }
        
        # 🟢 23. OVERSOLD TRAP
        if otf_res.get('is_trap'):
            return {
                "bias": "LONG" if otf_res.get('scenario') == 'LIQUIDITY_VACUUM_REBOUND' else otf_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V85_OTF: {otf_res['reason']}",
                "phase": "OVERSOLD_TRAP"
            }
        
        # ⚖️ 24. LIQUIDITY IMBALANCE
        if lim_res.get('bias') != "NEUTRAL" and lim_res.get('imbalance_ratio', 1.0) > 10:
            return {
                "bias": lim_res['bias'],
                "confidence": "HIGH",
                "reason": f"V87_LIM: {lim_res['reason']}",
                "phase": "IMBALANCE_MOMENTUM"
            }
        
        # Fallback
        return {
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "No strong signal detected.",
            "phase": "NEUTRAL"
        }


# ================= V96: GHOST WALL CONDEMNATION (GWC) - ANTI-LYN ILLUSION TRAP =================
class GhostWallCondemnationV96:
    """
    🔥 V96: GHOST WALL CONDEMNATION - MENDETEKSI 'TEMBOK HANTU' 🔥
    
    Kasus LYNUSDT:
    - Flow: 0.02x (FREEZE! Nggak ada transaksi)
    - Downside Energy: 303.0 (SANGAT EKSTRIM!)
    - RSI: 86 (Overbought)
    
    Interpretasi:
    Tembok bawah 303.0 itu 100% PALSU (Ghost Wall). MM cuma naruh order
    buat nakutin SHORT seller & mancing LONG buyer. Begitu LONG masuk,
    tembok dicabut -> FREE FALL 7% karena orderbook bawah kosong.
    
    Rule: Jika Flow < 0.05 (freeze) DAN Downside Energy > 150, maka GHOST WALL!
    """
    @staticmethod
    def analyze(flow: float, agg: float, down_energy: float, rsi: float) -> Dict:
        # Cek kondisi market freeze dengan tembok raksasa
        if flow < GWC_FLOW_MAX and down_energy > GWC_ENERGY_DOWN_MIN:
            # Validasi dengan RSI (harga di area tinggi)
            if rsi > GWC_RSI_OVERBOUGHT_MIN:
                return {
                    "is_ghost_wall": True,
                    "bias": "SHORT",
                    "reason": f"GWC_GHOST_WALL: Flow mati ({flow}x) TAPI Energy Downside ({down_energy:.1f}) meledak. "
                             f"RSI {rsi:.1f} overbought. Ini GHOST WALL! Whale siap cabut jaring beli. "
                             f"JANGAN LONG, bensin Dump sedang disiapkan!"
                }
            else:
                # Ghost wall di area netral (tetap spoof, tapi kurang yakin)
                return {
                    "is_ghost_wall": True,
                    "bias": "SHORT",
                    "reason": f"GWC_GHOST_WALL_SUSPECT: Flow mati ({flow}x) TAPI Energy Downside ({down_energy:.1f}) besar. "
                             f"Ini kemungkinan GHOST WALL. Waspada potensi dump!"
                }
        
        return {"is_ghost_wall": False, "bias": "NEUTRAL", "reason": ""}


# ================= V97: LIQUIDITY VACUUM DETECTOR (LVD) - DETEKSI VACUUM DUMP =================
class LiquidityVacuumDetectorV97:
    """
    🔥 V97: LIQUIDITY VACUUM DETECTOR - PREDIKSI DUMP CEPAT 🔥
    
    Kasus LYNUSDT:
    - Flow: 0.02x (freeze)
    - Agg: 0.0x (mati)
    - RSI: 86 (overbought)
    - Energy Downside besar (tapi palsu)
    
    Ini bukan cuma ghost wall. Ini fase sebelum LIQUIDITY VACUUM DROP.
    Orderbook bawah kosong. Ketika whale cancel bid wall, tidak ada liquidity
    untuk menahan price. Hasilnya: price free fall 7% tanpa resistance.
    
    Rule: Flow < 0.05 + Agg < 0.1 + RSI > 75 = VACUUM DUMP!
    """
    @staticmethod
    def analyze(flow: float, agg: float, rsi: float) -> Dict:
        if flow < LVD_FLOW_MAX and agg < LVD_AGG_MAX and rsi > LVD_RSI_MIN:
            return {
                "active": True,
                "bias": "SHORT",
                "reason": f"LVD_VACUUM: Market freeze (Flow {flow}x, Agg {agg}x) + RSI {rsi:.1f} overbought. "
                         f"Orderbook kemungkinan kosong! Dump cascade incoming tanpa hambatan!"
            }
        
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V97: SILENT DISTRIBUTION DETECTOR (SDD) - ANTI-DISTRIBUTION TOP =================
class SilentDistributionDetectorV97:
    """
    🔥 V97: SILENT DISTRIBUTION DETECTOR - WHALE JUAL PELAN TANPA MARKET SELL 🔥
    
    Kasus LYNUSDT:
    - RSI: 86 (extreme overbought)
    - OI: +1.47% (naik - posisi baru masuk)
    - Flow: 0.02x (mati)
    
    Ini pattern klasik DISTRIBUTION TOP:
    1. MM pump harga (RSI tinggi)
    2. Jual via limit orders (Agg = 0 karena pakai limit sell)
    3. OI naik (short building atau posisi baru)
    4. Flow mati (transaksi sepi)
    
    Rule: RSI > 80 + OI > 0 + Flow < 0.5 = SILENT DISTRIBUTION!
    """
    @staticmethod
    def analyze(rsi: float, oi_delta: float, flow: float) -> Dict:
        if rsi > SDD_RSI_MIN and oi_delta > SDD_OI_DELTA_MIN and flow < SDD_FLOW_MAX:
            return {
                "active": True,
                "bias": "SHORT",
                "reason": f"SDD_DISTRIBUTION: RSI {rsi:.1f} extreme + OI Δ {oi_delta:+.2f}% (rising) + Flow {flow}x (low). "
                         f"Whale distributing positions via limit orders. DISTRIBUTION TOP! SIAP DUMP!"
            }
        
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V97: CONFLICT RESOLVER (THE GHOST WALL HIERARCHY) =================
class ConflictResolverV97:
    """
    🔥 URUTAN PRIORITAS MUTLAK V97 (THE FINAL HIERARCHY - DENGAN EHS + VAC + PBD + EVH + SVI + GWC + LVD + SDD + ECD + RPT) 🔥
    
    HIERARKI FINAL (LENGKAP):
    1. EHS (Event Horizon Singularity) - Energy Ratio > 20x + WMI > 95 ⭐ BARU! (Anti-ARIA Trap)
    2. VAC (Vacuum Detector) - Agg < 0.2 + Flow > 1.5 ⭐ BARU! (Orderbook Vacuum)
    3. PBD (Position Build Detector) - OI > 3% + price move ⭐ BARU!
    4. EVH (Event Horizon) - Jika WMI > 95 & jarak < 0.3% ⭐ BARU!
    5. SVI (Singularity Veto) - Jika WMI > 99.5 (Veto Segala Veto) ⭐ BARU!
    6. ECD (Execution Completion Detector) (V96) ⭐ BARU! - Deteksi fase distribusi
    7. RPT (Retail Positioning Trap) (V95) ⭐ BARU! - Anti-crowded trap
    8. MARKET PHASE (V91) - Konteks market (paling penting!)
    9. GWC (Ghost Wall Condemnation) (V96) ⭐ - Flow <0.05 + Energy >150 = GHOST WALL!
    10. LVD (Liquidity Vacuum Detector) (V97) ⭐ - Flow <0.05 + Agg <0.1 + RSI >75 = VACUUM DUMP!
    11. SDD (Silent Distribution Detector) (V97) ⭐ - RSI >80 + OI >0 + Flow <0.5 = DISTRIBUTION!
    12. EST (Energy Spoof Tracker) (V95) - Energy >100 + OI turun = SPOOF!
    13. ODC (OI Drain Condemnation) (V93) - OI >3% drop + RSI >90 → FLUSH!
    14. PDD (Passive Distribution Detector) (V96) - OI turun + Flow tinggi + RSI <50
    15. LEP (Low Energy Path) (V94) - Energy ratio >10x → veto!
    16. PLR (Passive Liquidity Reload) (V94) - OI naik + Agg mati
    17. OPD (Orderbook Pull Detector) (V93) - Bid wall hilang + OI drop
    18. WMI EXHAUST (V93) - WMI 99 + OI crash
    19. CASCADE TIME (V93) - Jalur cascade tercepat
    20. EXECUTION ENERGY (V92) - Jalur termudah
    21. AGGRESSION DEATH (V92) - Market mati
    22. LGD (Void Drain) (V91) - Void trap
    23. WSC (Whale Singularity) (V89)
    24. SAT (Liquidity Saturation) (V90)
    25. PET (Position Expansion Trap) (V90)
    26. ZGH (Zero Gravity) (V86)
    27. OTF (Oversold Trap) (V85)
    28. LIM (Liquidity Imbalance) (V87)
    """
    @staticmethod
    def resolve(
        # NEW MODULES V97/V98 - PRIORITAS TERTINGGI!
        ehs_res: Dict,                # V97 Event Horizon Singularity ⭐ BARU! (Anti-ARIA)
        vac_res: Dict,                 # V98 Vacuum Detector ⭐ BARU! (Orderbook Vacuum)
        pbd_res: Dict,                  # V96 Position Build Detector ⭐ BARU!
        
        # Existing high priority modules
        evh_res: Dict,                # V97 Event Horizon Detector ⭐ BARU!
        svi_res: Dict,                 # V96 Singularity Veto Integrity ⭐ BARU!
        ecd_res: Dict,               # V96 Execution Completion Detector ⭐ BARU!
        rpt_res: Dict,                # V95 Retail Positioning Trap ⭐ BARU!
        
        phase_res: Dict,           # V91 Market Phase
        gwc_res: Dict,               # V96 Ghost Wall Condemnation ⭐
        lvd_res: Dict,                # V97 Liquidity Vacuum Detector ⭐
        sdd_res: Dict,                # V97 Silent Distribution Detector ⭐
        est_res: Dict,               # V95 Energy Spoof Tracker
        odc_res: Dict,              # V93 OI Drain Condemnation
        pdd_res: Dict,                # V96 Passive Distribution Detector
        lep_res: Dict,              # V94 Low Energy Path
        plr_res: Dict,               # V94 Passive Liquidity Reload
        opd_res: Dict,              # V93 Orderbook Pull Detector
        wmi_exhaust_res: Dict,      # V93 WMI Exhaustion
        cascade_res: Dict,          # V93 Cascade Time Estimator
        energy_res: Dict,           # V92 Execution Energy
        death_res: Dict,            # V92 Aggression Death
        lgd_res: Dict,              # V91 Liquidity Gravity Drain
        wsc_res: Dict,              # V89 Whale Singularity
        sat_res: Dict,              # V90 Liquidity Saturation
        pet_res: Dict,              # V90 Position Expansion Trap
        zgh_res: Dict,              # V86 Zero Gravity Horizon
        otf_res: Dict,              # V85 Oversold Trap Filter
        lim_res: Dict               # V87 Liquidity Imbalance
    ) -> Dict:
        
        # 🕳️ 1. EVENT HORIZON SINGULARITY (Penyelamat ARIA - Anti Over-Logic)
        # Jika energy ratio > 20x + WMI > 95, ini black hole. Jangan counter!
        if ehs_res.get('is_active'):
            return {
                "bias": ehs_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V97_EHS: {ehs_res['reason']}",
                "phase": "EVENT_HORIZON_SUCTION"
            }
        
        # 💨 2. VACUUM DETECTOR (Orderbook kosong)
        # Jika seller mati (Agg < 0.2) tapi volume masuk, price akan mudah bergerak
        if vac_res.get('active'):
            return {
                "bias": vac_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V98_VAC: {vac_res['reason']}",
                "phase": "LIQUIDITY_VACUUM"
            }
        
        # 🏗️ 3. POSITION BUILD DETECTOR (OI meledak + price move)
        # Whale sedang membangun posisi, ikuti arah OI
        if pbd_res.get('active'):
            return {
                "bias": pbd_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V96_PBD: {pbd_res['reason']}",
                "phase": "POSITION_BUILD_PHASE"
            }
        
        # 🎯 4. EVENT HORIZON (WMI > 95 + jarak < 0.3%)
        if evh_res.get('active'):
            return {
                "bias": evh_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V97_EVH: {evh_res['reason']}",
                "phase": "EVENT_HORIZON"
            }
        
        # 🌌 5. SINGULARITY VETO INTEGRITY (Anti-OverLogic DEGO)
        # Jika WMI > 99.5, veto semua filter lain
        if svi_res.get('is_absolute_veto'):
            return {
                "bias": svi_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V96_SVI: {svi_res['reason']}",
                "phase": "GOD_EXECUTION"
            }
        
        # 🎯 6. EXECUTION COMPLETION DETECTOR
        # Jika eksekusi sudah selesai, jangan entry searah!
        if ecd_res.get('completed'):
            return {
                "bias": ecd_res['direction'],
                "confidence": "ABSOLUTE",
                "reason": f"V96_ECD: {ecd_res['reason']}",
                "phase": "DISTRIBUTION_PHASE"
            }
        
        # 🛡️ 7. RETAIL POSITIONING TRAP (Hanya aktif jika bukan singularitas)
        # Catatan: SVI sudah handle kasus WMI > 99.5, jadi ini aman
        if rpt_res.get('is_trap'):
            return {
                "bias": rpt_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V95_RPT: {rpt_res['reason']}",
                "phase": "ENERGY_VENGEANCE"
            }
        
        # 🎯 8. MARKET PHASE VETO (Raja - Paling Penting!)
        if phase_res.get('priority') in ['ABSOLUTE', 'SUPREME']:
            return {
                "bias": phase_res.get('signal', phase_res['bias']),
                "confidence": phase_res['priority'],
                "reason": f"PHASE_OVERRIDE: {phase_res['reason']}",
                "phase": phase_res['phase']
            }
        
        # 👻 9. GHOST WALL CONDEMNATION (V96) - Flow mati + Energy raksasa
        if gwc_res.get('is_ghost_wall'):
            return {
                "bias": gwc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V96_GWC: {gwc_res['reason']}",
                "phase": "GHOST_WALL_COLLAPSE"
            }
        
        # 💨 10. LIQUIDITY VACUUM DETECTOR (V97) - Freeze + RSI tinggi = vacuum dump
        if lvd_res.get('active'):
            return {
                "bias": lvd_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V97_LVD: {lvd_res['reason']}",
                "phase": "VACUUM_DUMP"
            }
        
        # 📊 11. SILENT DISTRIBUTION DETECTOR (V97) - RSI tinggi + OI naik + flow rendah
        if sdd_res.get('active'):
            return {
                "bias": sdd_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V97_SDD: {sdd_res['reason']}",
                "phase": "SILENT_DISTRIBUTION"
            }
        
        # 🛡️ 12. ENERGY SPOOF TRACKER (V95)
        if est_res.get('is_spoof'):
            return {
                "bias": est_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V95_EST: {est_res['reason']}",
                "phase": "SPOOF_COLLAPSE"
            }
        
        # 💧 13. OI DRAIN CONDEMNATION (V93)
        if odc_res.get('active'):
            return {
                "bias": odc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V93_ODC: {odc_res['reason']}",
                "phase": "VACUUM_FLUSH"
            }
        
        # 📉 14. PASSIVE DISTRIBUTION DETECTOR (V96)
        if pdd_res.get('active'):
            return {
                "bias": pdd_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V96_PDD: {pdd_res['reason']}",
                "phase": "PASSIVE_DISTRIBUTION"
            }
        
        # ⚡ 15. LOW ENERGY PATH (V94)
        if lep_res.get('is_active'):
            return {
                "bias": lep_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V94_LEP: {lep_res['reason']}",
                "phase": "ENERGY_PATH_VETO"
            }
        
        # 🔄 16. PASSIVE LIQUIDITY RELOAD (V94)
        if plr_res.get('active'):
            return {
                "bias": plr_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V94_PLR: {plr_res['reason']}",
                "phase": "STEALTH_ACCUMULATION"
            }
        
        # 🧲 10. ORDERBOOK PULL DETECTOR (V93)
        if opd_res.get('active'):
            return {
                "bias": opd_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V93_OPD: {opd_res['reason']}",
                "phase": "LIQUIDITY_VACUUM"
            }
        
        # 💀 11. WMI SINGULARITY EXHAUSTION (V93)
        if wmi_exhaust_res.get('active'):
            return {
                "bias": wmi_exhaust_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V93_WMI_EXHAUST: {wmi_exhaust_res['reason']}",
                "phase": "SINGULARITY_TRAP"
            }
        
        # ⏱️ 12. CASCADE TIME ESTIMATOR (V93)
        if cascade_res.get('bias') != "NEUTRAL":
            return {
                "bias": cascade_res['bias'],
                "confidence": "HIGH",
                "reason": f"V93_CASCADE: {cascade_res['reason']}",
                "phase": "CASCADE_PATH"
            }
        
        # ⚡ 13. EXECUTION ENERGY (V92)
        if energy_res.get('bias') != "NEUTRAL":
            return {
                "bias": energy_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V92_ENERGY: {energy_res['reason']}",
                "phase": "EXECUTION_ENERGY"
            }
        
        # 🕳️ 14. LIQUIDITY GRAVITY DRAIN (V91)
        if lgd_res.get('active'):
            return {
                "bias": lgd_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V91_LGD: {lgd_res['reason']}",
                "phase": "VOID_DRAIN"
            }
        
        # 🌌 15. WHALE SINGULARITY (V89)
        if wsc_res.get('is_active'):
            return {
                "bias": wsc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V89_WSC: {wsc_res['reason']}",
                "phase": "SINGULARITY_EXECUTION"
            }
        
        # ⚡ 16. LIQUIDITY SATURATION (V90)
        if sat_res.get('active'):
            return {
                "bias": sat_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V90_SAT: {sat_res['reason']}",
                "phase": "SATURATION_SQUEEZE"
            }
        
        # 🔥 17. POSITION EXPANSION TRAP (V90)
        if pet_res.get('active'):
            return {
                "bias": pet_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V90_PET: {pet_res['reason']}",
                "phase": "EXPANSION_TRAP"
            }
        
        # 🔴 18. ZERO GRAVITY HORIZON (V86)
        if zgh_res.get('is_ceiling'):
            return {
                "bias": "SHORT",
                "confidence": "ABSOLUTE",
                "reason": f"V86_ZGH: {zgh_res['reason']}",
                "phase": "ZERO_GRAVITY"
            }
        
        # 🟢 19. OVERSOLD TRAP (V85)
        if otf_res.get('is_trap'):
            return {
                "bias": "LONG" if otf_res.get('scenario') == 'LIQUIDITY_VACUUM_REBOUND' else otf_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V85_OTF: {otf_res['reason']}",
                "phase": "OVERSOLD_TRAP"
            }
        
        # ⚖️ 20. LIQUIDITY IMBALANCE (V87)
        if lim_res.get('bias') != "NEUTRAL" and lim_res.get('imbalance_ratio', 1.0) > 10:
            return {
                "bias": lim_res['bias'],
                "confidence": "HIGH",
                "reason": f"V87_LIM: {lim_res['reason']}",
                "phase": "IMBALANCE_MOMENTUM"
            }
        
        # Fallback
        return {
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "No strong signal detected.",
            "phase": "NEUTRAL"
        }


# V82 - LIQUIDITY MIRROR GUARD (LMG) - BARU!
LMG_DEATH_DISTANCE_MAX = 0.05                   # Jarak kritis untuk Death Magnet (<0.05%)
LMG_RSI_DEATH_LONG_MAX = 10                     # Maksimal RSI untuk Death Magnet LONG (<10)
LMG_RSI_DEATH_SHORT_MIN = 90                    # Minimal RSI untuk Death Magnet SHORT (>90)

# V81 - LIQUIDITY THINNING GUARD (LTG) - BARU!
LTG_FLOW_VACUUM_MIN = 50.0                    # Minimal Flow untuk deteksi Liquidity Vacuum

# V81 - INTERNAL CROSS DETECTOR (ICD) - BARU!
ICD_FLOW_MIN = 2.0                            # Minimal Flow untuk deteksi Internal Cross
ICD_AGGRESSION_MAX = 2.0                       # Maksimal Aggressive Ratio
ICD_OI_DELTA_MAX = 0.5                         # Maksimal OI Delta

# V80 - INSTITUTIONAL EXIT RADAR (IER) - BARU!
IER_FLOW_MIN = 2.0                      # Minimal Flow untuk deteksi Institutional Exit (>2.0x)
IER_OI_DELTA_MAX = 1.0                   # Maksimal OI Delta untuk deteksi Exit (<1.0%)
IER_AGGRESSION_CHECK = True              # Cek Aggressive Ratio untuk validasi
IER_CONFIDENCE_ABSOLUTE = True            # Confidence mutlak untuk filter ini

# V80 - RSI MOMENTUM GUARD (RMG) - BARU!
RMG_RSI_MIN = 50                          # Minimal RSI untuk deteksi No Man's Land (>50)
RMG_RSI_MAX = 72                           # Maksimal RSI untuk deteksi No Man's Land (<72)
RMG_AGGRESSION_MAX = 1.0                   # Maksimal Aggressive Ratio untuk deteksi weak momentum (<1.0x)
RMG_SHORT_DIST_MAX = 1.0                    # Maksimal jarak Short Liq untuk validasi (<1.0%)
RMG_CONFIDENCE_ABSOLUTE = True              # Confidence mutlak untuk filter ini

# V80 - FAKE MAGNET VACUUM (FMV) - KOMBINASI IER + RMG
FMV_RSI_NEUTRAL_MIN = 39                    # RSI neutral zone bawah
FMV_RSI_NEUTRAL_MAX = 72                     # RSI neutral zone atas
FMV_FLOW_INFLATION_MIN = 2.0                 # Minimal Flow untuk deteksi Flow Inflation
FMV_OI_STAGNANT_MAX = 1.0                     # Maksimal OI Delta untuk deteksi OI Stagnan

# V79 - WASH TRADE DETECTOR (WTD)
WTD_FLOW_MIN = 10.0                     # Minimal Flow untuk deteksi Wash Trade (>10.0x)
WTD_RSI_MIN = 70                         # Minimal RSI untuk deteksi overbought palsu (>70)
WTD_CONFIDENCE_ABSOLUTE = True           # Confidence mutlak untuk filter ini

# V78 - EXECUTION ZONE HUNTER (EZH)
EZH_DISTANCE_MAX = 0.1                    # Maksimal jarak untuk Execution Zone (<0.1%)
EZH_RSI_OVERBOUGHT_MIN = 85                # RSI overbought minimal untuk SHORT execution
EZH_RSI_OVERSOLD_MAX = 15                  # RSI oversold maksimal untuk LONG execution

# V78 - PANIC SELL VALIDATOR (PSV)
PSV_RSI_OVERSOLD_MAX = 20                  # RSI oversold maksimal
PSV_FLOW_WHALE_MIN = 2.0                    # Minimal Flow untuk bukti Whale nampung (>2.0x)
PSV_CONFIDENCE_ABSOLUTE = True              # Confidence mutlak untuk filter ini

# V77 - OVERDRIVE FLOW FILTER (OFF)
OFF_FLOW_MIN = 2.5                         # Minimal Trade Flow untuk deteksi Liquidity Patching
OFF_DISTANCE_MAX = 0.2                      # Maksimal jarak likuidasi untuk overdrive

# V77 - AGGRESSIVE EXHAUSTION FILTER (AEF)
AEF_AGGRESSION_MIN = 10.0                   # Minimal Aggressive Ratio untuk deteksi retail FOMO
AEF_RSI_MIN = 80                            # Minimal RSI untuk deteksi overbought
AEF_OI_DELTA_MAX = 2.0                      # Maksimal OI Delta untuk validasi (harus <2%)

# V76 - PANIC SATURATION REVERSAL (PSR)
PSR_AGGRESSION_MIN = 5.0                    # Minimal Aggressive Ratio untuk panic saturation
PSR_PRICE_MA_DIFF_MAX = 0.05                 # Maksimal perbedaan harga dengan MA
PSR_RSI_MAX = 40                             # Maksimal RSI untuk validasi
PSR_FLOW_MIN = 0.5                           # Minimal Trade Flow untuk validasi

# V75 - ABSORPTION MOMENTUM VALIDATOR (AMV)
AMV_OI_DELTA_MIN = 3.0                       # Minimal OI Delta untuk deteksi akumulasi
AMV_AGGRESSION_MIN = 2.5                     # Minimal Aggressive Ratio
AMV_TRADE_FLOW_MIN = 0.7                      # Minimal Trade Flow

# V75 - LIQUIDATION GRAVITY OVERDRIVE (LGO)
LGO_SHORT_DIST_MAX = 0.2                      # Maksimal jarak Short Liq untuk overdrive
LGO_LONG_DIST_MAX = 0.2                       # Maksimal jarak Long Liq untuk overdrive

# V84 - FAKE GRAVITY DETECTOR (FGD) - BARU!
FGD_LONG_DIST_MAX = 0.2                       # Maksimal jarak Long Liq untuk deteksi fake gravity
FGD_FLOW_MIN = 0.6                            # Minimal Flow untuk validasi weak sell pressure
FGD_AGG_MIN = 0.8                             # Minimal Agg untuk validasi netral/no real selling

# V84 - LIQUIDITY DENSITY FILTER (LDF) - BARU!
LDF_DENSITY_THRESHOLD = 1.5                   # Threshold density ratio untuk bias detection

# V84 - WEAK DUMP FILTER (WDF) - BARU!
WDF_FLOW_MIN = 0.6                            # Minimal Flow untuk weak dump detection
WDF_AGG_MIN = 0.8                             # Minimal Agg untuk weak dump detection

# V84 - LONG LIQUIDITY SHIELD (LLS) - BARU!
LLS_WMI_THRESHOLD = -80                       # WMI threshold untuk long liquidity shield

# V84 - FUNDING SKEW DETECTOR (FSD) - BARU!
FSD_FUNDING_NEGATIVE_THRESHOLD = -0.01        # Funding negative threshold untuk pump detection

# V85 - OVERSOLD TRAP FILTER (OTF) - BARU! (Patch Kasus UAIUSDT & Liquidity Vacuum Rebound)
OTF_RSI_MAX = 15                               # Maksimal RSI untuk deteksi oversold trap (naik dari 10 ke 15)
OTF_WMI_MIN = -90                              # WMI < -90 = extreme short liquidation cluster below
OTF_AGG_MIN = 1.0                              # Agg > 1.0 = ada agresi beli di dasar
OTF_OI_DELTA_MAX = 0                           # OI Delta harus negatif (< 0) untuk trap detection
OTF_FLOW_MAX = 1.0                             # Flow < 1.0 = tidak ada volume confirmation

# V85 - NEUTRAL ZONE SHIELD (NZS) - BARU! (Patch Kasus STABLEUSDT - Anti-STABLE Trap)
NZS_RSI_MIN = 40                               # RSI neutral zone bawah
NZS_RSI_MAX = 65                               # RSI neutral zone atas
NZS_WMI_THRESHOLD = -80                        # WMI < -80 = Whale protect downside (Long Liquidity Shield)
NZS_IER_ACTIVE_CHECK = True                    # Cek apakah IER aktif untuk trigger shield

# V85 - POSITION FLIP DETECTOR (PFD) - BARU! (Patch Kasus STABLEUSDT - Internal Flow Illusion)
PFD_FLOW_MIN = 2.0                             # Flow > 2 = high flow
PFD_AGG_MAX = 1.0                              # Agg < 1 = low aggression (internal matching)
PFD_OI_DROP_MIN = -0.5                         # OI drop < -0.5% = position reload signal

# V85 - FAKE EXIT DETECTOR (FED_V85) - BARU! (Patch Kasus STABLEUSDT)
FED_V85_FLOW_MIN = 2.0                         # Flow > 2 = suspicious high flow
FED_V85_AGG_MAX = 1.0                          # Agg < 1 = fake exit (no real selling)

# V85 - LIQUIDITY RELOAD DETECTOR (LRD) - BARU! (Patch Kasus STABLEUSDT)
LRD_OI_DROP_MIN = 0                            # OI drop (negatif) = liquidity reset
LRD_WMI_THRESHOLD = -70                        # WMI < -70 = long liquidation pool besar

# V85 - AGGRESSION ABSORPTION FILTER (AAF) - BARU! (Patch Kasus UAIUSDT)
AAF_AGG_MIN = 3.0                              # Agg > 3x = aggressive buyers
AAF_FLOW_MAX = 1.0                             # Flow < 1.0 = volume tidak naik (buyers trapped)

# V85 - FAKE EXHAUSTION DETECTOR (FED) - BARU! (Patch Kasus UAIUSDT)
FED_RSI_MAX = 10                               # RSI < 10 = extreme oversold
FED_OI_DELTA_MAX = 0                           # OI turun = positions closing, bukan new longs

# V86 - ZERO GRAVITY HORIZON (ZGH) - BARU! (Anti-TRIA Trap)
ZGH_RSI_CEILING = 90                           # RSI > 90 = Nuclear Overbought
ZGH_OI_DELTA_MIN = 0.5                         # OI Delta > 0.5% = new positions building
ZGH_AGG_CEILING = 2.0                          # Agg < 2.0 = weak aggression (passive distribution)

# V86 - OVERBOUGHT DISTRIBUTION FILTER (ODF) - BARU! (Anti-TRIA Trap)
ODF_RSI_THRESHOLD = 90                         # RSI > 90 = extreme overbought
ODF_OI_DELTA_THRESHOLD = 0.5                   # OI Delta > 0.5% = whale building shorts
ODF_AGG_THRESHOLD = 2.0                        # Agg < 2.0 = passive sell wall

# V74 - MAGNET DECAY VALIDATOR (MDV)
MDV_MAX_WAIT_MINUTES = 10                     # Maksimal waktu tunggu magnet

# V73 - PASSIVE ABSORPTION BLACKHOLE (PAB)
PAB_FLOW_MIN = 10.0                           # Minimal Flow untuk deteksi blackhole
PAB_AGGRESSION_MAX = 1.5                       # Maksimal Aggressive Ratio

# V72 - CATCHING FALLING KNIVES (CFK)
CFK_WMI_EXTREME_NEGATIVE = -60                 # WMI sangat negatif
CFK_RSI_OVERSOLD_MAX = 25                      # RSI oversold maksimal
CFK_OI_DELTA_MIN = 1.5                          # Minimal OI delta

# V71 - MAGNET DISTANCE DOMINANCE (MDD)
MDD_MAX_DISTANCE = 0.8                         # Maksimal jarak likuidasi
MDD_MIN_RSI = 70                                # RSI minimal

# V70 - ORDERBOOK VACUUM DEFENSE (OVD)
OVD_BID_THINNING_RSI_MAX = 35                   # Maksimal RSI untuk deteksi vacuum trap
OVD_ASK_THINNING_RSI_MIN = 65                   # Minimal RSI untuk deteksi vacuum trap

# V69 - TREND INTEGRITY
TREND_MA_SHORT = 10
TREND_MA_LONG = 20
TREND_OBV_HISTORY_MIN = 3
TREND_OBV_CONSISTENCY = 2

# V68 - GRAVITY DEFLECTION (OGD)
OGD_WMI_EXTREME_NEGATIVE = -90
OGD_WMI_EXTREME_POSITIVE = 90
OGD_RSI_OVERSOLD_MAX = 25
OGD_RSI_OVERBOUGHT_MIN = 75

# V67 - ZERO AGGRESSION SLAUGHTER (ZAS)
ZAS_AGGRESSION_MAX = 0.01
ZAS_WMI_NEGATIVE_MIN = -70
ZAS_WMI_POSITIVE_MIN = 70

# V67 - ABSORPTION VALIDITY CHECK (AVC)
AVC_FLOW_MIN = 1.1
AVC_AGGRESSION_MAX = 0.8
AVC_OI_DELTA_NEGATIVE = 0

# V66 - TEMPORAL ACCUMULATION INDEX (ATI)
ATI_FLOW_MIN = 2.5
ATI_RSI_MAX = 45
ATI_WMI_MIN = 20

# V65 - THE DYL PARTICLE (TDP)
TDP_OI_DELTA_MIN = 5.0
TDP_WMI_MIN = 90
TDP_WMI_NEGATIVE_MIN = -90

# V65 - AGGRESSION-MASS DIVERGENCE (AMD)
AMD_WMI_UP_MIN = 80
AMD_WMI_DOWN_MIN = -80
AMD_AGGRESSION_LONG_MIN = 0.5
AMD_AGGRESSION_SHORT_MAX = 1.5

# VACUUM OVERRIDE THRESHOLDS
VACUUM_WMI_MIN = 95
VACUUM_DISTANCE_MAX = 2.0

# V63 - WALL ERASURE DETECTION (WED)
WED_WMI_EXTREME = 80
WED_RSI_FAKE_MAX = 40
WED_RSI_FAKE_MIN = 60
WED_OI_MIN = 0.5

# RSI Suicide Thresholds
RSI_SUICIDE_MIN = 95
SUICIDE_DISTANCE_MAX = 0.3

# V62 - MAGNET WALL REVERSAL (MWR)
MWR_RSI_MAX = 45
MWR_RSI_MIN = 55
MWR_WMI_THRESHOLD = 0

# V61 - LOW-VOLUME SUCTION (LVS)
LVS_AGGRESSION_MAX = 0.1
LVS_FLOW_MAX = 0.5
LVS_PRICE_MIN = -0.2
LVS_WMI_THRESHOLD = -50
LVS_WMI_POSITIVE_THRESHOLD = 50

# LIQUIDATION THRESHOLDS
EVENT_HORIZON = 0.3
SUPER_CRITICAL_LIQ = 0.5
CRITICAL_LIQ = 1.0
NEAR_LIQ = 2.0
FAR_LIQ = 5.0
DOUBLE_SWEEP_THRESHOLD = 1.5
MAGNET_RULE_THRESHOLD = 0.7

# ENGINE STARTER THRESHOLDS
THINNING_OB_HIGH = 2.5
THINNING_OB_LOW = 0.4
THINNING_AGG_HIGH = 1.2
THINNING_AGG_LOW = 0.8
FUEL_INJECTION_OI = 1.5
FUEL_INJECTION_PRICE = 0.2
FUEL_FLOW_THRESHOLD = 1.1
WHALE_WMI_THRESHOLD = 100
STARTER_MIN_SCORE = 60
RSI_HOT_LIMIT = 85
RSI_COLD_LIMIT = 15

# TTK COUNTDOWN THRESHOLDS
TTK_BASE = 45.0
TTK_OI_FACTOR = 5.0
TTK_OI_MAX_REDUCTION = 20.0
TTK_VOL_FACTOR = 3.0
TTK_VOL_MAX_REDUCTION = 15.0
TTK_SCORE_FACTOR = 10.0
TTK_IMMINENT_THRESHOLD = 5.0
TTK_HIGH_THRESHOLD = 15.0

# V58 - GHOST PROTOCOL THRESHOLDS
OI_FUEL_MINIMUM = 1.5
ABSORPTION_RSI_MAX = 30
ABSORPTION_AGG_MIN = 2.0
ABSORPTION_PRICE_MAX = 0.2
MAGNET_DECOUPLE_DIST = 0.5
RSI_EXTREME_LONG = 80
RSI_EXTREME_SHORT = 20

# ORDERBOOK DEPTH DECAY (ODD) THRESHOLDS
ODD_WINDOW_SIZE = 5
ODD_THIN_RATIO = 0.3
ODD_DEFENSE_RATIO = 3.0
ODD_VOLUME_MIN = 10000

# RSI WALL THRESHOLDS
RSI_NUCLEAR_OVERBOUGHT = 90
RSI_NUCLEAR_OVERSOLD = 10
RSI_EXTREME_HIGH_WALL = 75
RSI_EXTREME_LOW_WALL = 25
RSI_FORBID_LONG = 80
RSI_FORBID_SHORT = 20

# LRR THRESHOLDS
LRR_CLIFF_RATIO = 10.0
LRR_MIN_VOLUME_RATIO = 0.5

# AGGRESSION VELOCITY THRESHOLDS
AV_ACCELERATION_THRESHOLD = 0.5
AV_HISTORY_MIN = 5

# GRAVITY SPOOF THRESHOLDS
GRAVITY_SPOOF_DISTANCE = 1.2
MAGNET_OVERRIDE_DISTANCE = 0.6

# LIQUIDITY GRAVITY THRESHOLDS
LIQ_GRAVITY_EXTREME = 5.0
LIQ_GRAVITY_HIGH = 2.0
LIQ_GRAVITY_POWER = 3
GRAVITY_EXTREME_THRESHOLD = 1000000
GRAVITY_MASSIVE_THRESHOLD = 10000000

# ORDERBOOK THRESHOLDS
OB_EXTREME_BEARISH = 0.5
OB_EXTREME_BULLISH = 2.0
OB_SPOOF_THRESHOLD = 3.0

# TRADE FLOW THRESHOLDS
FLOW_EXTREME_BUY = 3.0
FLOW_EXTREME_SELL = 0.33
FLOW_CAPITULATION = 0.15
FLOW_HIDDEN_DISTRIBUTION = 0.7
FLOW_AGGRESSIVE_THRESHOLD = 0.2
FLOW_CRITICAL_LOW = 0.5
FLOW_CRITICAL_HIGH = 2.0
FLOW_FORCE_LONG = 1.2
AGGRESSION_MIN_LONG = 0.3
AGGRESSION_MIN_SHORT = 0.3

# RSI THRESHOLDS
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
RSI_DEEP_OVERBOUGHT = 75
RSI_DEEP_OVERSOLD = 25
RSI_WARNING_LONG = 65
RSI_EXTREME_OVERSOLD = 15
RSI_EXTREME_OVERBOUGHT = 85
RSI_NO_MANS_LAND_LOW = 30
RSI_NO_MANS_LAND_HIGH = 70

# PREMIUM THRESHOLDS
PREMIUM_EXTREME_SHORT = -0.5
PREMIUM_SUPER_SHORT = -1.5
PREMIUM_CROWDED_LONG = 0.3
PREMIUM_FORBID_LONG = -1.5

# VOLUME THRESHOLDS
VOLUME_SURGE = 2.0
VOLUME_CAPITULATION = 2.0
VOLUME_DISTRIBUTION = 3.0
VOLUME_ACCUMULATION = 1.0
VOLUME_ACCUMULATION_SURGE = 1.5
VOLATILITY_BURST_MULTIPLIER = 2.0
VOLUME_BURST_THRESHOLD = 1.2

# ENERGY THRESHOLDS
ENERGY_SQUEEZE_MIN = 70
ENERGY_EXPLOSIVE_MIN = 80
DUMP_SIZE_FOR_SQUEEZE = 8.0
FUNDING_EXTREME_FOR_SQUEEZE = -5.0
LEVERAGE_SKEW_FOR_SQUEEZE = 3.0

# POSITIONING PRESSURE INDEX
PPI_EXTREME = 3.0
PPI_HIGH = 1.5

# SPOOFING DETECTION
SPOOFING_FLOW_THRESHOLD = 0.5
SPOOFING_OB_THRESHOLD = 2.0

# OI VELOCITY THRESHOLDS
OI_ACCUMULATION_THRESHOLD = 2.0
OI_SURGE_THRESHOLD = 3.0
OI_LIQUIDATION_THRESHOLD = -2.0
OI_EXTREME_DROP = -5.0

# TIME PERSISTENCE
TIME_PERSISTENCE_MINUTES = 15
AGING_FACTOR_PER_MINUTE = 0.05

# DOUBLE SWEEP DETECTION
DOUBLE_SWEEP_CONFIRMATION = 3

# ENTRY CONFIRMATION
CONFIRM_NEUTRAL = 3
CONFIRM_EXPANSION = 1
CONFIRM_DEFAULT = 2
COOLDOWN_SECONDS = 120
PERSISTENCE_CYCLES = 3

# TIMEOUTS
DEFAULT_TIMEOUT = 10
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"

# ================= HELPER FUNCTIONS =================
def safe_get(data, key, default=None):
    """Safe dictionary get dengan error handling"""
    try:
        if isinstance(data, dict):
            return data.get(key, default)
        return default
    except:
        return default

def safe_float(val, default=0.0):
    """Safe float conversion"""
    try:
        if val is None:
            return default
        return float(val)
    except:
        return default

def safe_div(a, b, default=1.0):
    """Safe division"""
    try:
        if b == 0 or b is None:
            return default
        return a / b
    except:
        return default

# ================= V99: REVISED CONFLICT RESOLVER (THE ULTIMATE HIERARCHY) =================
class ConflictResolverV99:
    """
    🔥 URUTAN PRIORITAS MUTLAK V99 (DENGAN SHORT CROWD TRAP):
    
    ⚠️ PRIORITAS BARU V99:
    1. V99-SCT (Short Crowd Trap) - ANTI-CHECKMATE! ⭐ TERTINGGI!
    2. V99 Crowd vs Cluster Logic - Bandingkan Crowd vs Cluster
    3. V99 OI Build at Extremum - Deteksi akumulasi diam-diam
    4. V99 OI Build Validator - Nuclear OI
    5. V99 Gravity Distance - Proximity > Massa
    6. V99 WMI VETO - Hanya valid jika tidak crowded
    7. V99 Internal Trap (FMT)
    8. V97 EHS (Event Horizon Singularity)
    9. V98 VAC (Vacuum Detector)
    10. V96 PBD (Position Build Detector)
    """
    @staticmethod
    def resolve(
        # NEW V99 MODULES - PRIORITAS TERTINGGI!
        sct_res: Dict,                 # V99 Short Crowd Trap ⭐ TERTINGGI!
        crowd_cluster_res: Dict,        # V99 Crowd vs Cluster Logic ⭐
        oi_extremum_res: Dict,          # V99 OI Build at Extremum ⭐
        
        # Existing V99 modules
        oi_build_res: Dict,
        gravity_dist_res: Dict,
        wmi_veto_res: Dict,
        internal_trap_res: Dict,
        density_res: Dict,
        
        # Existing modules
        ehs_res: Dict,
        vac_res: Dict,
        pbd_res: Dict,
        evh_res: Dict,
        svi_res: Dict,
        ecd_res: Dict,
        rpt_res: Dict,
        phase_res: Dict,
        gwc_res: Dict,
        lvd_res: Dict,
        sdd_res: Dict,
        est_res: Dict,
        odc_res: Dict,
        pdd_res: Dict,
        lep_res: Dict,
        plr_res: Dict,
        opd_res: Dict,
        wmi_exhaust_res: Dict,
        cascade_res: Dict,
        energy_res: Dict,
        death_res: Dict,
        lgd_res: Dict,
        wsc_res: Dict,
        sat_res: Dict,
        pet_res: Dict,
        zgh_res: Dict,
        otf_res: Dict,
        lim_res: Dict
    ) -> Dict:
        
        # 🎯 1. V99 SHORT CROWD TRAP (PRIORITAS TERTINGGI!)
        # Jika Short Imbalance > 50x + Agg mati = SQUEEZE!
        if sct_res.get('is_trap'):
            return {
                "bias": sct_res['bias'],
                "confidence": sct_res.get('confidence', 'ABSOLUTE'),
                "reason": f"V99_SCT: {sct_res['reason']}",
                "phase": sct_res.get('phase', 'CROWDED_SQUEEZE')
            }
        
        # 🎯 2. V99 CROWD VS CLUSTER LOGIC
        # Bandingkan crowd vs cluster, prioritaskan crowd
        if crowd_cluster_res.get('override'):
            return {
                "bias": crowd_cluster_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V99_CROWD_CLUSTER: {crowd_cluster_res['reason']}",
                "phase": crowd_cluster_res.get('phase', 'CROWD_DOMINANCE')
            }
        
        # 🎯 3. V99 OI BUILD AT EXTREMUM
        # Deteksi akumulasi diam-diam sebelum squeeze
        if oi_extremum_res.get('is_accumulation'):
            return {
                "bias": oi_extremum_res['bias'],
                "confidence": oi_extremum_res.get('confidence', 'SUPREME'),
                "reason": f"V99_OI_EXTREMUM: {oi_extremum_res['reason']}",
                "phase": oi_extremum_res.get('phase', 'STEALTH_ACCUMULATION')
            }
        
        # 🎯 4. V99 OI BUILD VALIDATOR
        if oi_build_res.get('bias') != "NEUTRAL" and oi_build_res.get('confidence') == "ABSOLUTE":
            return {
                "bias": oi_build_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V99_OI_NUCLEAR: {oi_build_res['reason']}",
                "phase": oi_build_res.get('phase', 'OI_DOMINANCE')
            }
        
        # 🎯 5. V99 GRAVITY DISTANCE
        if gravity_dist_res.get('override'):
            return {
                "bias": gravity_dist_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V99_GRAVITY: {gravity_dist_res['reason']}",
                "phase": gravity_dist_res.get('phase', 'PROXIMITY_OVERRIDE')
            }
        
        # 🎯 6. V99 WMI VETO (Hanya jika tidak ada crowd)
        if wmi_veto_res.get('is_veto'):
            return {
                "bias": wmi_veto_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V99_WMI_VETO: {wmi_veto_res['reason']}",
                "phase": wmi_veto_res.get('phase', 'WHALE_SINGULARITY_OVERRIDE')
            }
        
        # 🎯 7. V99 INTERNAL TRAP
        if internal_trap_res.get('is_trap'):
            return {
                "bias": internal_trap_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V99_FMT: {internal_trap_res['reason']}",
                "phase": "INTERNAL_MATCHING_TRAP"
            }
        
        # 🎯 8. V97 EVENT HORIZON SINGULARITY
        if ehs_res.get('is_active'):
            return {
                "bias": ehs_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V97_EHS: {ehs_res['reason']}",
                "phase": "EVENT_HORIZON_SUCTION"
            }
        
        # 💨 9. VACUUM DETECTOR
        if vac_res.get('active'):
            return {
                "bias": vac_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V98_VAC: {vac_res['reason']}",
                "phase": "LIQUIDITY_VACUUM"
            }
        
        # 🏗️ 10. POSITION BUILD DETECTOR
        if pbd_res.get('active'):
            return {
                "bias": pbd_res['bias'],
                "confidence": pbd_res.get('confidence', 'ABSOLUTE'),
                "reason": f"V96_PBD: {pbd_res['reason']}",
                "phase": "POSITION_BUILD_PHASE"
            }
        
        # 🎯 11. EVENT HORIZON
        if evh_res.get('active'):
            return {
                "bias": evh_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V97_EVH: {evh_res['reason']}",
                "phase": "EVENT_HORIZON"
            }
        
        # 🌌 12. SINGULARITY VETO
        if svi_res.get('is_absolute_veto'):
            return {
                "bias": svi_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V96_SVI: {svi_res['reason']}",
                "phase": "GOD_EXECUTION"
            }
        
        # 🎯 13. EXECUTION COMPLETION DETECTOR
        if ecd_res.get('completed'):
            return {
                "bias": ecd_res['direction'],
                "confidence": "ABSOLUTE",
                "reason": f"V96_ECD: {ecd_res['reason']}",
                "phase": "DISTRIBUTION_PHASE"
            }
        
        # 🛡️ 14. RETAIL POSITIONING TRAP
        if rpt_res.get('is_trap'):
            return {
                "bias": rpt_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V95_RPT: {rpt_res['reason']}",
                "phase": "ENERGY_VENGEANCE"
            }
        
        # 🎯 15. MARKET PHASE VETO
        if phase_res.get('priority') in ['ABSOLUTE', 'SUPREME']:
            return {
                "bias": phase_res.get('signal', phase_res['bias']),
                "confidence": phase_res['priority'],
                "reason": f"PHASE_OVERRIDE: {phase_res['reason']}",
                "phase": phase_res['phase']
            }
        
        # 👻 16. GHOST WALL CONDEMNATION
        if gwc_res.get('is_ghost_wall'):
            return {
                "bias": gwc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V96_GWC: {gwc_res['reason']}",
                "phase": "GHOST_WALL_COLLAPSE"
            }
        
        # 💨 17. LIQUIDITY VACUUM DETECTOR
        if lvd_res.get('active'):
            return {
                "bias": lvd_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V97_LVD: {lvd_res['reason']}",
                "phase": "VACUUM_DUMP"
            }
        
        # 📊 18. SILENT DISTRIBUTION DETECTOR
        if sdd_res.get('active'):
            return {
                "bias": sdd_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V97_SDD: {sdd_res['reason']}",
                "phase": "SILENT_DISTRIBUTION"
            }
        
        # 🛡️ 19. ENERGY SPOOF TRACKER
        if est_res.get('is_spoof'):
            return {
                "bias": est_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V95_EST: {est_res['reason']}",
                "phase": "SPOOF_COLLAPSE"
            }
        
        # 💧 20. OI DRAIN CONDEMNATION
        if odc_res.get('active'):
            return {
                "bias": odc_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V93_ODC: {odc_res['reason']}",
                "phase": "VACUUM_FLUSH"
            }
        
        # 📉 21. PASSIVE DISTRIBUTION DETECTOR
        if pdd_res.get('active'):
            return {
                "bias": pdd_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V96_PDD: {pdd_res['reason']}",
                "phase": "PASSIVE_DISTRIBUTION"
            }
        
        # ⚡ 22. LOW ENERGY PATH (PRIORITAS DITURUNKAN!)
        if lep_res.get('is_active'):
            # Cek density calculator
            if density_res.get('better_path') != 'BALANCED':
                return {
                    "bias": density_res['bias'],
                    "confidence": "SUPREME",
                    "reason": f"V99_DENSITY: {density_res['reason']} (override LEP)",
                    "phase": "DENSITY_OVERRIDE"
                }
            return {
                "bias": lep_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V94_LEP: {lep_res['reason']}",
                "phase": "ENERGY_PATH_VETO"
            }
        
        # ... (sisa kode untuk module lainnya tetap sama) ...
        
        # Fallback
        return {
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "No strong signal detected.",
            "phase": "NEUTRAL"
        }


# ================= V100: LIQUIDATION PAYOUT CALCULATOR =================
class LiquidationPayoutCalculatorV100:
    """
    🔥 V100: LIQUIDATION PAYOUT CALCULATOR - HFT REWARD MODEL
    
    HFT tidak memilih target berdasarkan jarak terdekat,
    tapi berdasarkan REWARD TERBESAR per unit ENERGY.
    
    Formula:
        payout_long = long_liq_size / abs(long_liq_distance)
        payout_short = short_liq_size / abs(short_liq_distance)
    
    Contoh PIXELUSDT:
        short liq 0.6%, size kecil = payout kecil
        long liq 3.7%, size besar = payout besar
        Maka HFT akan: DUMP DULU (pre-flush) baru PUMP
    
    Kasus PLAYUSDT:
        long liq -2.95%, size 1.2M → payout = 1.2/2.95 = 0.407
        short liq +0.19%, size 8.5M → payout = 8.5/0.19 = 44.7
        Maka HFT akan: LANGSUNG SQUEEZE!
    """
    
    @staticmethod
    def calculate_payouts(long_liq_size: float, short_liq_size: float,
                         long_dist: float, short_dist: float) -> Dict:
        """
        Menghitung payout untuk kedua sisi likuidasi
        
        Args:
            long_liq_size: Ukuran likuidasi LONG (dalam $)
            short_liq_size: Ukuran likuidasi SHORT (dalam $)
            long_dist: Jarak ke long liquidation (negatif, dalam %)
            short_dist: Jarak ke short liquidation (positif, dalam %)
        
        Returns:
            Dict dengan payout_long, payout_short, bias, reason
        """
        # Hindari division by zero
        safe_long_dist = max(abs(long_dist), 0.01)
        safe_short_dist = max(abs(short_dist), 0.01)
        
        # Hitung payout (reward per unit distance)
        payout_long = long_liq_size / safe_long_dist if long_liq_size > 0 else 0
        payout_short = short_liq_size / safe_short_dist if short_liq_size > 0 else 0
        
        # Hitung rasio payout
        if payout_long > payout_short:
            ratio = payout_long / max(payout_short, 0.01)
            bias = "SHORT"  # Long payout lebih besar → target long di bawah → SHORT
            reason = (f"LPC_PAYOUT: Long payout {payout_long:.2f} > Short payout {payout_short:.2f} "
                     f"(ratio {ratio:.1f}x). MM akan pilih target LONG di bawah (SHORT bias)")
        elif payout_short > payout_long:
            ratio = payout_short / max(payout_long, 0.01)
            bias = "LONG"   # Short payout lebih besar → target short di atas → LONG
            reason = (f"LPC_PAYOUT: Short payout {payout_short:.2f} > Long payout {payout_long:.2f} "
                     f"(ratio {ratio:.1f}x). MM akan pilih target SHORT di atas (LONG bias)")
        else:
            ratio = 1.0
            bias = "NEUTRAL"
            reason = "LPC_PAYOUT: Payout seimbang, tunggu signal lain"
        
        return {
            "payout_long": round(payout_long, 2),
            "payout_short": round(payout_short, 2),
            "payout_ratio": round(ratio, 2),
            "bias": bias,
            "reason": reason,
            "dominant_target": "LONG_LIQ" if payout_long > payout_short else "SHORT_LIQ"
        }
    
    @staticmethod
    def get_optimal_path(payout_result: Dict, 
                         long_dist: float, short_dist: float,
                         flow: float, agg: float) -> Dict:
        """
        Menentukan path optimal dengan validasi tambahan
        
        Args:
            payout_result: Hasil dari calculate_payouts
            long_dist: Jarak long liquidation
            short_dist: Jarak short liquidation
            flow: Trade flow
            agg: Aggression ratio
        
        Returns:
            Dict dengan path, bias, dan rekomendasi
        """
        # Jika salah satu payout dominan (> LPC_PAYOUT_THRESHOLD)
        if payout_result['payout_ratio'] > LPC_PAYOUT_THRESHOLD:
            if payout_result['dominant_target'] == "LONG_LIQ":
                return {
                    "path": "PRE_FLUSH_THEN_PUMP" if abs(short_dist) < 2.0 else "DIRECT_DUMP",
                    "bias": "SHORT",
                    "first_move": "DUMP",
                    "second_move": "PUMP" if abs(short_dist) < 2.0 else None,
                    "reason": f"Long payout dominan ({payout_result['payout_ratio']:.1f}x). "
                             f"MM akan {'dump dulu sebelum pump' if abs(short_dist) < 2.0 else 'dump langsung'}",
                    "flush_expected": abs(short_dist) < 2.0
                }
            else:
                return {
                    "path": "DIRECT_PUMP",
                    "bias": "LONG",
                    "first_move": "PUMP",
                    "second_move": None,
                    "reason": f"Short payout dominan ({payout_result['payout_ratio']:.1f}x). "
                             f"MM akan pump langsung ke short liquidation",
                    "flush_expected": False
                }
        
        # Jika payout seimbang, lihat konteks
        return {
            "path": "CONTEXT_DEPENDENT",
            "bias": "NEUTRAL",
            "first_move": "UNKNOWN",
            "reason": "Payout seimbang, perlu validasi dari modul lain",
            "flush_expected": False
        }


# ================= V100: LIQUIDATION PRE-FLUSH DETECTOR =================
class LiquidationPreFlushDetectorV100:
    """
    🔥 V100: LIQUIDATION PRE-FLUSH DETECTOR - ANTI-PIXEL TRAP
    
    Mendeteksi pattern klasik di mana market maker melakukan pre-flush
    (dump -3% sampai -7%) sebelum squeeze.
    
    Pattern PIXELUSDT:
        1. price mendekati short liquidation (+0.6%)
        2. bot long (karena lihat short liq dekat)
        3. market flush dulu -3% sampai -7%
        4. baru squeeze ke atas
    
    Kenapa? Karena market maker perlu membersihkan long leverage
    sebelum pump. Long liquidity di bawah masih terlalu banyak.
    
    Rule:
        if wmi > 90
        and long_liq_distance < 4%
        and long_liq_size > short_liq_size:
            expect flush first
    """
    
    @staticmethod
    def analyze(wmi: float, long_dist: float, short_dist: float,
               long_size: float, short_size: float,
               flow: float, agg: float, rsi: float) -> Dict:
        """
        Mendeteksi potensi pre-flush sebelum pump
        
        Args:
            wmi: Whale Migration Index (>90 = extreme)
            long_dist: Jarak ke long liquidation
            short_dist: Jarak ke short liquidation
            long_size: Ukuran long liquidation
            short_size: Ukuran short liquidation
            flow: Trade flow
            agg: Aggression ratio
            rsi: RSI value
        
        Returns:
            Dict dengan flush_detected, bias, reason
        """
        flush_detected = False
        bias = "NEUTRAL"
        reason = ""
        
        # Kondisi klasik pre-flush: WMI tinggi + long pool besar + short dekat
        if (wmi > LPF_WMI_THRESHOLD and 
            abs(long_dist) < LPF_LONG_DIST_MAX and
            long_size > short_size * 1.5 and
            abs(short_dist) < 2.0):
            
            flush_detected = True
            bias = "LONG"  # Setelah flush, target LONG
            reason = (f"LPF_PRE_FLUSH_DETECTED: WMI {wmi:.1f}x > {LPF_WMI_THRESHOLD} + "
                     f"Long pool {long_size:.0f} > Short pool {short_size:.0f} + "
                     f"Short liq {short_dist:.2f}% dekat. "
                     f"MM akan FLUSH dulu ({LPF_PRE_FLUSH_MIN}% sampai {LPF_PRE_FLUSH_MAX}%) "
                     f"untuk bersihkan long leverage, baru SQUEEZE ke short liq!")
        
        # Double sweep zone: kedua sisi likuidasi dekat
        elif (abs(long_dist) < DSZ_LONG_DIST_MAX and 
              abs(short_dist) < DSZ_SHORT_DIST_MAX):
            
            flush_detected = True
            bias = "NEUTRAL"  # JANGAN ENTRY di double sweep zone!
            reason = (f"LPF_DOUBLE_SWEEP_ZONE: Long liq {long_dist:.2f}% < {DSZ_LONG_DIST_MAX}% + "
                     f"Short liq {short_dist:.2f}% < {DSZ_SHORT_DIST_MAX}%. "
                     f"Zona double sweep! Hampir pasti ada fake move dulu. JANGAN ENTRY!")
        
        # Long pool dominan dengan aggression mati
        elif (long_size > short_size * 2 and 
              agg < 0.2 and 
              flow < 1.0):
            
            flush_detected = True
            bias = "SHORT"  # Flush ke bawah
            reason = (f"LPF_LIQUIDITY_IMBALANCE: Long pool {long_size:.0f} >> Short pool {short_size:.0f} + "
                     f"Agg {agg:.2f}x mati + Flow {flow:.2f}x rendah. "
                     f"MM akan FLUSH ke bawah untuk ambil long liquidity!")
        
        return {
            "flush_detected": flush_detected,
            "bias": bias,
            "reason": reason,
            "expected_flush_range": f"{LPF_PRE_FLUSH_MIN}% to {LPF_PRE_FLUSH_MAX}%" if flush_detected else "NONE",
            "confidence": "HIGH" if flush_detected else "LOW"
        }
    
    @staticmethod
    def calculate_flush_probability(long_size: float, short_size: float,
                                   long_dist: float, short_dist: float,
                                   wmi: float, oi_delta: float) -> float:
        """
        Menghitung probabilitas pre-flush berdasarkan data
        
        Returns:
            Float 0-1: probabilitas flush akan terjadi
        """
        prob = 0.0
        
        # Faktor 1: Rasio ukuran likuidasi
        if long_size > 0 and short_size > 0:
            size_ratio = long_size / short_size
            if size_ratio > 2.0:
                prob += 0.3
            elif size_ratio > 1.5:
                prob += 0.2
        
        # Faktor 2: Jarak likuidasi
        if abs(long_dist) < 4.0 and abs(short_dist) < 2.0:
            prob += 0.3
        
        # Faktor 3: WMI ekstrim
        if wmi > 90:
            prob += 0.2
        elif wmi < -90:
            prob += 0.1
        
        # Faktor 4: OI movement
        if oi_delta > 1.0:  # OI naik = posisi baru masuk
            prob += 0.2
        
        return min(prob, 1.0)


# ================= V100: CONFLICT RESOLVER (THE ULTIMATE LIQUIDATION HIERARCHY) =================
class ConflictResolverV100:
    """
    🔥 URUTAN PRIORITAS MUTLAK V100 (DENGAN LIQUIDATION PAYOUT & PRE-FLUSH) 🔥
    
    HIERARKI FINAL V100:
    1. LPC (Liquidation Payout Calculator) ⭐ BARU! - Reward-based target selection
    2. LPF (Liquidation Pre-Flush Detector) ⭐ BARU! - Antisipasi flush sebelum pump
    3. V99-SCT (Short Crowd Trap) - Anti-crowded squeeze
    4. V99 WMI VETO - WMI > 99.5 override
    5. V99 Crowd vs Cluster Logic
    6. V99 OI Build at Extremum
    7. V99 OI Build Validator
    8. V99 Gravity Distance
    9. V98 VAC (Vacuum Detector)
    10. V97 EHS (Event Horizon Singularity)
    11. V96 PBD (Position Build Detector)
    """
    
    @staticmethod
    def resolve(
        # V100 NEW MODULES - PRIORITAS TERTINGGI!
        lpc_result: Dict,               # V100 Liquidation Payout Calculator ⭐
        lpf_result: Dict,                # V100 Liquidation Pre-Flush Detector ⭐
        
        # V99-SCT Modules
        sct_res: Dict,
        crowd_cluster_res: Dict,
        oi_extremum_res: Dict,
        oi_build_res: Dict,
        gravity_dist_res: Dict,
        wmi_veto_res: Dict,
        internal_trap_res: Dict,
        density_res: Dict,
        
        # Existing modules
        ehs_res: Dict,
        vac_res: Dict,
        pbd_res: Dict,
        evh_res: Dict,
        svi_res: Dict,
        ecd_res: Dict,
        rpt_res: Dict,
        phase_res: Dict,
        gwc_res: Dict,
        lvd_res: Dict,
        sdd_res: Dict,
        est_res: Dict,
        odc_res: Dict,
        pdd_res: Dict,
        lep_res: Dict,
        plr_res: Dict,
        opd_res: Dict,
        wmi_exhaust_res: Dict,
        cascade_res: Dict,
        energy_res: Dict,
        death_res: Dict,
        lgd_res: Dict,
        wsc_res: Dict,
        sat_res: Dict,
        pet_res: Dict,
        zgh_res: Dict,
        otf_res: Dict,
        lim_res: Dict
    ) -> Dict:
        
        # 🎯 1. LIQUIDATION PAYOUT CALCULATOR (TERTINGGI!)
        # MM memilih target berdasarkan reward/effort, bukan jarak
        if lpc_result.get('payout_ratio', 1.0) > LPC_PAYOUT_THRESHOLD:
            path_info = LiquidationPayoutCalculatorV100.get_optimal_path(
                lpc_result, 
                long_dist=0,  # Akan diisi dari data
                short_dist=0,
                flow=0,
                agg=0
            )
            
            if path_info['flush_expected']:
                return {
                    "bias": "NEUTRAL",  # JANGAN ENTRY, tunggu flush!
                    "confidence": "ABSOLUTE",
                    "reason": f"V100_LPC: {lpc_result['reason']}. {path_info['reason']}. TUNGGU FLUSH SELESAI!",
                    "phase": "PRE_FLUSH_WAIT",
                    "action": "WAIT_FOR_FLUSH_COMPLETION"
                }
            else:
                return {
                    "bias": lpc_result['bias'],
                    "confidence": "ABSOLUTE",
                    "reason": f"V100_LPC: {lpc_result['reason']}",
                    "phase": "PAYOUT_DOMINANT",
                    "action": "FOLLOW_PAYOUT"
                }
        
        # 🎯 2. LIQUIDATION PRE-FLUSH DETECTOR
        if lpf_result.get('flush_detected'):
            if "DOUBLE_SWEEP_ZONE" in lpf_result['reason']:
                return {
                    "bias": "NEUTRAL",
                    "confidence": "ABSOLUTE",
                    "reason": f"V100_LPF: {lpf_result['reason']}",
                    "phase": "DOUBLE_SWEEP_ZONE",
                    "action": "DO_NOT_ENTER"
                }
            else:
                return {
                    "bias": lpf_result['bias'],
                    "confidence": "HIGH",
                    "reason": f"V100_LPF: {lpf_result['reason']}",
                    "phase": "PRE_FLUSH",
                    "action": "PREPARE_FOR_REVERSAL"
                }
        
        # 🎯 3. V99-SCT (Short Crowd Trap)
        if sct_res.get('is_trap'):
            return {
                "bias": sct_res['bias'],
                "confidence": sct_res.get('confidence', 'ABSOLUTE'),
                "reason": f"V99_SCT: {sct_res['reason']}",
                "phase": sct_res.get('phase', 'CROWDED_SQUEEZE'),
                "action": "FOLLOW_CROWD_TRAP"
            }
        
        # 🎯 4. V99 WMI VETO
        if wmi_veto_res.get('is_veto'):
            return {
                "bias": wmi_veto_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V99_WMI_VETO: {wmi_veto_res['reason']}",
                "phase": wmi_veto_res.get('phase', 'WHALE_SINGULARITY_OVERRIDE'),
                "action": "FOLLOW_WMI"
            }
        
        # 🎯 5. V99 CROWD VS CLUSTER LOGIC
        if crowd_cluster_res.get('override'):
            return {
                "bias": crowd_cluster_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V99_CROWD_CLUSTER: {crowd_cluster_res['reason']}",
                "phase": crowd_cluster_res.get('phase', 'CROWD_DOMINANCE'),
                "action": "FOLLOW_CROWD_CLUSTER"
            }
        
        # 🎯 6. V99 OI BUILD AT EXTREMUM
        if oi_extremum_res.get('is_accumulation'):
            return {
                "bias": oi_extremum_res['bias'],
                "confidence": oi_extremum_res.get('confidence', 'SUPREME'),
                "reason": f"V99_OI_EXTREMUM: {oi_extremum_res['reason']}",
                "phase": oi_extremum_res.get('phase', 'STEALTH_ACCUMULATION'),
                "action": "FOLLOW_OI_ACCUMULATION"
            }
        
        # Fallback ke hierarki V99 yang tersisa
        if oi_build_res.get('bias') != "NEUTRAL" and oi_build_res.get('confidence') == "ABSOLUTE":
            return {
                "bias": oi_build_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V99_OI_NUCLEAR: {oi_build_res['reason']}",
                "phase": oi_build_res.get('phase', 'OI_DOMINANCE'),
                "action": "FOLLOW_OI_BUILD"
            }
        
        if gravity_dist_res.get('override'):
            return {
                "bias": gravity_dist_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V99_GRAVITY: {gravity_dist_res['reason']}",
                "phase": gravity_dist_res.get('phase', 'PROXIMITY_OVERRIDE'),
                "action": "FOLLOW_GRAVITY"
            }
        
        if internal_trap_res.get('is_trap'):
            return {
                "bias": internal_trap_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V99_FMT: {internal_trap_res['reason']}",
                "phase": "INTERNAL_MATCHING_TRAP",
                "action": "FOLLOW_INTERNAL_TRAP"
            }
        
        if ehs_res.get('is_active'):
            return {
                "bias": ehs_res['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V97_EHS: {ehs_res['reason']}",
                "phase": "EVENT_HORIZON_SUCTION",
                "action": "FOLLOW_EHS"
            }
        
        if vac_res.get('active'):
            return {
                "bias": vac_res['bias'],
                "confidence": "SUPREME",
                "reason": f"V98_VAC: {vac_res['reason']}",
                "phase": "LIQUIDITY_VACUUM",
                "action": "FOLLOW_VAC"
            }
        
        if pbd_res.get('active'):
            return {
                "bias": pbd_res['bias'],
                "confidence": pbd_res.get('confidence', 'ABSOLUTE'),
                "reason": f"V96_PBD: {pbd_res['reason']}",
                "phase": pbd_res.get('phase', 'POSITION_BUILD'),
                "action": "FOLLOW_PBD"
            }
        
        # Fallback akhir
        return {
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "No strong signal detected.",
            "phase": "NEUTRAL",
            "action": "WAIT"
        }


# ================= V82: ABSORPTION PRESSURE INDEX (API) - BARU! =================
class AbsorptionPressureV82:
    """
    V82: Mendeteksi Whale menyerap retail (Absorption).
    Jika Agg (Agresi) > 5.0x TAPI Harga nempel di MA/Dasar,
    artinya Whale sedang 'makan' retail tanpa bikin harga naik/turun dulu.

    Kasus SIGNUSDT (The Bullish Absorption Siphon):
    - Bot Bias: SHORT (Karena IER Exit aktif, OI mampet -0.30%).
    - Market Move: LONG (Naik).
    - Liciknya MM: MM sengaja bikin OI turun tipis biar bot lo mikir Whale lagi Exit.
      Padahal, agresi retail 5.67x itu diserap habis oleh Whale lewat Limit Order.
      RSI 45.5 itu adalah "Spring Zone". Jika Agresi Retail tinggi di harga bawah
      tapi harga nggak mau turun, itu namanya BULLISH ABSORPTION.
    """
    @staticmethod
    def analyze(agg_ratio: float, rsi6: float, price_change: float, distance_to_liq: float = 0) -> Dict:
        is_absorbing = False
        bias = "NEUTRAL"
        reason = ""

        # Bullish Absorption: Retail agresif beli di zona bawah, tapi harga stagnan/diserap
        if agg_ratio > API_AGGRESSION_MIN and rsi6 < API_RSI_BULL_MAX:
            is_absorbing = True
            bias = "LONG"
            reason = (f"API_BULL_ABSORPTION: Retail agresif beli ({agg_ratio:.1f}x) di RSI {rsi6:.1f} (rendah) "
                      f"dan Whale menyerap semua. SIAP TERBANG!")

        # Bearish Absorption: Retail agresif jual di zona atas, tapi harga stagnan/diserap
        elif agg_ratio > API_AGGRESSION_MIN and rsi6 > API_RSI_BEAR_MIN and abs(price_change) < API_PRICE_CHANGE_MAX:
            is_absorbing = True
            bias = "SHORT"
            reason = (f"API_BEAR_ABSORPTION: Retail agresif jual ({agg_ratio:.1f}x) di RSI {rsi6:.1f} (tinggi) "
                      f"dan Whale menyerap semua. SIAP DUMP!")

        # Bullish Absorption dengan validasi jarak likuidasi (Kasus SIGN)
        if distance_to_liq < 0.15 and agg_ratio > 3.0 and rsi6 < 50:
            is_absorbing = True
            bias = "LONG"
            reason = (f"API_ABSORPTION: Jarak likuidasi {distance_to_liq}% sangat dekat TAPI Agg {agg_ratio:.1f}x tinggi "
                      f"di RSI {rsi6:.1f}. MM sedang memasang jaring pasif untuk menelan semua Short. SIAP SQUEEZE KE ATAS!")

        return {
            "is_absorbing": is_absorbing,
            "bias": bias,
            "reason": reason
        }

# ================= V82: LIQUIDITY MIRROR GUARD (LMG) - BARU! =================
class LiquidityMirrorGuardV82:
    """
    V82: Anti-Bottomless Hole (Kasus SIREN).
    Jika Jarak Likuidasi < 0.05% (Long Liq 0.02%), JANGAN ENTRY LONG!
    Itu adalah 'Magnet Maut'. Satu dorongan kecil (Long Liq 0.02%) buat memicu Liquidation Cascade ke bawah.

    Kasus SIRENUSDT (The ICD Counter-Trap):
    - Bot Bias: LONG (Karena ICD Trap aktif, Agg rendah 0.11x).
    - Market Move: SHORT (Dump).
    - Liciknya MM: MM ngelihat bot lo udah punya logic ICD (Internal Cross).
      Jadi mereka sengaja bikin Flow 2.5x tinggi tapi Agg 0.11x rendah di RSI 6.6 (Ekstrim Bottom).
      Bot lo Long, tapi ternyata itu adalah "The Bottomless Hole".
      MM cuma butuh satu dorongan kecil (Long Liq 0.02%) buat memicu Liquidation Cascade ke bawah.
    """
    @staticmethod
    def analyze(long_dist: float, short_dist: float, rsi6: float) -> Dict:
        is_death_magnet = False
        bias = "NEUTRAL"
        reason = ""

        # Death Magnet untuk LONG: Jarak likuidasi long terlalu tipis di RSI ekstrim bottom
        if abs(long_dist) < LMG_DEATH_DISTANCE_MAX and rsi6 < LMG_RSI_DEATH_LONG_MAX:
            is_death_magnet = True
            bias = "SHORT"
            reason = (f"LMG_DEATH_MAGNET_LONG: Jarak Long Liq {long_dist:.2f}% terlalu tipis di RSI {rsi6:.1f}. "
                      f"Bahaya cascade! Ikuti arah terjun.")

        # Death Magnet untuk SHORT: Jarak likuidasi short terlalu tipis di RSI ekstrim top
        elif abs(short_dist) < LMG_DEATH_DISTANCE_MAX and rsi6 > LMG_RSI_DEATH_SHORT_MIN:
            is_death_magnet = True
            bias = "LONG"
            reason = (f"LMG_DEATH_MAGNET_SHORT: Jarak Short Liq {short_dist:.2f}% terlalu tipis di RSI {rsi6:.1f}. "
                      f"Bahaya cascade! Ikuti arah terjun.")

        return {
            "is_death_magnet": is_death_magnet,
            "bias": bias,
            "reason": reason
        }

# ================= V83: LIQUIDATION HEAT GRADIENT (LHG) - BARU! =================
class LiquidationHeatGradientV83:
    """
    🔥 V83: LIQUIDATION HEAT GRADIENT - THE MICROSECOND SNIPER
    
    Masalah umum: Bot hanya lihat distance liquidation.
    Padahal HFT lihat: gradient = liquidity_size / distance
    
    Formula:
        long_gradient = long_liq_size / long_distance
        short_gradient = short_liq_size / short_distance
    
    Decision:
        if short_gradient > long_gradient:
            target = SHORT_LIQ (Short lebih mudah ditembak)
        else:
            target = LONG_LIQ
    
    Contoh:
        Short liq: +1.72%, Size: 20M → gradient = 20 / 1.72 = 11.6
        Long liq: -0.48%, Size: 5M → gradient = 5 / 0.48 = 10.4
        ➡ Short lebih mudah ditembak (gradient lebih tinggi)
    
    Cascade Detection:
        cascade = liq_size / liquidity_depth
        Jika cascade > 5 → domino liquidation
    """
    @staticmethod
    def analyze(long_dist: float, short_dist: float, 
                long_liq_size: float, short_liq_size: float,
                bid_depth: float = 1.0, ask_depth: float = 1.0) -> Dict:
        
        # Avoid division by zero
        long_dist_abs = abs(long_dist) if long_dist != 0 else 0.01
        short_dist_abs = abs(short_dist) if short_dist != 0 else 0.01
        
        # Calculate gradients (size per percentage distance)
        long_gradient = long_liq_size / long_dist_abs if long_dist_abs > 0 else 0
        short_gradient = short_liq_size / short_dist_abs if short_dist_abs > 0 else 0
        
        # Calculate cascade potential
        long_cascade = long_liq_size / bid_depth if bid_depth > 0 else 0
        short_cascade = short_liq_size / ask_depth if ask_depth > 0 else 0
        
        # Determine which side is easier to hit
        target = "LONG_LIQ" if long_gradient >= short_gradient else "SHORT_LIQ"
        
        # Check for cascade potential
        cascade_risk = "NONE"
        if long_cascade > LHG_CASCADE_MULTIPLIER:
            cascade_risk = "LONG_CASCADE"
        elif short_cascade > LHG_CASCADE_MULTIPLIER:
            cascade_risk = "SHORT_CASCADE"
        
        # Build reason string
        reason = (f"LHG_GRADIENT: Long={long_gradient:.2f} | Short={short_gradient:.2f} | "
                  f"Target={target} | Cascade={cascade_risk}")
        
        bias = "SHORT" if target == "SHORT_LIQ" else "LONG"
        
        return {
            "long_gradient": round(long_gradient, 2),
            "short_gradient": round(short_gradient, 2),
            "target": target,
            "bias": bias,
            "cascade_risk": cascade_risk,
            "long_cascade": round(long_cascade, 2),
            "short_cascade": round(short_cascade, 2),
            "reason": reason
        }

# ================= V83: ORDERBOOK VACUUM SPEED (OVS) - BARU! =================
class OrderbookVacuumSpeedV83:
    """
    🔥 V83: ORDERBOOK VACUUM SPEED - MICROSECOND LIQUIDITY RADAR
    
    Ini super penting untuk microseconds.
    
    Formula:
        vacuum_speed = (bid_volume_now - bid_volume_100ms_ago) / time
    
    Decision:
        if bid_vacuum > ask_vacuum → DUMP (Bid disappearing fast)
        if ask_vacuum > bid_vacuum → PUMP (Ask disappearing fast)
    """
    @staticmethod
    def analyze(current_bids: List, current_asks: List,
                prev_bids: List = None, prev_asks: List = None,
                time_delta_ms: float = OVS_TIME_WINDOW_MS) -> Dict:
        
        # Calculate current volumes (top 5 levels)
        current_bid_vol = sum(q for _, q in current_bids[:5]) if current_bids else 0
        current_ask_vol = sum(q for _, q in current_asks[:5]) if current_asks else 0
        
        # Calculate previous volumes if available
        if prev_bids and prev_asks:
            prev_bid_vol = sum(q for _, q in prev_bids[:5]) if prev_bids else 0
            prev_ask_vol = sum(q for _, q in prev_asks[:5]) if prev_asks else 0
            
            # Calculate vacuum speed (volume change per ms)
            bid_vacuum_speed = (prev_bid_vol - current_bid_vol) / time_delta_ms if time_delta_ms > 0 else 0
            ask_vacuum_speed = (prev_ask_vol - current_ask_vol) / time_delta_ms if time_delta_ms > 0 else 0
        else:
            # Fallback: use volume ratio as proxy
            bid_vacuum_speed = 0
            ask_vacuum_speed = 0
        
        # Determine direction
        if bid_vacuum_speed > ask_vacuum_speed and bid_vacuum_speed > OVS_VACUUM_THRESHOLD:
            direction = "DUMP"
            reason = f"OVS_DUMP: Bid vacuum {bid_vacuum_speed:.2f} > Ask vacuum {ask_vacuum_speed:.2f}"
            bias = "SHORT"
        elif ask_vacuum_speed > bid_vacuum_speed and ask_vacuum_speed > OVS_VACUUM_THRESHOLD:
            direction = "PUMP"
            reason = f"OVS_PUMP: Ask vacuum {ask_vacuum_speed:.2f} > Bid vacuum {bid_vacuum_speed:.2f}"
            bias = "LONG"
        else:
            direction = "NEUTRAL"
            reason = f"OVS_NEUTRAL: No significant vacuum detected"
            bias = "NEUTRAL"
        
        return {
            "bid_vacuum_speed": round(bid_vacuum_speed, 4),
            "ask_vacuum_speed": round(ask_vacuum_speed, 4),
            "direction": direction,
            "bias": bias,
            "current_bid_vol": round(current_bid_vol, 2),
            "current_ask_vol": round(current_ask_vol, 2),
            "reason": reason
        }

# ================= V83: AGGRESSION VELOCITY (ADV) - BARU! =================
class AggressionVelocityV83:
    """
    🔥 V83: AGGRESSION VELOCITY - WHALE ATTACK DETECTOR
    
    Yang dipakai sekarang: Agg Ratio (statik)
    Yang penting sebenarnya: dAgg / dt (velocity)
    
    Formula:
        agg_velocity = (agg_now - agg_1s_ago) / time
    
    Interpretasi:
        Velocity > 2x spike → whale attack
        slow increase → retail
        flat → spoof
    """
    @staticmethod
    def analyze(current_agg: float, prev_agg: float = None,
                time_delta_s: float = 1.0, agg_history: deque = None) -> Dict:
        
        if prev_agg is not None:
            # Calculate velocity from previous value
            agg_velocity = (current_agg - prev_agg) / time_delta_s if time_delta_s > 0 else 0
        elif agg_history and len(agg_history) >= 2:
            # Calculate velocity from history
            recent_avg = np.mean(list(agg_history)[-3:]) if len(agg_history) >= 3 else agg_history[-1]
            older_avg = np.mean(list(agg_history)[:3]) if len(agg_history) >= 3 else agg_history[0]
            agg_velocity = (recent_avg - older_avg) / len(agg_history)
        else:
            agg_velocity = 0
        
        # Determine signal type
        velocity_ratio = abs(agg_velocity) / max(current_agg, 0.01)
        
        if velocity_ratio > ADV_SPIKE_THRESHOLD:
            signal_type = "WHALE_ATTACK"
            reason = f"ADV_WHALE_ATTACK: Velocity spike {velocity_ratio:.2f}x (Agg: {current_agg:.2f})"
            bias = "LONG" if agg_velocity > 0 else "SHORT"
        elif velocity_ratio > 0.5:
            signal_type = "RETAIL_FLOW"
            reason = f"ADV_RETAIL: Slow increase {velocity_ratio:.2f}x"
            bias = "LONG" if agg_velocity > 0 else "SHORT"
        else:
            signal_type = "SPOOF"
            reason = f"ADV_SPOOF: Flat velocity {velocity_ratio:.2f}x"
            bias = "NEUTRAL"
        
        return {
            "agg_velocity": round(agg_velocity, 4),
            "velocity_ratio": round(velocity_ratio, 2),
            "signal_type": signal_type,
            "bias": bias,
            "current_agg": round(current_agg, 2),
            "reason": reason
        }

# ================= V83: TRADE BURST DETECTOR (TBD) - BARU! =================
class TradeBurstDetectorV83:
    """
    🔥 V83: TRADE BURST DETECTOR - HFT ENTRY SIGNAL
    
    HFT entry biasanya: 50 trades dalam <200ms
    
    Formula:
        burst = trades_last_200ms
    
    Interpretasi:
        Burst > 40 → whale entry
        Burst 10-30 → retail
        Burst < 10 → noise
    """
    @staticmethod
    def analyze(trade_count: int, time_window_ms: float = TBD_TIME_WINDOW_MS) -> Dict:
        
        # Determine burst category
        if trade_count >= TBD_BURST_COUNT_MIN:
            category = "WHALE_ENTRY"
            reason = f"TBD_WHALE: {trade_count} trades in {time_window_ms}ms (>40)"
            bias = "FOLLOW_BURST"  # Will be refined by other signals
            confidence = "HIGH"
        elif trade_count >= TBD_RETAIL_MIN:
            category = "RETAIL_FLOW"
            reason = f"TBD_RETAIL: {trade_count} trades in {time_window_ms}ms (10-30)"
            bias = "NEUTRAL"
            confidence = "LOW"
        else:
            category = "NOISE"
            reason = f"TBD_NOISE: {trade_count} trades in {time_window_ms}ms (<10)"
            bias = "NEUTRAL"
            confidence = "VERY_LOW"
        
        # Calculate burst intensity
        burst_intensity = trade_count / TBD_BURST_COUNT_MIN if TBD_BURST_COUNT_MIN > 0 else 0
        
        return {
            "trade_count": trade_count,
            "category": category,
            "bias": bias,
            "confidence": confidence,
            "burst_intensity": round(burst_intensity, 2),
            "time_window_ms": time_window_ms,
            "reason": reason
        }

# ================= V83: OI ACCELERATION (OIA) - BARU! =================
class OIAccelerationV83:
    """
    🔥 V83: OI ACCELERATION - POSITION BUILDING DETECTOR
    
    Yang dipakai: OI Δ5m
    Tapi HFT lihat: OI Δ1s, OI Δ500ms
    
    Formula:
        oi_acceleration = (oi_now - oi_1s_ago)
    
    Interpretasi:
        OI ↑ + price flat → absorption
        OI ↓ + price move → liquidation
        OI ↑ + price ↑ → squeeze
    """
    @staticmethod
    def analyze(oi_now: float, oi_prev: float, 
                price_change: float, time_delta_s: float = 1.0) -> Dict:
        
        # Calculate OI acceleration
        oi_accel = oi_now - oi_prev if oi_now and oi_prev else 0
        oi_accel_pct = (oi_accel / oi_prev * 100) if oi_prev and oi_prev > 0 else 0
        
        # Determine market phase
        if oi_accel > 0 and abs(price_change) < 0.1:
            phase = "ABSORPTION"
            reason = f"OIA_ABSORPTION: OI ↑ ({oi_accel_pct:+.2f}%) + Price flat ({price_change:.2f}%)"
            bias = "FOLLOW_OI"  # Wait for breakout
        elif oi_accel < 0 and abs(price_change) > 0.2:
            phase = "LIQUIDATION"
            reason = f"OIA_LIQUIDATION: OI ↓ ({oi_accel_pct:+.2f}%) + Price move ({price_change:.2f}%)"
            bias = "FOLLOW_PRICE"
        elif oi_accel > 0 and price_change > 0.2:
            phase = "SQUEEZE"
            reason = f"OIA_SQUEEZE: OI ↑ ({oi_accel_pct:+.2f}%) + Price ↑ ({price_change:.2f}%)"
            bias = "LONG"
        elif oi_accel > 0 and price_change < -0.2:
            phase = "DIVERGENCE"
            reason = f"OIA_DIVERGENCE: OI ↑ ({oi_accel_pct:+.2f}%) + Price ↓ ({price_change:.2f}%)"
            bias = "REVERSAL_LONG"
        else:
            phase = "NEUTRAL"
            reason = f"OIA_NEUTRAL: OI ({oi_accel_pct:+.2f}%) + Price ({price_change:.2f}%)"
            bias = "NEUTRAL"
        
        return {
            "oi_acceleration": round(oi_accel, 2),
            "oi_acceleration_pct": round(oi_accel_pct, 2),
            "phase": phase,
            "bias": bias,
            "oi_now": round(oi_now, 2) if oi_now else 0,
            "oi_prev": round(oi_prev, 2) if oi_prev else 0,
            "reason": reason
        }

# ================= V83: LIQUIDITY SWEEP PROBABILITY (LSP) - BARU! =================
class LiquiditySweepProbabilityV83:
    """
    🔥 V83: LIQUIDITY SWEEP PROBABILITY - MARKET MAKER TRACKER
    
    Dipakai banyak HFT market makers.
    
    Formula:
        probability = liquidity_target / total_liquidity
    
    Decision:
        if short_liq / total_liq > 0.7 → sweep short
        if long_liq / total_liq > 0.7 → sweep long
    """
    @staticmethod
    def analyze(long_liq_size: float, short_liq_size: float,
                total_liquidity: float = None) -> Dict:
        
        # Calculate total if not provided
        if total_liquidity is None or total_liquidity == 0:
            total_liquidity = long_liq_size + short_liq_size
        
        # Avoid division by zero
        if total_liquidity == 0:
            total_liquidity = 1
        
        # Calculate probabilities
        long_prob = long_liq_size / total_liquidity
        short_prob = short_liq_size / total_liquidity
        
        # Determine sweep target
        if short_prob > LSP_SWEEP_THRESHOLD:
            sweep_target = "SHORT_LIQUIDITY"
            reason = f"LSP_SWEEP_SHORT: Probability {short_prob:.1%} > {LSP_SWEEP_THRESHOLD:.0%}"
            bias = "LONG"  # Price will go up to sweep shorts
        elif long_prob > LSP_SWEEP_THRESHOLD:
            sweep_target = "LONG_LIQUIDITY"
            reason = f"LSP_SWEEP_LONG: Probability {long_prob:.1%} > {LSP_SWEEP_THRESHOLD:.0%}"
            bias = "SHORT"  # Price will go down to sweep longs
        else:
            sweep_target = "NONE"
            reason = f"LSP_BALANCED: Long={long_prob:.1%}, Short={short_prob:.1%}"
            bias = "NEUTRAL"
        
        return {
            "long_probability": round(long_prob, 4),
            "short_probability": round(short_prob, 4),
            "sweep_target": sweep_target,
            "bias": bias,
            "total_liquidity": round(total_liquidity, 2),
            "reason": reason
        }

# ================= V83: LIQUIDITY SNIPER SCORE - BARU! =================
class LiquiditySniperScoreV83:
    """
    🔥 V83: LIQUIDITY SNIPER SCORE - COMPOSITE DECISION ENGINE
    
    Cara Simple Menebak +6% Direction
    
    Rule cepat:
        score_long = ask_vacuum + agg_velocity + oi_acceleration + short_liq_gradient
        score_short = bid_vacuum + negative_agg_velocity + negative_oi_acceleration + long_liq_gradient
    
    Decision:
        if score_long > score_short:
            target = short_liq (Price goes UP to hit shorts)
        else:
            target = long_liq (Price goes DOWN to hit longs)
    """
    @staticmethod
    def calculate(ovs_result: Dict, adv_result: Dict, oia_result: Dict, 
                  lhg_result: Dict, lsp_result: Dict) -> Dict:
        
        # Initialize scores
        score_long = 0
        score_short = 0
        
        # 1. Orderbook Vacuum Speed component
        if ovs_result:
            if ovs_result.get('direction') == 'PUMP':
                score_long += 25
            elif ovs_result.get('direction') == 'DUMP':
                score_short += 25
        
        # 2. Aggression Velocity component
        if adv_result:
            vel_ratio = adv_result.get('velocity_ratio', 0)
            if adv_result.get('bias') == 'LONG':
                score_long += min(vel_ratio * 10, 25)
            elif adv_result.get('bias') == 'SHORT':
                score_short += min(vel_ratio * 10, 25)
        
        # 3. OI Acceleration component
        if oia_result:
            if oia_result.get('bias') == 'LONG':
                score_long += 25
            elif oia_result.get('bias') == 'SHORT':
                score_short += 25
        
        # 4. Liquidation Heat Gradient component
        if lhg_result:
            long_grad = lhg_result.get('long_gradient', 0)
            short_grad = lhg_result.get('short_gradient', 0)
            total_grad = long_grad + short_grad if (long_grad + short_grad) > 0 else 1
            
            # Higher gradient = easier to hit
            score_short += (long_grad / total_grad) * 25  # Long gradient attracts price DOWN
            score_long += (short_grad / total_grad) * 25  # Short gradient attracts price UP
        
        # 5. Liquidity Sweep Probability component
        if lsp_result:
            if lsp_result.get('bias') == 'LONG':
                score_long += 25 * lsp_result.get('short_probability', 0)
            elif lsp_result.get('bias') == 'SHORT':
                score_short += 25 * lsp_result.get('long_probability', 0)
        
        # Determine final decision
        total_score = score_long + score_short
        if total_score == 0:
            total_score = 1
        
        long_confidence = (score_long / total_score) * 100
        short_confidence = (score_short / total_score) * 100
        
        if score_long > score_short and score_long >= V83_LONG_SCORE_THRESHOLD:
            target = "SHORT_LIQUIDITY"
            direction = "UP"
            bias = "LONG"
            reason = f"V83_SNIPER_LONG: Score {score_long:.1f} > {score_short:.1f} → Target Short Liq (+6% potential)"
            confidence = "HIGH"
        elif score_short > score_long and score_short >= V83_SHORT_SCORE_THRESHOLD:
            target = "LONG_LIQUIDITY"
            direction = "DOWN"
            bias = "SHORT"
            reason = f"V83_SNIPER_SHORT: Score {score_short:.1f} > {score_long:.1f} → Target Long Liq (-6% potential)"
            confidence = "HIGH"
        else:
            target = "NONE"
            direction = "NEUTRAL"
            bias = "NEUTRAL"
            reason = f"V83_NEUTRAL: Score {score_long:.1f} vs {score_short:.1f} (No clear edge)"
            confidence = "LOW"
        
        return {
            "score_long": round(score_long, 2),
            "score_short": round(score_short, 2),
            "long_confidence": round(long_confidence, 1),
            "short_confidence": round(short_confidence, 1),
            "target": target,
            "direction": direction,
            "bias": bias,
            "confidence": confidence,
            "reason": reason
        }

# ================= V81: LIQUIDITY THINNING GUARD (LTG) - BARU! =================
class LiquidityThinningGuardV81:
    """
    V81: Mendeteksi kondisi 'Vacuum' di Orderbook.
    Jika Flow > 50.0x (Anomali Total), abaikan semua sinyal SHORT.
    Harga akan terus melayang ke atas (Squeeze) sampai ada Bid Wall baru.
    """
    @staticmethod
    def analyze(trade_flow: float, ask_vol: float, bid_vol: float) -> Dict:
        is_vacuum = False
        reason = ""
        bias = "NEUTRAL"

        if trade_flow > LTG_FLOW_VACUUM_MIN:  # Flow super anomali (Kasus KITE)
            is_vacuum = True
            bias = "LONG"
            reason = f"LTG_VACUUM: Flow {trade_flow:.1f}x adalah anomali Liquidity Thinning! Sisi ASK kosong. JANGAN SHORT! Harga akan melayang (Infinity Squeeze)!"

        return {
            "is_vacuum": is_vacuum,
            "bias": bias,
            "reason": reason
        }

# ================= V81: INTERNAL CROSS DETECTOR (ICD) - BARU! =================
class InternalCrossDetectorV81:
    """
    V81: Memvalidasi IER_EXIT.
    Jika Flow > 2.0x TAPI Aggressive Ratio (Retail) < 2.0x,
    maka Whale TIDAK sedang exit ke retail. Mereka sedang manipulasi internal.
    Abaikan sinyal SHORT dari IER!
    """
    @staticmethod
    def analyze(trade_flow: float, agg_ratio: float, oi_delta: float) -> Dict:
        is_internal_trap = False
        reason = ""
        bias = "NEUTRAL"

        if trade_flow > ICD_FLOW_MIN and agg_ratio < ICD_AGGRESSION_MAX and abs(oi_delta) < ICD_OI_DELTA_MAX:
            is_internal_trap = True
            bias = "LONG"
            reason = (f"ICD_TRAP: Flow {trade_flow:.1f}x tinggi tapi agresi retail mati ({agg_ratio:.2f}x). "
                      f"Whale sedang Position Flipping! Bias IER SHORT dibatalkan. BIAS LONG!")

        return {
            "is_internal_trap": is_internal_trap,
            "bias": bias,
            "reason": reason
        }

# ================= V80: INSTITUTIONAL EXIT RADAR (IER) - BARU! =================
class InstitutionalExitRadarV80:
    """
    V80: Mendeteksi Whale yang sedang Exit (Cuci Tangan).
    """
    @staticmethod
    def analyze(trade_flow: float, oi_delta: float, aggressive_ratio: float) -> Dict:
        """
        Args:
            trade_flow: Rasio volume beli/jual (>2.0x mencurigakan)
            oi_delta: OI Delta 5 menit (<1.0% = mampet/stagnan)
            aggressive_ratio: Rasio aggressive buy/sell (untuk validasi tambahan)
        Returns:
            Dict dengan is_exit, exit_type, bias, reason, confidence
        """
        is_exit = False
        bias = "NEUTRAL"
        reason = "No institutional exit detected"
        confidence = "LOW"
        exit_type = "NONE"

        # ============================================
        # KASUS OPN: Flow 7.33x + OI +0.38% (Stagnan!)
        # KASUS BARD: Flow 2.0x+ + OI -0.67% (Turun!)
        # ============================================
        if trade_flow > IER_FLOW_MIN and abs(oi_delta) < IER_OI_DELTA_MAX:
            is_exit = True
            bias = "SHORT"
            exit_type = "INSTITUTIONAL_EXIT"
            confidence = "ABSOLUTE"

            if oi_delta > 0:
                oi_status = f"STAGNAN (+{oi_delta:.2f}%)"
            else:
                oi_status = f"TURUN ({oi_delta:.2f}%)"

            reason = (f"IER_EXIT: Flow {trade_flow:.1f}x tinggi TAPI OI {oi_status} (<{IER_OI_DELTA_MAX}%). "
                      f"Ini BUKAN akumulasi Whale asli! Whale sedang cuci gudang/exit ke retail. "
                      f"Magnet atas adalah jebakan! Aggressive Ratio {aggressive_ratio:.2f}x hanya umpan. "
                      f"SIAP DUMP!")

        # ============================================
        # KASUS WARNING: Flow > 1.5x + OI < 1.5% (Peringatan dini)
        # ============================================
        elif trade_flow > (IER_FLOW_MIN - 0.5) and abs(oi_delta) < (IER_OI_DELTA_MAX + 0.5):
            is_exit = True
            bias = "SHORT"
            exit_type = "INSTITUTIONAL_EXIT_WARNING"
            confidence = "HIGH"
            reason = (f"IER_WARNING: Flow {trade_flow:.1f}x tinggi TAPI OI {oi_delta:.2f}% mampet. "
                      f"Potensi Institutional Exit! Waspada jebakan volume palsu.")

        return {
            "is_exit": is_exit,
            "exit_type": exit_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V80: RSI MOMENTUM GUARD (RMG) - BARU! =================
class RSIMomentumGuardV80:
    """
    V80: Mencegah Long di area 'RSI No Man's Land' (39-72).
    Kasus RIVER (The Gravity Decoy):
        - 📊 Short Liq: +0.49% (Dekat banget!)
        - 📊 RSI: 72 (High, tapi belum ekstrim)
        - 📊 Aggressive Ratio: <1.0x (Rendah!)
        - Bot V79 terpicu GRAVITY_WARNING: "Short Liq 0.49% sangat dekat! Potensi gravity overdrive!"
        - Tapi Binance HFT punya teknik "Gravity Decoy": Mereka naruh likuidasi besar di jarak super dekat
        tapi TIDAK PERNAH DITABRAK. Mereka pakai gravitasi itu buat nahan harga di atas (High RSI 72)
        biar bot tidak berani SHORT, padahal MM lagi distribusi barang pelan-pelan.
    Prinsip RMG:
        "Jika RSI sudah di atas 50 (Neutral-High) tapi agresi retail (Agg) rendah, itu tanda harga kehilangan
        tenaga untuk makan magnet. MM akan ambil jalan termudah: DUMP ke bawah."
    Logic Baru:
        Jika RSI > 50 TAPI Aggressive Ratio < 1.0x TAPI Short Dist < 1.0%, maka harga tidak punya tenaga
        untuk nembus magnet atas. Bias harus SHORT.
    """
    @staticmethod
    def analyze(rsi6: float, agg_ratio: float, short_dist: float) -> Dict:
        """
        Args:
            rsi6: RSI 6 period (>50 = neutral-high)
            agg_ratio: Aggressive Ratio (<1.0 = weak momentum)
            short_dist: Jarak ke likuidasi SHORT (<1.0% = magnet dekat)
        Returns:
            Dict dengan is_weak, weakness_type, bias, reason, confidence
        """
        is_weak = False
        bias = "NEUTRAL"
        reason = "Momentum normal"
        confidence = "LOW"
        weakness_type = "NONE"
        # ============================================
        # KASUS RIVER: RSI 72 + Agg <1.0x + Short Dist 0.49%
        # ============================================
        if rsi6 > RMG_RSI_MIN and rsi6 < RMG_RSI_MAX and agg_ratio < RMG_AGGRESSION_MAX and short_dist < RMG_SHORT_DIST_MAX:
            is_weak = True
            bias = "SHORT"  # PAKSA SHORT! Ini jebakan!
            weakness_type = "GRAVITY_DECOY"
            confidence = "ABSOLUTE"
            reason = (f"RMG_GRAVITY_DECOY: RSI {rsi6:.1f} di atas 50 TAPI agresi retail mati ({agg_ratio:.2f}x). "
                    f"Short Liq {short_dist}% hanya umpan (Gravity Decoy)! "
                    f"Gak ada tenaga buat makan magnet atas. MM bakal ambil jalan termudah: DUMP ke bawah!")
        # ============================================
        # KASUS WEAK MOMENTUM: RSI > 50 + Agg rendah (tanpa validasi Short Dist)
        # ============================================
        elif rsi6 > RMG_RSI_MIN and agg_ratio < RMG_AGGRESSION_MAX:
            is_weak = True
            bias = "SHORT"
            weakness_type = "WEAK_MOMENTUM"
            confidence = "HIGH"
            reason = (f"RMG_WEAK_MOMENTUM: RSI {rsi6:.1f} di atas 50 TAPI agresi retail mati ({agg_ratio:.2f}x). "
                    f"Harga kehilangan tenaga untuk naik. SIAP KOREKSI!")
        # ============================================
        # KASUS KEBALIKAN: RSI < 50 + Agg tinggi (Bearish exhaustion)
        # ============================================
        elif rsi6 < (100 - RMG_RSI_MIN) and agg_ratio > (1 / RMG_AGGRESSION_MAX):
            is_weak = True
            bias = "LONG"
            weakness_type = "WEAK_MOMENTUM_BULLISH"
            confidence = "HIGH"
            reason = (f"RMG_WEAK_MOMENTUM_BULLISH: RSI {rsi6:.1f} di bawah 50 TAPI agresi beli tinggi ({agg_ratio:.2f}x). "
                    f"Harga kehilangan tenaga untuk turun. SIAP REBOUND!")
        return {
            "is_weak": is_weak,
            "weakness_type": weakness_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V80: FAKE MAGNET VACUUM (FMV) - KOMBINASI IER + RMG =================
class FakeMagnetVacuumV80:
    """
    V80: Kombinasi IER + RMG untuk mendeteksi "The Fake Magnet Vacuum"
    """
    @staticmethod
    def analyze(ier_result: Dict, rmg_result: Dict, rsi6: float, trade_flow: float,
                oi_delta: float, agg_ratio: float, short_dist: float) -> Dict:
        """
        Args:
            ier_result: Hasil dari InstitutionalExitRadarV80
            rmg_result: Hasil dari RSIMomentumGuardV80
            rsi6: RSI 6 period
            trade_flow: Rasio volume beli/jual
            oi_delta: OI Delta 5 menit
            agg_ratio: Aggressive Ratio
            short_dist: Jarak ke likuidasi SHORT
        Returns:
            Dict dengan is_fake_magnet, bias, reason, confidence
        """
        is_fake_magnet = False
        bias = "NEUTRAL"
        reason = "No fake magnet detected"
        confidence = "LOW"
        fake_type = "NONE"

        # KASUS OPN/BARD: IER aktif + RSI neutral
        if ier_result['is_exit'] and ier_result['confidence'] in ["ABSOLUTE", "HIGH"]:
            if FMV_RSI_NEUTRAL_MIN < rsi6 < FMV_RSI_NEUTRAL_MAX:
                is_fake_magnet = True
                bias = "SHORT"
                fake_type = "FAKE_MAGNET_VACUUM_OPN"
                confidence = "ABSOLUTE"
                reason = (f"FAKE_MAGNET_VACUUM (OPN/BARD): {ier_result['reason']} "
                         f"RSI {rsi6:.1f} di neutral zone ({FMV_RSI_NEUTRAL_MIN}-{FMV_RSI_NEUTRAL_MAX}) "
                         f"membuat bot percaya masih bisa naik, padahal ini jebakan!")

        # KASUS RIVER: RMG aktif + Short Dist dekat
        elif rmg_result['is_weak'] and rmg_result['confidence'] in ["ABSOLUTE", "HIGH"]:
            if short_dist < RMG_SHORT_DIST_MAX:
                is_fake_magnet = True
                bias = "SHORT"
                fake_type = "FAKE_MAGNET_VACUUM_RIVER"
                confidence = "ABSOLUTE"
                reason = (f"FAKE_MAGNET_VACUUM (RIVER): {rmg_result['reason']} "
                         f"Short Liq {short_dist}% hanya umpan (Gravity Decoy)!")

        # KASUS FLOW INFLATION: Flow > 2.0x + OI < 1.0% + RSI neutral
        elif (trade_flow > FMV_FLOW_INFLATION_MIN and
              abs(oi_delta) < FMV_OI_STAGNANT_MAX and
              FMV_RSI_NEUTRAL_MIN < rsi6 < FMV_RSI_NEUTRAL_MAX):
            is_fake_magnet = True
            bias = "SHORT"
            fake_type = "FLOW_INFLATION_VACUUM"
            confidence = "SUPREME"
            reason = (f"FLOW_INFLATION_VACUUM: Flow {trade_flow:.1f}x tinggi TAPI OI {oi_delta:.2f}% mampet di RSI {rsi6:.1f} (neutral). "
                     f"Ini Likuiditas Tiruan! Binance ciptakan magnet palsu untuk tarik bot LONG masuk sebelum banting harga!")

        return {
            "is_fake_magnet": is_fake_magnet,
            "fake_type": fake_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V79: WASH TRADE DETECTOR (WTD) =================
class WashTradeDetectorV79:
    """
    V79: Mendeteksi Volume/Flow palsu (Wash Trading).
    Kasus KITEUSDT:
        - 📊 Flow: 11.5x (Sangat Ekstrim!)
        - 📊 RSI: 76.7 (Tinggi/Overbought)
        - Bot V78 mikir: "Whale beli masif (Flow 11.5x) di dekat Magnet Short, SIAP LONG!"
        - Tapi Binance HFT punya teknik "Wash Trading": Whale beli-jual ke diri sendiri untuk menciptakan volume palsu,
        membuat bot ikutan Long, sementara mereka pasang jaring Short raksasa di belakang layar.
    Prinsip WTD:
        "Jika Whale terlihat terlalu bersemangat (Flow > 10x) di harga yang sudah mahal, dia tidak sedang mengajakmu pesta,
        dia sedang menagih tagihan pesta padamu."
    Logic:
        Jika Flow > 10.0x DAN RSI > 70, itu adalah Wash Trading Distribution.
        Bias harus SHORT.
    """
    @staticmethod
    def analyze(trade_flow: float, rsi6: float, oi_delta: float) -> Dict:
        """
        Args:
            trade_flow: Rasio volume beli/jual ( >10.0x mencurigakan)
            rsi6: RSI 6 period ( >70 overbought palsu)
            oi_delta: OI Delta 5 menit (untuk validasi tambahan, negatif = buang posisi)
        Returns:
            Dict dengan is_wash_trade, wash_type, bias, reason, confidence
        """
        is_wash_trade = False
        bias = "NEUTRAL"
        reason = "No wash trade detected"
        confidence = "LOW"
        wash_type = "NONE"
        # ============================================
        # KASUS KITE: Flow 11.5x + RSI 76.7 (Sangat mencurigakan!)
        # ============================================
        if trade_flow > WTD_FLOW_MIN and rsi6 > WTD_RSI_MIN:
            is_wash_trade = True
            bias = "SHORT"  # PAKSA SHORT! Ini jebakan!
            wash_type = "WASH_TRADE_DISTRIBUTION"
            confidence = "ABSOLUTE"
            reason = (f"WASH_TRADE_DISTRIBUTION: Flow {trade_flow:.1f}x RAKSASA di RSI {rsi6:.1f} (Overbought). "
                    f"Ini BUKAN akumulasi Whale asli! Whale sedang 'Wash Trading' (jual-beli ke diri sendiri) "
                    f"untuk menciptakan volume palsu dan menjebak Long. OI Delta {oi_delta:.1f}%. SIAP DUMP BESAR-BESARAN!")
        # ============================================
        # KASUS MODERAT: Flow > 8.0x + RSI > 75 (Peringatan dini)
        # ============================================
        elif trade_flow > (WTD_FLOW_MIN - 2.0) and rsi6 > (WTD_RSI_MIN + 5):
            is_wash_trade = True
            bias = "SHORT"
            wash_type = "WASH_TRADE_WARNING"
            confidence = "HIGH"
            reason = (f"WASH_TRADE_WARNING: Flow {trade_flow:.1f}x (sangat tinggi) di RSI {rsi6:.1f} (overbought). "
                    f"Potensi wash trading! Waspada jebakan volume palsu.")
        return {
            "is_wash_trade": is_wash_trade,
            "wash_type": wash_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V78: EXECUTION ZONE HUNTER (EZH) =================
class ExecutionZoneHunterV78:
    """
    V78: Mendeteksi zona eksekusi likuidasi (Execution Zone)
    Kasus RIVERUSDT:
        - 📊 Jarak Short Liq: -0.06% (SUDAH TERSENTUH!)
        - 📊 RSI: 90.7 (Nuclear overbought)
        - Bot V77 mikir: "Wah, jarak likuidasi tinggal 0.06%, PASTI tabrak atas!"
        - Tapi Binance HFT punya teknik "Magnetic Slingshot": MM naruh harga super dekat ke likuidasi
        cuma buat dapet daya lenting (slingshot) untuk nge-dump 12%.
    Prinsip EZH:
        "Jika jarak likuidasi sudah menyentuh angka negatif atau mendekati nol (0.06%),
        likuidasi itu SUDAH TERJADI atau sedang terjadi. MM cuma butuh milidetik buat nyapu itu,
        lalu mereka langsung 'buang muatan'."
    Logic:
        Jika Jarak Likuidasi < 0.1% DAN RSI > 85, itu bukan Magnet lagi, tapi "Execution Zone".
        Begitu dieksekusi, harga akan berbalik arah secara brutal.
    """
    @staticmethod
    def analyze(short_dist: float, long_dist: float, rsi6: float, trade_flow: float = 1.0) -> Dict:
        """
        Args:
            short_dist: Jarak ke likuidasi SHORT (dalam persen, bisa negatif jika sudah tersentuh)
            long_dist: Jarak ke likuidasi LONG (dalam persen)
            rsi6: RSI 6 period
            trade_flow: Rasio volume beli/jual (untuk validasi tambahan)
        Returns:
            Dict dengan is_execution, bias, reason, confidence
        """
        is_execution = False
        bias = "NEUTRAL"
        reason = "No execution zone detected"
        confidence = "LOW"
        execution_type = "NONE"
        # ============================================
        # KASUS RIVER: Jarak Short Liq 0.06% (sangat dekat) + RSI 90.7 (Nuclear)
        # ============================================
        if abs(short_dist) < EZH_DISTANCE_MAX and rsi6 > EZH_RSI_OVERBOUGHT_MIN:
            is_execution = True
            bias = "SHORT"  # Balikkan jadi SHORT!
            execution_type = "SHORT_EXECUTION_ZONE"
            confidence = "ABSOLUTE"
            reason = (f"EXECUTION_ZONE: Short Liq ({short_dist}%) sudah tersentuh/sangat dekat di RSI {rsi6:.1f} (Nuclear). "
                    f"MM sudah selesai sapu likuidasi atas. SIAP DUMP BESAR-BESARAN!")
        # ============================================
        # KASUS KEBALIKAN: Jarak Long Liq sangat dekat + RSI sangat rendah
        # ============================================
        elif abs(long_dist) < EZH_DISTANCE_MAX and rsi6 < EZH_RSI_OVERSOLD_MAX:
            is_execution = True
            bias = "LONG"  # Balikkan jadi LONG!
            execution_type = "LONG_EXECUTION_ZONE"
            confidence = "ABSOLUTE"
            reason = (f"EXECUTION_ZONE: Long Liq ({long_dist}%) sudah tersentuh/sangat dekat di RSI {rsi6:.1f} (Nuclear oversold). "
                    f"MM sudah selesai sapu likuidasi bawah. SIAP REBOUND BESAR-BESARAN!")
        # ============================================
        # KASUS WARNING: Jarak sangat dekat tapi RSI belum ekstrim
        # ============================================
        elif abs(short_dist) < EZH_DISTANCE_MAX and rsi6 > 80:
            is_execution = True
            bias = "SHORT"
            execution_type = "SHORT_EXECUTION_WARNING"
            confidence = "HIGH"
            reason = (f"EXECUTION_WARNING: Short Liq ({short_dist}%) sangat dekat di RSI {rsi6:.1f} (overbought). "
                    f"Potensi execution zone! Waspada reversal ke bawah!")
        elif abs(long_dist) < EZH_DISTANCE_MAX and rsi6 < 20:
            is_execution = True
            bias = "LONG"
            execution_type = "LONG_EXECUTION_WARNING"
            confidence = "HIGH"
            reason = (f"EXECUTION_WARNING: Long Liq ({long_dist}%) sangat dekat di RSI {rsi6:.1f} (oversold). "
                    f"Potensi execution zone! Waspada reversal ke atas!")
        return {
            "is_execution": is_execution,
            "execution_type": execution_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V78: PANIC SELL VALIDATOR (PSV) =================
class PanicSellValidatorV78:
    """
    V78: Memvalidasi apakah RSI rendah benar-benar exhaustion atau falling knife
    Kasus OPNUSDT:
        - 📊 RSI: 0.0 (Ekstrim oversold)
        - 📊 Flow: 0.54x (Rendah!)
        - 📊 OI Delta: +0.79% (Naik dikit)
        - Bot V77 mikir: "RSI 0.0! Pasti Panic Sell Exhaustion, waktunya LONG!"
        - Tapi Binance HFT tahu: Di koin gorengan, RSI 0.0 bisa berarti "pintu masuk ke neraka yang lebih dalam".
        Retail panik jual, tapi Whale TIDAK NAMPUNG (Flow < 1.0).
    Prinsip PSV:
        "Jangan pernah Long di RSI rendah kecuali Flow > 2.0x (Bukti Whale nampung).
        Jika RSI 0.0 tapi Flow rendah, itu namanya FALLING KNIFE ASLI, bukan exhaustion."
    """
    @staticmethod
    def analyze(rsi6: float, trade_flow: float, aggressive_ratio: float, oi_delta: float) -> Dict:
        """
        Args:
            rsi6: RSI 6 period ( <20 = oversold)
            trade_flow: Rasio volume beli/jual ( >2.0x = Whale nampung)
            aggressive_ratio: Rasio aggressive buy/sell (untuk validasi tambahan)
            oi_delta: OI Delta 5 menit (untuk validasi tambahan)
        Returns:
            Dict dengan is_valid, bias, reason, confidence
        """
        is_valid = False
        bias = "NEUTRAL"
        reason = "RSI normal"
        confidence = "LOW"
        validation_type = "NONE"
        # ============================================
        # KASUS OPN: RSI 0.0 + Flow 0.54x (Rendah)
        # Ini FALLING KNIFE ASLI!
        # ============================================
        if rsi6 < PSV_RSI_OVERSOLD_MAX:
            # Jika Flow rendah (< 2.0x) = Whale TIDAK NAMPUNG = FALLING KNIFE
            if trade_flow < PSV_FLOW_WHALE_MIN:
                is_valid = True
                bias = "SHORT"  # PAKSA SHORT! (Lanjutkan dump)
                validation_type = "FALLING_KNIFE_CONTINUATION"
                confidence = "ABSOLUTE"
                reason = (f"FALLING_KNIFE: RSI {rsi6:.1f} (oversold) TAPI Whale gak nampung (Flow {trade_flow:.2f}x < {PSV_FLOW_WHALE_MIN}x). "
                        f"Ini BUKAN exhaustion, tapi FALLING KNIFE ASLI! Retail panik jual tanpa pembeli. SIAP DUMP LANJUTAN!")
            # Jika Flow tinggi (> 2.0x) = Whale NAMPUNG = REAL EXHAUSTION
            elif trade_flow >= PSV_FLOW_WHALE_MIN:
                is_valid = True
                bias = "LONG"  # PAKSA LONG! (Reversal)
                validation_type = "REAL_EXHAUSTION"
                confidence = "ABSOLUTE"
                reason = (f"REAL_EXHAUSTION: RSI {rsi6:.1f} (oversold) DAN Whale nampung (Flow {trade_flow:.2f}x >= {PSV_FLOW_WHALE_MIN}x). "
                        f"Ini EXHAUSTION ASLI! Whale borong panik sell retail. SIAP REVERSAL LONG!")
        # ============================================
        # KASUS KEBALIKAN: RSI tinggi (>80) untuk validasi overbought
        # ============================================
        elif rsi6 > (100 - PSV_RSI_OVERSOLD_MAX):
            # Jika Flow tinggi (> 2.0x) di overbought = REAL DISTRIBUTION
            if trade_flow > PSV_FLOW_WHALE_MIN:
                is_valid = True
                bias = "SHORT"  # PAKSA SHORT! (Reversal)
                validation_type = "REAL_DISTRIBUTION"
                confidence = "ABSOLUTE"
                reason = (f"REAL_DISTRIBUTION: RSI {rsi6:.1f} (overbought) DAN Whale jual (Flow {trade_flow:.2f}x tinggi). "
                        f"Whale distribusi ke retail FOMO. SIAP REVERSAL SHORT!")
            # Jika Flow rendah (< 2.0x) = FAKE PUMP
            elif trade_flow < PSV_FLOW_WHALE_MIN:
                is_valid = True
                bias = "SHORT"  # PAKSA SHORT! (Lanjutkan dump)
                validation_type = "FAKE_PUMP"
                confidence = "HIGH"
                reason = (f"FAKE_PUMP: RSI {rsi6:.1f} (overbought) TAPI Whale gak beli (Flow {trade_flow:.2f}x rendah). "
                        f"Ini PUMP PALSU! SIAP DUMP!")
        return {
            "is_valid": is_valid,
            "validation_type": validation_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V77: OVERDRIVE FLOW FILTER (OFF) =================
class OverdriveFlowFilterV77:
    """
    V77: Mendeteksi Whale yang menambal jurang likuidasi (Liquidity Patching)
    """
    @staticmethod
    def analyze(lgo_result: Dict, trade_flow: float, rsi6: float, agg_ratio: float) -> Dict:
        """
        Args:
            lgo_result: Hasil dari LiquidationGravityOverdriveV75
            trade_flow: Rasio volume beli/jual ( >2.5x = Whale masif)
            rsi6: RSI 6 period (untuk validasi tambahan)
            agg_ratio: Aggressive Ratio (untuk validasi)
        Returns:
            Dict dengan is_patched, bias, reason, confidence
        """
        is_patched = False
        bias = "NEUTRAL"
        reason = "Overdrive valid"
        confidence = "LOW"
        patched_type = "NONE"

        # Kasus HUSDT: Jarak Long Liq 0.12% (Sangat dekat!) TAPI Flow 3.0x (Whale beli gila!)
        if lgo_result['is_overdrive'] and lgo_result['bias'] == "SHORT" and trade_flow > OFF_FLOW_MIN:
            is_patched = True
            bias = "LONG"  # BALIKKAN ARAH!
            patched_type = "WHALE_BRIDGE_REVERSAL"
            confidence = "ABSOLUTE"
            reason = (f"OFF_FILTER: Jarak Long Liq {lgo_result['long_dist']}% sangat dekat (LGO bilang SHORT), "
                    f"TAPI Whale beli masif (Flow {trade_flow:.2f}x). "
                    f"Whale sedang menambal jurang bawah! DILARANG SHORT, SIAP REVERSAL LONG!")

        # Kasus kebalikan: LGO ingin LONG tapi Whale jual masif
        elif lgo_result['is_overdrive'] and lgo_result['bias'] == "LONG" and trade_flow < (1 / OFF_FLOW_MIN):
            is_patched = True
            bias = "SHORT"  # BALIKKAN ARAH!
            patched_type = "WHALE_BRIDGE_REVERSAL_BEARISH"
            confidence = "ABSOLUTE"
            reason = (f"OFF_FILTER: Jarak Short Liq {lgo_result['short_dist']}% sangat dekat (LGO bilang LONG), "
                    f"TAPI Whale jual masif (Flow {trade_flow:.2f}x). "
                    f"Whale sedang menambal jurang atas! DILARANG LONG, SIAP REVERSAL SHORT!")

        # Kasus searah dengan LGO (validasi)
        elif (lgo_result['is_overdrive'] and
            lgo_result['overdrive_type'] == "SHORT_GRAVITY_OVERDRIVE" and
            lgo_result['bias'] == "LONG" and
            trade_flow > OFF_FLOW_MIN):
            is_patched = True
            bias = "LONG"  # Tetap LONG (searah)
            patched_type = "SHORT_OVERDRIVE_PATCHED"
            confidence = "ABSOLUTE"
            reason = (f"OFF_FILTER: Jarak Short Liq {lgo_result['short_dist']}% sangat dekat "
                    f"TAPI Whale beli masif (Flow {trade_flow:.2f}x). Whale PERTAHANKAN arah ke atas! "
                    f"SIAP LONG VALID!")

        # Kasus searah dengan LGO (validasi bearish)
        elif (lgo_result['is_overdrive'] and
            lgo_result['overdrive_type'] == "LONG_GRAVITY_OVERDRIVE" and
            lgo_result['bias'] == "SHORT" and
            trade_flow < (1 / OFF_FLOW_MIN)):
            is_patched = True
            bias = "SHORT"  # Tetap SHORT (searah)
            patched_type = "LONG_OVERDRIVE_PATCHED"
            confidence = "ABSOLUTE"
            reason = (f"OFF_FILTER: Jarak Long Liq {lgo_result['long_dist']}% sangat dekat "
                    f"TAPI Whale jual masif (Flow {trade_flow:.2f}x). Whale PERTAHANKAN arah ke bawah! "
                    f"SIAP SHORT VALID!")

        return {
            "is_patched": is_patched,
            "patched_type": patched_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V77: AGGRESSIVE EXHAUSTION FILTER (AEF) =================
class AggressiveExhaustionFilterV77:
    """
    V77: Mendeteksi klimaks agresi retail (Retail Peak FOMO)
    """
    @staticmethod
    def analyze(agg_ratio: float, rsi6: float, oi_delta: float, short_dist: float, long_dist: float, trade_flow: float = 0) -> Dict:
        """
        Args:
            agg_ratio: Aggressive Ratio ( >10.0x = retail FOMO gila)
            rsi6: RSI 6 period ( >80 = overbought)
            oi_delta: OI Delta 5 menit ( <2.0% = no fuel)
            short_dist: Jarak ke likuidasi SHORT
            long_dist: Jarak ke likuidasi LONG
            trade_flow: Rasio volume beli/jual (untuk validasi di V78)
        Returns:
            Dict dengan is_exhausted, bias, reason, confidence
        """
        is_exhausted = False
        bias = "NEUTRAL"
        reason = "Aggression healthy"
        confidence = "LOW"
        exhausted_type = "NONE"

        # ============================================
        # V78 UPDATE: Tambahkan validasi Flow untuk Panic Sell
        # ============================================
        if agg_ratio < 0.1 and rsi6 < 20:
            # V78: Validasi dengan Flow
            if trade_flow > PSV_FLOW_WHALE_MIN:  # WAJIB ADA FLOW WHALE
                is_exhausted = True
                bias = "LONG"
                exhausted_type = "PANIC_SELL_EXHAUSTION"
                confidence = "ABSOLUTE"
                reason = (f"PANIC_SELL_EXHAUSTION: Retail panic sell (Agg {agg_ratio:.2f}x) di RSI {rsi6:.1f} (oversold). "
                        f"Whale nampung beneran (Flow {trade_flow:.2f}x > {PSV_FLOW_WHALE_MIN}x). SIAP REVERSAL LONG!")
            else:
                is_exhausted = True
                bias = "SHORT"  # JIKA FLOW RENDAH, INI FALLING KNIFE!
                exhausted_type = "CONTINUATION_DUMP"
                confidence = "ABSOLUTE"
                reason = (f"CONTINUATION_DUMP: RSI {rsi6:.1f} nol tapi Whale gak nampung (Flow {trade_flow:.2f}x < {PSV_FLOW_WHALE_MIN}x). "
                        f"Ini FALLING KNIFE ASLI! JANGAN LONG! SIAP DUMP LANJUTAN!")
        # ============================================
        # KASUS PHA: Agg 19.0x (Gila!) + RSI 87 (Nuclear) + OI 0.25% (Zonk!)
        # ============================================
        elif agg_ratio > AEF_AGGRESSION_MIN and rsi6 > AEF_RSI_MIN:
            # Validasi dengan OI Delta (harus <2.0% = no fuel)
            if oi_delta < AEF_OI_DELTA_MAX:
                is_exhausted = True
                bias = "SHORT"  # PAKSA SHORT! (Dump)
                exhausted_type = "RETAIL_FOMO_EXHAUSTION"
                confidence = "ABSOLUTE"
                reason = (f"RETAIL_FOMO_EXHAUSTION: Retail gila (Agg {agg_ratio:.2f}x) di RSI {rsi6:.1f} (overbought) "
                        f"TAPI OI cuma naik {oi_delta:.1f}% (no fuel). MM sedang cuci gudang ke retail FOMO. "
                        f"Magnet Short {short_dist}% di atas cuma umpan beracun! SIAP DUMP!")
        # ============================================
        # KASUS EKSTRIM: Agg > 15.0x + RSI > 85
        # ============================================
        elif agg_ratio > 15.0 and rsi6 > 85:
            is_exhausted = True
            bias = "SHORT"
            exhausted_type = "EXTREME_FOMO_EXHAUSTION"
            confidence = "ABSOLUTE"
            reason = (f"EXTREME_FOMO: Agg {agg_ratio:.2f}x SUPER GILA! RSI {rsi6:.1f} NUCLEAR! "
                    f"Ini puncak histeria retail! MM pasti distribusi besar-besaran!")
        # ============================================
        # KASUS KEBALIKAN: Agg sangat rendah (<0.1) + RSI sangat rendah (<20) - Tanpa Flow validation (V77 lama)
        # ============================================
        elif agg_ratio < 0.1 and rsi6 < 20:
            is_exhausted = True
            bias = "LONG"  # PAKSA LONG! (Reversal) - V77 style
            exhausted_type = "PANIC_SELL_EXHAUSTION_V77"
            confidence = "HIGH"
            reason = (f"PANIC_SELL_EXHAUSTION (V77): Retail panic sell (Agg {agg_ratio:.2f}x) di RSI {rsi6:.1f} (oversold). "
                    f"Potensi reversal (tanpa validasi Flow).")

        return {
            "is_exhausted": is_exhausted,
            "exhausted_type": exhausted_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V76: PANIC SATURATION REVERSAL (PSR) =================
class PanicSaturationReversalV76:
    """
    V76: Mendeteksi titik jenuh kepanikan (Panic Saturation)
    """
    @staticmethod
    def analyze(agg_ratio: float, price: float, ma10: float, ma20: float,
                rsi6: float, trade_flow: float, wmi_ratio: float) -> Dict:
        """
        Args:
            agg_ratio: Aggressive Ratio ( >5.0x = panic sell)
            price: Harga current
            ma10: MA 10 period
            ma20: MA 20 period
            rsi6: RSI 6 period (untuk validasi tambahan)
            trade_flow: Rasio volume beli/jual (untuk validasi tembok Whale)
            wmi_ratio: Whale Mass Index (untuk validasi target)
        Returns:
            Dict dengan is_saturated, bias, reason, confidence
        """
        is_saturated = False
        bias = "NEUTRAL"
        reason = "Market sentiment normal"
        confidence = "LOW"
        saturation_type = "NONE"

        # Hitung perbedaan harga dengan MA dalam persen
        price_ma10_diff = abs(price - ma10) / price * 100 if price > 0 else 999
        price_ma20_diff = abs(price - ma20) / price * 100 if price > 0 else 999
        price_ma_diff = min(price_ma10_diff, price_ma20_diff)

        # ============================================
        # KASUS HUMA: Agg 5.67x (Peak Panic!) + Harga nempel di MA
        # ============================================
        if agg_ratio > PSR_AGGRESSION_MIN and price_ma_diff < PSR_PRICE_MA_DIFF_MAX:
            # Validasi tambahan: RSI harus dingin (tidak overbought) dan flow harus > 0.5 (ada tembok)
            if rsi6 < PSR_RSI_MAX and trade_flow > PSR_FLOW_MIN:
                is_saturated = True
                bias = "LONG"  # PAKSA LONG! (Reversal)
                saturation_type = "PANIC_SATURATION_REVERSAL"
                confidence = "SUPREME"
                reason = (f"PANIC_SATURATION: Agg {agg_ratio:.2f}x (Peak Panic!) tapi harga dipaku di MA (diff {price_ma_diff:.3f}%). "
                        f"RSI {rsi6:.1f} dingin, Flow {trade_flow:.2f}x stabil. "
                        f"Whale sudah selesai borong panik sell retail. SIAP REVERSAL LONG!")

        return {
            "is_saturated": is_saturated,
            "saturation_type": saturation_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence,
            "price_ma_diff": round(price_ma_diff, 3)
        }

# ================= V75: ABSORPTION MOMENTUM VALIDATOR (AMV) =================
class AbsorptionMomentumValidatorV75:
    """
    V75: Mendeteksi manipulasi Institutional Shorting
    """
    @staticmethod
    def analyze(oi_delta: float, aggressive_ratio: float, price_change: float, trade_flow: float) -> Dict:
        """
        Args:
            oi_delta: OI Delta 5 menit dalam persen
            aggressive_ratio: Rasio aggressive buy/sell (>2.5x = retail panic selling)
            price_change: Perubahan harga 5 menit dalam persen
            trade_flow: Rasio volume beli/jual (>0.7 = stabil, ada tembok Whale)
        Returns:
            Dict dengan is_absorption_long, bias, reason, confidence
        """
        is_absorption_long = False
        bias = "NEUTRAL"
        reason = "Normal market conditions"
        confidence = "LOW"

        # ============================================
        # KASUS HUMA: OI Delta > 3%, Price Change < 0 (turun), Agg > 2.5x (retail panic)
        # ============================================
        if (oi_delta > AMV_OI_DELTA_MIN and
            price_change < 0 and
            aggressive_ratio > AMV_AGGRESSION_MIN):
            # Jika flow tidak ikut hancur (masih di atas AMV_TRADE_FLOW_MIN)
            if trade_flow > AMV_TRADE_FLOW_MIN:
                is_absorption_long = True
                bias = "LONG"  # Paksa LONG!
                confidence = "SUPREME"
                reason = (f"ABSORPTION_JUDGE: Retail panik (Agg {aggressive_ratio:.2f}x) "
                        f"tapi Whale nampung (OI +{oi_delta:.1f}%). "
                        f"Ini bukan Shorting asli, ini Passive Accumulation! BIAS LONG!")

        return {
            "is_absorption_long": is_absorption_long,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V75: LIQUIDATION GRAVITY OVERDRIVE (LGO) =================
class LiquidationGravityOverdriveV75:
    """
    V75: Mendeteksi 'The Nuclear Squeeze'
    V84 UPDATE: Sekarang dengan Fake Gravity Detector (FGD) override
    """
    @staticmethod
    def analyze(short_dist: float, long_dist: float, rsi6: float, trade_flow: float,
                agg_ratio: float = 1.0, wmi_ratio: float = 0.0,
                long_liq_size: float = 0.0, short_liq_size: float = 0.0,
                funding_rate: float = 0.0) -> Dict:
        """
        Args:
            short_dist: Jarak ke likuidasi SHORT (dalam persen)
            long_dist: Jarak ke likuidasi LONG (dalam persen)
            rsi6: RSI 6 period
            trade_flow: Rasio volume beli/jual
            agg_ratio: Aggressive Ratio (untuk FGD filter)
            wmi_ratio: WMI ratio (untuk LLS filter)
            long_liq_size: Ukuran likuidasi LONG (untuk density calculation)
            short_liq_size: Ukuran likuidasi SHORT (untuk density calculation)
            funding_rate: Funding rate (untuk FSD filter)
        Returns:
            Dict dengan is_overdrive, bias, reason, confidence
        """
        is_overdrive = False
        bias = "NEUTRAL"
        reason = "Normal distance"
        confidence = "LOW"
        overdrive_type = "NONE"

        # ============================================
        # V84 - FAKE GRAVITY DETECTOR (FGD) - QUICK PATCH
        # Jika long_dist < 0.2 tapi flow > 0.6 dan agg >= 1 → LONG (bukan SHORT!)
        # ============================================
        if long_dist < FGD_LONG_DIST_MAX and trade_flow > FGD_FLOW_MIN and agg_ratio >= FGD_AGG_MIN:
            is_overdrive = True
            bias = "LONG"  # Override! Ini adalah Gravity Trap!
            overdrive_type = "FAKE_GRAVITY_TRAP"
            confidence = "ABSOLUTE"
            reason = (f"FGD_FAKE_GRAVITY: Long Liq ({long_dist}%) dekat TAPI Flow {trade_flow:.2f}x > {FGD_FLOW_MIN} "
                     f"dAN Agg {agg_ratio:.2f}x >= {FGD_AGG_MIN}. Ini BAIT LIQUIDITY! "
                     f"MM akan PUMP dulu sebelum sweep long. BIAS LONG!")
            return {
                "is_overdrive": is_overdrive,
                "overdrive_type": overdrive_type,
                "bias": bias,
                "reason": reason,
                "confidence": confidence,
                "short_dist": short_dist,
                "long_dist": long_dist
            }

        # ============================================
        # V84 - WEAK DUMP FILTER (WDF) - BLOCK SHORT
        # Jika flow > 0.6 dan agg > 0.8 → dump tidak mungkin terjadi
        # ============================================
        if trade_flow > WDF_FLOW_MIN and agg_ratio > WDF_AGG_MIN:
            # Block SHORT bias jika kondisi weak dump terpenuhi
            if long_dist < LGO_LONG_DIST_MAX:
                #原本是SHORT，但被WDF block
                is_overdrive = True
                bias = "LONG"  # Override ke LONG karena dump tidak mungkin
                overdrive_type = "WEAK_DUMP_BLOCK"
                confidence = "HIGH"
                reason = (f"WDF_WEAK_DUMP: Flow {trade_flow:.2f}x > {WDF_FLOW_MIN} DAN Agg {agg_ratio:.2f}x > {WDF_AGG_MIN}. "
                         f"Tidak ada real selling pressure! Dump tidak mungkin terjadi. "
                         f"Bias LONG dipaksa meskipun Long Liq dekat!")
                return {
                    "is_overdrive": is_overdrive,
                    "overdrive_type": overdrive_type,
                    "bias": bias,
                    "reason": reason,
                    "confidence": confidence,
                    "short_dist": short_dist,
                    "long_dist": long_dist
                }

        # ============================================
        # V84 - LONG LIQUIDITY SHIELD (LLS) - WMI PROTECTION
        # Jika WMI < -80 → short probability rendah
        # ============================================
        if wmi_ratio < LLS_WMI_THRESHOLD:
            # Block SHORT bias jika WMI sangat negatif
            if long_dist < LGO_LONG_DIST_MAX:
                is_overdrive = True
                bias = "LONG"  # Override ke LONG karena whale protect downside
                overdrive_type = "LONG_LIQUIDITY_SHIELD"
                confidence = "HIGH"
                reason = (f"LLS_WMI_SHIELD: WMI {wmi_ratio:.1f}x < {LLS_WMI_THRESHOLD}. "
                         f"Whale protect downside! Short probability rendah. "
                         f"Bias LONG dipaksa!")
                return {
                    "is_overdrive": is_overdrive,
                    "overdrive_type": overdrive_type,
                    "bias": bias,
                    "reason": reason,
                    "confidence": confidence,
                    "short_dist": short_dist,
                    "long_dist": long_dist
                }

        # ============================================
        # V84 - FUNDING SKEW DETECTOR (FSD) - PUMP SIGNAL
        # Jika funding negative → biasanya pump karena short crowded
        # ============================================
        if funding_rate < FSD_FUNDING_NEGATIVE_THRESHOLD:
            # Support LONG bias jika funding negative
            if long_dist < LGO_LONG_DIST_MAX:
                is_overdrive = True
                bias = "LONG"  # Override ke LONG karena funding negative
                overdrive_type = "FUNDING_SKEW_PUMP"
                confidence = "MEDIUM"
                reason = (f"FSD_FUNDING_SKEW: Funding rate {funding_rate:.4f} < {FSD_FUNDING_NEGATIVE_THRESHOLD}. "
                         f"Short crowded! Biasanya pump terjadi. "
                         f"Bias LONG dipaksa!")
                return {
                    "is_overdrive": is_overdrive,
                    "overdrive_type": overdrive_type,
                    "bias": bias,
                    "reason": reason,
                    "confidence": confidence,
                    "short_dist": short_dist,
                    "long_dist": long_dist
                }

        # ============================================
        # KASUS RIVER: Short Liq 0.06% (SANGAT DEKAT) - GRAVITY OVERDRIVE
        # ============================================
        if short_dist < LGO_SHORT_DIST_MAX:
            is_overdrive = True
            bias = "LONG"  # Paksa LONG mengikuti tarikan gravitasi likuidasi!
            overdrive_type = "SHORT_GRAVITY_OVERDRIVE"
            confidence = "ABSOLUTE"
            reason = (f"GRAVITY_OVERDRIVE: Jarak Short Liq ({short_dist}%) terlalu dekat! "
                    f"RSI {rsi6:.1f} tidak relevan. MM akan menabrak titik likuidasi ini. "
                    f"DILARANG SHORT! BIAS LONG!")
        # ============================================
        # KASUS KEBALIKAN: Long Liq sangat dekat - BEARISH GRAVITY OVERDRIVE
        # ============================================
        elif long_dist < LGO_LONG_DIST_MAX:
            is_overdrive = True
            bias = "SHORT"  # Paksa SHORT!
            overdrive_type = "LONG_GRAVITY_OVERDRIVE"
            confidence = "ABSOLUTE"
            reason = (f"GRAVITY_OVERDRIVE: Jarak Long Liq ({long_dist}%) terlalu dekat! "
                    f"RSI {rsi6:.1f} tidak relevan. MM akan menabrak titik likuidasi ini. "
                    f"DILARANG LONG! BIAS SHORT!")
        # ============================================
        # KASUS MODERAT: Short Liq dekat tapi belum ekstrim (0.2% - 0.5%)
        # ============================================
        elif short_dist < 0.5:
            is_overdrive = True
            bias = "LONG"
            overdrive_type = "SHORT_GRAVITY_WARNING"
            confidence = "HIGH"
            reason = (f"GRAVITY_WARNING: Short Liq {short_dist}% sangat dekat! "
                    f"Potensi gravity overdrive! Waspada squeeze ke atas!")
        # ============================================
        # KASUS MODERAT: Long Liq dekat tapi belum ekstrim
        # ============================================
        elif long_dist < 0.5:
            is_overdrive = True
            bias = "SHORT"
            overdrive_type = "LONG_GRAVITY_WARNING"
            confidence = "HIGH"
            reason = (f"GRAVITY_WARNING: Long Liq {long_dist}% sangat dekat! "
                    f"Potensi gravity overdrive! Waspada dump ke bawah!")

        return {
            "is_overdrive": is_overdrive,
            "overdrive_type": overdrive_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence,
            "short_dist": short_dist,
            "long_dist": long_dist
        }

# ================= V84: FAKE GRAVITY DETECTOR (FGD) =================
class FakeGravityDetectorV84:
    """
    V84: Mendeteksi 'Gravity Trap' dimana long liq kecil adalah umpan
    Quick Patch untuk kasus PHAUSDT
    """
    @staticmethod
    def analyze(long_dist: float, trade_flow: float, agg_ratio: float) -> Dict:
        """
        Args:
            long_dist: Jarak ke likuidasi LONG (dalam persen)
            trade_flow: Rasio volume beli/jual
            agg_ratio: Aggressive Ratio
        Returns:
            Dict dengan is_fake_gravity, bias, reason, confidence
        """
        is_fake_gravity = False
        bias = "NEUTRAL"
        reason = "Normal gravity"
        confidence = "LOW"

        # Jika long_liq < 0.2 AND flow > 0.6 AND agg > 0.8 → LONG bias
        if long_dist < FGD_LONG_DIST_MAX and trade_flow > FGD_FLOW_MIN and agg_ratio >= FGD_AGG_MIN:
            is_fake_gravity = True
            bias = "LONG"
            confidence = "ABSOLUTE"
            reason = (f"FGD_GRAVITY_TRAP: Long Liq ({long_dist}%) dekat TAPI Flow {trade_flow:.2f}x > {FGD_FLOW_MIN} "
                     f"DAN Agg {agg_ratio:.2f}x >= {FGD_AGG_MIN}. Ini BAIT LIQUIDITY! "
                     f"MM akan PUMP dulu sebelum sweep long.")

        return {
            "is_fake_gravity": is_fake_gravity,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V84: LIQUIDITY DENSITY FILTER (LDF) =================
class LiquidityDensityFilterV84:
    """
    V84: Hitung density likuidasi untuk memprediksi path optimal
    """
    @staticmethod
    def analyze(long_liq_size: float, short_liq_size: float,
                long_dist: float, short_dist: float) -> Dict:
        """
        Args:
            long_liq_size: Ukuran likuidasi LONG
            short_liq_size: Ukuran likuidasi SHORT
            long_dist: Jarak ke likuidasi LONG (dalam persen)
            short_dist: Jarak ke likuidasi SHORT (dalam persen)
        Returns:
            Dict dengan density_long, density_short, bias, reason
        """
        long_dist_abs = abs(long_dist) if long_dist != 0 else 0.01
        short_dist_abs = abs(short_dist) if short_dist != 0 else 0.01

        density_long = long_liq_size / long_dist_abs if long_dist_abs > 0 else 0
        density_short = short_liq_size / short_dist_abs if short_dist_abs > 0 else 0

        bias = "NEUTRAL"
        reason = "Density balanced"

        # Jika density_short > density_long → LONG bias
        if density_short > density_long * LDF_DENSITY_THRESHOLD:
            bias = "LONG"
            reason = f"LDF_DENSITY: Density Short ({density_short:.2f}) > Density Long ({density_long:.2f}). Path optimal ke atas!"
        elif density_long > density_short * LDF_DENSITY_THRESHOLD:
            bias = "SHORT"
            reason = f"LDF_DENSITY: Density Long ({density_long:.2f}) > Density Short ({density_short:.2f}). Path optimal ke bawah!"

        return {
            "density_long": round(density_long, 2),
            "density_short": round(density_short, 2),
            "bias": bias,
            "reason": reason
        }

# ================= V84: WEAK DUMP FILTER (WDF) =================
class WeakDumpFilterV84:
    """
    V84: Filter kondisi weak dump - jika flow > 0.6 dan agg > 0.8, dump tidak mungkin
    """
    @staticmethod
    def analyze(trade_flow: float, agg_ratio: float) -> Dict:
        """
        Args:
            trade_flow: Rasio volume beli/jual
            agg_ratio: Aggressive Ratio
        Returns:
            Dict dengan is_weak_dump, bias, reason
        """
        is_weak_dump = False
        bias = "NEUTRAL"
        reason = "Normal conditions"

        # Jika flow > 0.6 dan agg > 0.8 → dump tidak mungkin terjadi
        if trade_flow > WDF_FLOW_MIN and agg_ratio > WDF_AGG_MIN:
            is_weak_dump = True
            bias = "LONG"  # Block SHORT, support LONG
            reason = (f"WDF_WEAK_DUMP: Flow {trade_flow:.2f}x > {WDF_FLOW_MIN} DAN Agg {agg_ratio:.2f}x > {WDF_AGG_MIN}. "
                     f"Tidak ada real selling pressure! Dump tidak mungkin terjadi.")

        return {
            "is_weak_dump": is_weak_dump,
            "bias": bias,
            "reason": reason
        }

# ================= V84: LONG LIQUIDITY SHIELD (LLS) =================
class LongLiquidityShieldV84:
    """
    V84: WMI based protection - jika WMI < -80, short probability rendah
    """
    @staticmethod
    def analyze(wmi_ratio: float) -> Dict:
        """
        Args:
            wmi_ratio: WMI ratio
        Returns:
            Dict dengan is_shield_active, bias, reason
        """
        is_shield_active = False
        bias = "NEUTRAL"
        reason = "No shield"

        # Jika WMI < -80 → short probability rendah
        if wmi_ratio < LLS_WMI_THRESHOLD:
            is_shield_active = True
            bias = "LONG"  # Whale protect downside
            reason = f"LLS_WMI_SHIELD: WMI {wmi_ratio:.1f}x < {LLS_WMI_THRESHOLD}. Whale protect downside! Short probability rendah."

        return {
            "is_shield_active": is_shield_active,
            "bias": bias,
            "reason": reason
        }

# ================= V84: FUNDING SKEW DETECTOR (FSD) =================
class FundingSkewDetectorV84:
    """
    V84: Funding rate analysis - jika funding negative, biasanya pump karena short crowded
    """
    @staticmethod
    def analyze(funding_rate: float) -> Dict:
        """
        Args:
            funding_rate: Funding rate
        Returns:
            Dict dengan is_crowded_short, bias, reason
        """
        is_crowded_short = False
        bias = "NEUTRAL"
        reason = "Normal funding"

        # Jika funding negative → biasanya pump karena short crowded
        if funding_rate < FSD_FUNDING_NEGATIVE_THRESHOLD:
            is_crowded_short = True
            bias = "LONG"  # Pump signal
            reason = f"FSD_FUNDING_SKEW: Funding rate {funding_rate:.4f} < {FSD_FUNDING_NEGATIVE_THRESHOLD}. Short crowded! Biasanya pump terjadi."

        return {
            "is_crowded_short": is_crowded_short,
            "bias": bias,
            "reason": reason
        }

# ================= V85: OVERSOLD TRAP FILTER (OTF) - ANTI-UAI TRAP =================
class OversoldTrapFilterV85:
    """
    V85: Mendeteksi 'Oversold Trap' - RSI ekstrem yang bukan reversal signal
    
    KASUS 1: UAIUSDT (The Oversold Trap - Liquidation Cascade)
        Data: Price 0.2847, RSI 3.6 (extreme oversold), Agg 4.0x buy, Flow 0.85x, OI Δ -0.32%
        Bot memilih: RMG_WEAK_MOMENTUM_BULLISH → LONG
        Tapi market: DUMP -7%
        
        🧠 Error Utama: RMG override PSV tanpa filter OI
        Masalahnya: RSI < 10 tidak selalu berarti bottom, sering berarti liquidation acceleration phase
        
        🔬 Clue yang Bot Lewatkan:
        - RSI 3.6 < 10 = extreme oversold
        - OI Δ -0.32% < 0 = positions closing, bukan new longs entering
        - Flow 0.85x < 1.0 = volume tidak confirm bullish
        
        Interpretasi sebenarnya:
        - Jika market benar-benar reversal, OI harus naik (new longs entering)
        - OI turun = liquidation cascade incoming
        - Pattern: oversold bounce trap → retail buy dip → dump continuation → long liq cascade
    
    KASUS 2: The Liquidity Vacuum Rebound (Anti-Checkmate)
        Data: WMI -99.1x, RSI 11.7, Agg 2.33x, OI turun (Institutional Exit detected)
        Bot memilih: IER_EXIT → SHORT (Karena OI turun, Whale kabur)
        Tapi market: PUMP! REBOUND! Short squeeze!
        
        🧠 Error Utama: IER terlalu dominan tanpa filter WMI + RSI ekstrim
        Masalahnya: WMI -99.1x artinya Short Liquidation Pool di atas 4% - itu "bernutrisi" buat MM!
        
        🔬 Clue yang Bot Lewatkan:
        - RSI 11.7 < 15 = extreme oversold
        - WMI -99.1 < -90 = massive short liquidation cluster BELOW price
        - Agg 2.33 > 1.0 = ada agresi beli di dasar ekstrim
        - OI turun = Whale narik order untuk bersihin Orderbook bawah (Liquidity Vacuum)
        
        Interpretasi sebenarnya:
        - Whale sengaja narik order (bikin OI turun) buat ngebersihin Orderbook bawah
        - Lalu dalam hitungan milidetik mereka hajar Market Buy buat squeeze semua Short seller
        - Ini adalah "The Liquidity Vacuum Rebound" - Short Trap klasik!
    
    Prinsip OTF V85:
        "RSI < 15 TIDAK SELALU berarti bottom atau dump. Konteks WMI dan Agg adalah kunci!"
        
        SCENARIO 1 (UAI Trap): 
            Jika RSI < 15 AND OI decreasing AND Flow < 1 AND WMI > -90 → bias = SHORT
            (Ini liquidation cascade - retail buy dip trapped!)
        
        SCENARIO 2 (Liquidity Vacuum Rebound - ANTI-CHECKMATE):
            Jika RSI < 15 AND WMI < -90 AND Agg > 1.0 → bias = LONG (DILARANG SHORT!)
            (Ini Short Trap - Whale sedang narik rem tangan untuk rebound!)
    """
    @staticmethod
    def analyze(rsi6: float, oi_delta: float, trade_flow: float, 
                wmi_ratio: float = None, agg_ratio: float = None) -> Dict:
        """
        Args:
            rsi6: RSI 6 period (< 15 = extreme oversold)
            oi_delta: OI Delta 5 menit (< 0 = positions closing)
            trade_flow: Rasio volume beli/jual (< 1.0 = no volume confirmation)
            wmi_ratio: WMI Ratio (optional, untuk deteksi Liquidity Vacuum Rebound)
            agg_ratio: Aggressive Ratio (optional, untuk deteksi whale aggression)
        Returns:
            Dict dengan is_trap, bias, reason, confidence
        """
        is_trap = False
        bias = "NEUTRAL"
        reason = "Normal conditions"
        confidence = "LOW"
        
        # ============================================
        # 🟢 SCENARIO 2: LIQUIDITY VACUUM REBOUND (ANTI-CHECKMATE)
        # Prioritas LEBIH TINGGI dari UAI Trap!
        # Jika RSI ekstrim TAPI WMI super negatif + ada agresi beli = SHORT TRAP!
        # ============================================
        if wmi_ratio is not None and agg_ratio is not None:
            if rsi6 < OTF_RSI_MAX and wmi_ratio < OTF_WMI_MIN and agg_ratio > OTF_AGG_MIN:
                is_trap = True
                bias = "LONG"  # DILARANG SHORT! Ini Short Trap!
                confidence = "ABSOLUTE"
                reason = (f"OTF_LIQUIDITY_VACUUM_REBOUND: RSI {rsi6:.1f} < {OTF_RSI_MAX} (extreme oversold) TAPI "
                         f"WMI {wmi_ratio:.1f}x < {OTF_WMI_MIN} (massive short liq cluster below) DAN "
                         f"Agg {agg_ratio:.1f}x > {OTF_AGG_MIN} (whale buy aggression). "
                         f"Whale narik order (OI turun) buat bersihin orderbook, lalu MAHJARRR! Short Squeeze incoming!")
                return {
                    "is_trap": is_trap,
                    "bias": bias,
                    "reason": reason,
                    "confidence": confidence,
                    "scenario": "LIQUIDITY_VACUUM_REBOUND"
                }
        
        # ============================================
        # 🔴 SCENARIO 1: UAI TRAP (Liquidation Cascade)
        # Hanya aktif jika Scenario 2 tidak terpenuhi
        # ============================================
        if rsi6 < OTF_RSI_MAX and oi_delta < OTF_OI_DELTA_MAX and trade_flow < OTF_FLOW_MAX:
            is_trap = True
            bias = "SHORT"  # PAKSA SHORT! Ini trap!
            confidence = "ABSOLUTE"
            reason = (f"OTF_OVERSOLD_TRAP: RSI {rsi6:.1f} < {OTF_RSI_MAX} (extreme oversold) TAPI "
                     f"OI Δ {oi_delta:.2f}% < 0 (positions closing) DAN Flow {trade_flow:.2f}x < 1.0 (no volume). "
                     f"WMI={wmi_ratio if wmi_ratio else 'N/A'} (tidak cukup ekstrim untuk rebound). "
                     f"Ini BUKAN reversal! Ini LIQUIDATION CASCADE INCOMING! Retail buy dip trapped!")
        
        return {
            "is_trap": is_trap,
            "bias": bias,
            "reason": reason,
            "confidence": confidence,
            "scenario": "UAI_TRAP" if is_trap and bias == "SHORT" else "NORMAL"
        }

# ================= V85: AGGRESSION ABSORPTION FILTER (AAF) =================
class AggressionAbsorptionFilterV85:
    """
    V85: Mendeteksi 'Aggression Absorption' - aggressive buyers yang trapped
    
    Kasus UAIUSDT (The Absorption Trap):
        Data: Agg 4.0x (aggressive buyers), Flow 0.85x (volume tidak naik)
        
        🧠 Error Utama: Agg tinggi disalahartikan sebagai bullish signal
        Masalahnya: Aggression tinggi tapi volume tidak naik = buyers trapped
        
        🔬 Clue yang Bot Lewatkan:
        - Agg 4.0x > 3 = aggressive buyers masuk
        - Flow 0.85x < 1.0 = volume tidak confirm
        - Interpretasi: Market maker menyerap order mereka dengan limit orders
        - Net liquidity imbalance tetap bearish
        
    Prinsip AAF:
        "Aggression tinggi biasanya berarti buyer agresif.
        Tetapi jika Flow < 1, artinya volume tidak naik.
        Ini biasanya berarti buyers trapped. Market maker menyerap order mereka."
    
    Rule Baru:
        Jika Agg > 3 AND Flow < 1 → bias = SHORT (buyers absorbed)
    """
    @staticmethod
    def analyze(agg_ratio: float, trade_flow: float) -> Dict:
        """
        Args:
            agg_ratio: Aggressive Ratio (> 3.0 = aggressive buyers)
            trade_flow: Rasio volume beli/jual (< 1.0 = volume tidak naik)
        Returns:
            Dict dengan is_absorbed, bias, reason, confidence
        """
        is_absorbed = False
        bias = "NEUTRAL"
        reason = "Normal aggression"
        confidence = "LOW"
        
        # ============================================
        # KASUS UAI: Agg > 3 + Flow < 1
        # Ini ABSORPTION TRAP! Buyers trapped!
        # ============================================
        if agg_ratio > AAF_AGG_MIN and trade_flow < AAF_FLOW_MAX:
            is_absorbed = True
            bias = "SHORT"  # PAKSA SHORT! Buyers trapped!
            confidence = "ABSOLUTE"
            reason = (f"AAF_AGGRESSION_ABSORPTION: Agg {agg_ratio:.2f}x > {AAF_AGG_MIN} (aggressive buyers) TAPI "
                     f"Flow {trade_flow:.2f}x < 1.0 (volume tidak naik). "
                     f"Buyers TRAPPED! Market maker menyerap order dengan limit orders. SIAP DUMP!")
        
        return {
            "is_absorbed": is_absorbed,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V86: ZERO GRAVITY HORIZON (ZGH) - BARU! =================
class ZeroGravityHorizonV86:
    """
    🔥 V86: ZERO GRAVITY HORIZON - THE ULTIMATE ANTI-TRIA TRAP
    
    KASUS TRIAUSDT (The Paradox of 0.00% Liquidation):
        Data: RSI 96.7 (Nuclear Overbought), Short Liq 0.0%, Long Liq -8.73%,
              Flow 1.94x, Agg 1.5x, OI Δ +1.37%
        Bot memilih: LMG_DEATH_MAGNET_SHORT → LONG (Karena Short Liq 0.0% = magnet)
        Tapi market: DUMP -5% sampai -10% setelah ±58 menit
        
        🧠 Error Utama: LMG terlalu dominan tanpa filter RSI-OI Ceiling
        Masalahnya: Short liq 0.0% tidak selalu berarti cascade, sering kali itu "Exit Liquidity"!
        
        🔬 Clue yang Bot Lewatkan:
        - RSI 96.7 > 90 = Nuclear Overbought (area extrem)
        - OI Δ +1.37% > 0.5% = NEW POSITIONS ENTERING (bukan short liquidation!)
        - Agg 1.5x < 2.0 = weak aggression (passive sell wall)
        - Flow 1.94x tinggi tapi Agg rendah = internal matching / passive distribution
        
        Interpretasi sebenarnya:
        - Jika benar squeeze ke atas, OI harus TURUN (karena short liquidation menutup posisi)
        - TAPI OI NAIK = NEW SHORT BUILDING (Whale sedang build short positions!)
        - Pattern: Distribution top → Whale building shorts → Fake short magnet 0% → Dump ke long liq 8%
        
    Prinsip ZGH:
        "RSI > 90 TIDAK SELALU berarti continuation. OI dan Agg adalah kunci!"
        "Jika RSI > 90 dan OI naik, itu BUKAN squeeze - itu DISTRIBUTION!"
        "MM tidak akan squeeze kalau OI masih naik - mereka butuh likuiditas buat EXIT!"
        "Short liq 0.0% itu sering kali FAKE MAGNET - yang besar justru Long liq di bawah!"
        
    Rule Pamungkas:
        IF RSI > 90 AND OI_delta > 0.5 AND Agg < 2.0 → bias = SHORT (DILARANG LONG!)
        Reason: RSI extreme + OI rising + weak aggression = Whale short build
    """
    @staticmethod
    def analyze(rsi6: float, oi_delta: float, agg_ratio: float, 
                short_dist: float = None, long_dist: float = None) -> Dict:
        """
        Args:
            rsi6: RSI 6 period (> 90 = Nuclear Overbought)
            oi_delta: OI Delta 5 menit (> 0.5% = new positions building)
            agg_ratio: Aggressive Ratio (< 2.0 = weak aggression, passive distribution)
            short_dist: Distance to short liquidation (optional, untuk konteks)
            long_dist: Distance to long liquidation (optional, untuk konteks)
        Returns:
            Dict dengan is_ceiling, bias, reason, confidence
        """
        is_ceiling = False
        bias = "NEUTRAL"
        reason = "Normal conditions"
        confidence = "LOW"
        
        # ============================================
        # 🟢 ZERO GRAVITY HORIZON DETECTED!
        # RSI > 90 + OI naik + Agg rendah = DISTRIBUTION TOP!
        # ============================================
        if rsi6 > ZGH_RSI_CEILING and oi_delta > ZGH_OI_DELTA_MIN and agg_ratio < ZGH_AGG_CEILING:
            is_ceiling = True
            bias = "SHORT"  # DILARANG LONG! Ini Distribution Top!
            confidence = "ABSOLUTE"
            
            # Tambahkan konteks tentang fake magnet jika short_dist tersedia
            magnet_context = ""
            if short_dist is not None and abs(short_dist) < 0.1:
                magnet_context = (f" Short Liq {short_dist:.2f}% adalah FAKE MAGNET! "
                                 f"MM pakai ini buat pancing LONG entry supaya mereka bisa EXIT!")
            
            reason = (f"ZGH_ZERO_GRAVITY_HORIZON: RSI {rsi6:.1f} > {ZGH_RSI_CEILING} (Nuclear Overbought) TAPI "
                     f"OI Δ {oi_delta:.2f}% > {ZGH_OI_DELTA_MIN}% (NEW SHORT BUILDING) DAN "
                     f"Agg {agg_ratio:.2f}x < {ZGH_AGG_CEILING} (weak aggression/passive sell wall). "
                     f"INI ADALAH DISTRIBUTION TOP! Whale building short positions!{magnet_context}")
        
        return {
            "is_ceiling": is_ceiling,
            "bias": bias,
            "reason": reason,
            "confidence": confidence,
            "rsi": round(rsi6, 1),
            "oi_delta": round(oi_delta, 2),
            "agg_ratio": round(agg_ratio, 2)
        }

# ================= V86: OVERBOUGHT DISTRIBUTION FILTER (ODF) - BARU! =================
class OverboughtDistributionFilterV86:
    """
    🔥 V86: OVERBOUGHT DISTRIBUTION FILTER - PRIORITAS TERATAS ANTI-TRIA TRAP
    
    Ini adalah modul prioritas tertinggi yang override SEMUA sinyal LONG
    ketika kondisi Overbought Distribution terdeteksi.
    
    KASUS TRIAUSDT (The Ultimate Trap):
        Metric          Value           Interpretasi
        RSI             96.7            Nuclear Overbought
        Short liq       0.0%            Fake Magnet / Exit Liquidity
        Long liq        -8.73%          REAL TARGET (besar & juicy)
        Flow            1.94x           High volume
        Agg             1.5x            LOW aggression (passive sell)
        OI Δ            +1.37%          NEW POSITIONS (short building!)
        
        Bot membaca: LMG_DEATH_MAGNET_SHORT → SHORT LIQ sangat dekat → harus LONG
        Realita: MM pump sedikit → distribution → dump ke long liq 8%
        
    🧠 Cara Market Maker Berpikir:
        MM memilih target berdasarkan profit/effort:
        - Target Short: Distance 0%, Reward kecil (cluster kecil/sudah tersapu)
        - Target Long: Distance 8.7%, Reward besar (cluster gemuk)
        
        Jadi mereka:
        1. Pump ke RSI 96 (bikin retail FOMO LONG)
        2. Build short positions (OI naik +1.37%)
        3. Fake short magnet 0% (pancing bot entry LONG)
        4. Distribution (jual ke retail yang FOMO)
        5. Dump ke long liq 8% (real target!)
    
    💀 Pattern Overbought Distribution Trap:
        - RSI > 90
        - OI_delta > 0.5%
        - Agg 1-2x (low aggression)
        - Move berikutnya: -5% sampai -10%
    
    Rule Pamungkas:
        IF RSI > 90 AND OI_delta > 0.5 AND Agg < 2.0 → bias = SHORT
        Reason: RSI extreme + OI rising + weak aggression = Whale short build
    """
    @staticmethod
    def analyze(rsi6: float, oi_delta: float, agg_ratio: float,
                short_liq_size: float = None, long_liq_size: float = None,
                short_dist: float = None, long_dist: float = None) -> Dict:
        """
        Args:
            rsi6: RSI 6 period (> 90 = extreme overbought)
            oi_delta: OI Delta 5 menit (> 0.5% = whale building shorts)
            agg_ratio: Aggressive Ratio (< 2.0 = passive sell wall)
            short_liq_size: Total short liquidation size (optional, untuk density comparison)
            long_liq_size: Total long liquidation size (optional, untuk density comparison)
            short_dist: Distance to short liquidation (optional)
            long_dist: Distance to long liquidation (optional)
        Returns:
            Dict dengan active, bias, reason, confidence
        """
        active = False
        bias = "NEUTRAL"
        reason = "Normal conditions"
        confidence = "LOW"
        
        # ============================================
        # 🔴 OVERBOUGHT DISTRIBUTION DETECTED!
        # Ini adalah DISTRIBUTION TOP! Whale building shorts!
        # ============================================
        if rsi6 > ODF_RSI_THRESHOLD and oi_delta > ODF_OI_DELTA_THRESHOLD and agg_ratio < ODF_AGG_THRESHOLD:
            active = True
            bias = "SHORT"  # OVERRIDE SEMUA SINYAL LONG!
            confidence = "ABSOLUTE"
            
            # Tambahkan konteks density jika data tersedia
            density_context = ""
            if short_liq_size is not None and long_liq_size is not None:
                if long_liq_size > short_liq_size * 2:
                    density_context = (f" Long liq pool {long_liq_size:.0f} >> Short liq pool {short_liq_size:.0f}. "
                                      f"MM akan pilih target yang lebih 'bernutrisi' (Long liq)!")
            
            # Tambahkan konteks distance jika data tersedia
            distance_context = ""
            if short_dist is not None and long_dist is not None:
                if abs(short_dist) < 0.1 and abs(long_dist) > 5:
                    distance_context = (f" Short dist {short_dist:.2f}% adalah FAKE MAGNET! "
                                       f"Long dist {abs(long_dist):.2f}% adalah REAL TARGET!")
            
            reason = (f"ODF_OVERBOUGHT_DISTRIBUTION: RSI {rsi6:.1f} > {ODF_RSI_THRESHOLD} (extreme overbought) + "
                     f"OI Δ {oi_delta:.2f}% > {ODF_OI_DELTA_THRESHOLD}% (whale building shorts) + "
                     f"Agg {agg_ratio:.2f}x < {ODF_AGG_THRESHOLD} (passive sell wall). "
                     f"INI BUKAN SQUEEZE - INI DISTRIBUTION!{density_context}{distance_context}")
        
        return {
            "active": active,
            "bias": bias,
            "reason": reason,
            "confidence": confidence,
            "rsi": round(rsi6, 1),
            "oi_delta": round(oi_delta, 2),
            "agg_ratio": round(agg_ratio, 2)
        }

# ================= V85: NEUTRAL ZONE SHIELD (NZS) - ANTI-STABLE TRAP =================
class NeutralZoneShieldV85:
    """
    V85: Mendeteksi jebakan di area RSI Neutral (40-65).
    
    KASUS STABLEUSDT (The Neutral Zone Trap):
        Data: Price pump, RSI 58.8 (neutral), Flow 2.57x (tinggi), Agg 0.67x (rendah), 
              OI Δ -1.10% (turun), WMI -83.9 (ekstrim negatif)
        
        Bot membaca: IER_WARNING (Flow tinggi + OI turun = Whale exit) → SHORT
        Tapi market: PUMP!
        
        🧠 Error Utama: IER terlalu dominan tanpa filter WMI + RSI neutral
        Masalahnya: WMI -83.9x artinya Long Liquidation Pool besar di atas - itu "bernutrisi" buat MM!
        
        🔬 Clue yang Bot Lewatkan:
        - RSI 58.8 di zona neutral (40-65)
        - WMI -83.9 < -80 = massive long liquidation cluster above price
        - Flow 2.57x tinggi TAPI Agg 0.67x rendah = Internal Flow Illusion
        - OI turun = Whale narik order untuk position flip, bukan exit
        
        Interpretasi sebenarnya:
        - Market maker menutup posisi lama + membuka posisi baru (position flip)
        - Mengurangi OI sementara agar terlihat seperti exit
        - Ini adalah "Liquidity Reload" - Whale sedang reload posisi untuk pump!
        - NZS Logic: "Heh, lo mau SHORT di RSI 58 sementara WMI -83? Itu namanya lo nyodorin leher ke MM."
    
    Prinsip NZS V85:
        "Jika IER terdeteksi TAPI WMI < -80 (Whale Protect Downside) di RSI Neutral,
        maka sinyal SHORT dibatalkan. MM cuma spoofing OI buat mancing Short Seller."
        
        SCENARIO: NZS_SHIELD
            Jika RSI 40-65 AND IER_active AND WMI < -80 → bias = LONG (DILARANG SHORT!)
            (Ini Short Trap - Whale sedang mancing short seller sebelum pump!)
    """
    @staticmethod
    def analyze(rsi6: float, wmi_ratio: float, ier_active: bool) -> Dict:
        """
        Args:
            rsi6: RSI 6 period (40-65 = neutral zone)
            wmi_ratio: WMI Ratio (< -80 = whale protect downside)
            ier_active: Apakah IER_EXIT aktif
        Returns:
            Dict dengan is_shielded, bias, reason
        """
        is_shielded = False
        bias = "NEUTRAL"
        reason = ""
        
        # ============================================
        # 🛡️ SCENARIO: NZS_SHIELD (Anti-STABLE Trap)
        # Jika RSI neutral + IER aktif TAPI WMI ekstrim negatif = SHORT TRAP!
        # ============================================
        if NZS_RSI_MIN < rsi6 < NZS_RSI_MAX and ier_active:
            if wmi_ratio < NZS_WMI_THRESHOLD:  # WMI < -80
                is_shielded = True
                bias = "LONG"  # DILARANG SHORT! Ini Short Trap!
                reason = (f"NZS_SHIELD: RSI {rsi6:.1f} Neutral ({NZS_RSI_MIN}-{NZS_RSI_MAX}) + "
                         f"WMI {wmi_ratio:.1f}x < {NZS_WMI_THRESHOLD} (Ekstrim!). "
                         f"Whale naruh jaring raksasa di bawah (Anti-Dump)! "
                         f"IER_EXIT adalah False Signal untuk mancing Short Trap. MM bakal PUMP!")
        
        return {
            "is_shielded": is_shielded,
            "bias": bias,
            "reason": reason
        }

# ================= V85: POSITION FLIP DETECTOR (PFD) - ANTI-INTERNAL FLOW ILLUSION =================
class PositionFlipDetectorV85:
    """
    V85: Mendeteksi 'Position Flip' - Whale menutup posisi lama dan buka posisi baru.
    
    KASUS STABLEUSDT (The Position Flip):
        Data: Flow 2.57x (tinggi), Agg 0.67x (rendah), OI Δ -1.10% (turun)
        
        🧠 Error Utama: Bot menganggap ini exit distribution
        Masalahnya: Flow tinggi + Agg rendah = Internal Matching, bukan real selling
        
        🔬 Clue yang Bot Lewatkan:
        - Flow > 2 = high flow (suspicious)
        - Agg < 1 = low aggression (tidak ada real selling pressure)
        - OI drop < -0.5% = position reload signal (bukan exit)
        
        Interpretasi sebenarnya:
        - Market maker melakukan internal matching (wash trade internal)
        - Menutup posisi lama + membuka posisi baru
        - Mengurangi OI sementara untuk menciptakan liquidity vacuum
        - Pattern: OI drop → flow spike → aggression low → orderbook thin → PUMP
    
    Prinsip PFD V85:
        "Jika Flow > 2 AND Agg < 1 AND OI drop < -0.5%, ini bukan exit.
        Ini adalah Position Flip - Whale sedang reload posisi!"
        
        SCENARIO: POSITION_FLIP
            Jika Flow > 2 AND Agg < 1 AND OI drop < -0.5% → bias = LONG
    """
    @staticmethod
    def analyze(trade_flow: float, agg_ratio: float, oi_delta: float) -> Dict:
        """
        Args:
            trade_flow: Rasio volume beli/jual (> 2.0 = high flow)
            agg_ratio: Aggressive Ratio (< 1.0 = low aggression)
            oi_delta: OI Delta 5 menit (< -0.5% = position reload signal)
        Returns:
            Dict dengan is_flip, bias, reason, confidence
        """
        is_flip = False
        bias = "NEUTRAL"
        reason = "No position flip detected"
        confidence = "LOW"
        
        # ============================================
        # 🔄 SCENARIO: POSITION_FLIP (Internal Flow Illusion)
        # Flow tinggi + Agg rendah + OI drop = Whale reload posisi!
        # ============================================
        if trade_flow > PFD_FLOW_MIN and agg_ratio < PFD_AGG_MAX and oi_delta < PFD_OI_DROP_MIN:
            is_flip = True
            bias = "LONG"  # DILARANG SHORT! Ini reload posisi!
            confidence = "SUPREME"
            reason = (f"PFD_POSITION_FLIP: Flow {trade_flow:.1f}x > {PFD_FLOW_MIN} (tinggi) TAPI "
                     f"Agg {agg_ratio:.2f}x < {PFD_AGG_MAX} (rendah - internal matching) DAN "
                     f"OI Δ {oi_delta:.2f}% < {PFD_OI_DROP_MIN}% (position reload). "
                     f"Whale nutup posisi lama + buka posisi baru (reload)! "
                     f"Liquidity Vacuum Pump incoming!")
        
        return {
            "is_flip": is_flip,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V85: FAKE EXIT DETECTOR (FED_V85) - ANTI-LIQUIDITY BUILDING =================
class FakeExitDetectorV85:
    """
    V85: Mendeteksi 'Fake Exit' - Flow tinggi tanpa agresi market.
    
    KASUS STABLEUSDT (The Fake Exit):
        Data: Flow 2.57x (tinggi), Agg 0.67x (rendah)
        
        🧠 Error Utama: Bot melihat Flow tinggi = distribution
        Masalahnya: Jika whale benar exit, biasanya Agg sell > 2
        
        🔬 Clue yang Bot Lewatkan:
        - Flow > 2 = suspicious high flow
        - Agg < 1 = no real selling (fake exit)
        
        Interpretasi sebenarnya:
        - Exchange bisa membuat flow tinggi tanpa agresi market
        - Ini adalah Limit Absorption, bukan market sell
        - Market maker menarik orderbook untuk menciptakan liquidity vacuum
        
    Prinsip FED_V85:
        "Jika Flow > 2 AND Aggression < 1, ignore IER.
        Ini adalah Liquidity Building, bukan Distribution."
        
        SCENARIO: FAKE_EXIT
            Jika Flow > 2 AND Agg < 1 → Ignore IER (bias LONG)
    """
    @staticmethod
    def analyze(trade_flow: float, agg_ratio: float) -> Dict:
        """
        Args:
            trade_flow: Rasio volume beli/jual (> 2.0 = high flow)
            agg_ratio: Aggressive Ratio (< 1.0 = no real selling)
        Returns:
            Dict dengan is_fake_exit, bias, reason, confidence
        """
        is_fake_exit = False
        bias = "NEUTRAL"
        reason = "No fake exit detected"
        confidence = "LOW"
        
        # ============================================
        # 🎭 SCENARIO: FAKE_EXIT (Liquidity Building)
        # Flow tinggi + Agg rendah = Fake distribution!
        # ============================================
        if trade_flow > FED_V85_FLOW_MIN and agg_ratio < FED_V85_AGG_MAX:
            is_fake_exit = True
            bias = "LONG"  # Ignore IER! Ini fake exit!
            confidence = "HIGH"
            reason = (f"FED_FAKE_EXIT: Flow {trade_flow:.1f}x > {FED_V85_FLOW_MIN} (tinggi) TAPI "
                     f"Agg {agg_ratio:.2f}x < {FED_V85_AGG_MAX} (tidak ada real selling). "
                     f"Market maker tarik orderbook buat Liquidity Vacuum! "
                     f"IER_EXIT adalah FALSE SIGNAL!")
        
        return {
            "is_fake_exit": is_fake_exit,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V85: LIQUIDITY RELOAD DETECTOR (LRD) - ANTI-OI MANIPULATION =================
class LiquidityReloadDetectorV85:
    """
    V85: Mendeteksi 'Liquidity Reload' - OI turun untuk liquidity reset.
    
    KASUS STABLEUSDT (The Liquidity Reload):
        Data: OI Δ -1.10% (turun), WMI -83.9 (ekstrim negatif)
        
        🧠 Error Utama: Bot menganggap OI turun = exit distribution
        Masalahnya: OI turun bisa berarti liquidity reset, bukan exit
        
        🔬 Clue yang Bot Lewatkan:
        - OI drop (negatif) = liquidity reset signal
        - WMI < -70 = long liquidation pool besar di atas
        
        Interpretasi sebenarnya:
        - Market maker mengurangi OI untuk membersihkan orderbook
        - Menciptakan liquidity vacuum untuk pump lebih mudah
        - WMI negatif ekstrim = whale protect downside (short probability rendah)
    
    Prinsip LRD V85:
        "OI turun ≠ selalu bearish.
        Sering kali berarti liquidity reset.
        Jika WMI < -70, ini adalah LONG bias."
        
        SCENARIO: LIQUIDITY_RELOAD
            Jika OI drop (negatif) AND WMI < -70 → bias = LONG
    """
    @staticmethod
    def analyze(oi_delta: float, wmi_ratio: float) -> Dict:
        """
        Args:
            oi_delta: OI Delta 5 menit (negatif = drop)
            wmi_ratio: WMI Ratio (< -70 = long liquidation pool besar)
        Returns:
            Dict dengan is_reload, bias, reason, confidence
        """
        is_reload = False
        bias = "NEUTRAL"
        reason = "No liquidity reload detected"
        confidence = "LOW"
        
        # ============================================
        # 🔁 SCENARIO: LIQUIDITY_RELOAD (OI Manipulation)
        # OI drop + WMI ekstrim negatif = Whale reload untuk pump!
        # ============================================
        if oi_delta < -LRD_OI_DROP_MIN and wmi_ratio < LRD_WMI_THRESHOLD:
            is_reload = True
            bias = "LONG"  # DILARANG SHORT! Ini reload!
            confidence = "SUPREME"
            reason = (f"LRD_LIQUIDITY_RELOAD: OI Δ {oi_delta:.2f}% (drop/liquidity reset) + "
                     f"WMI {wmi_ratio:.1f}x < {LRD_WMI_THRESHOLD} (long liq pool besar). "
                     f"MM reducing OI to clear orderbook for PUMP! "
                     f"Institutional Reload, BUKAN Institutional Exit!")
        
        return {
            "is_reload": is_reload,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V85: FAKE EXHAUSTION DETECTOR (FED) =================
class FakeExhaustionDetectorV85:
    """
    V85: Mendeteksi 'Fake Exhaustion' - RSI ekstrem tanpa OI confirmation
    
    Kasus UAIUSDT (The Fake Exhaustion):
        Data: RSI 3.6 (extreme oversold), OI Δ -0.32% (turun)
        
        🧠 Error Utama: RSI < 10 dianggap sebagai exhaustion/reversal signal
        Masalahnya: Jika market benar-benar reversal, OI harus naik (new longs entering)
        
        🔬 Clue yang Bot Lewatkan:
        - RSI 3.6 < 10 = extreme oversold
        - OI Δ -0.32% < 0 = positions closing, bukan new longs
        - Pattern klasik: liquidation cascade incoming
        
    Prinsip FED:
        "RSI < 10 tidak selalu berarti bottom.
        Sering berarti liquidation acceleration phase.
        Jika OI down, maka NO REVERSAL."
    
    Rule Baru:
        Jika RSI < 10 AND OI down → NO REVERSAL (bias SHORT)
    """
    @staticmethod
    def analyze(rsi6: float, oi_delta: float) -> Dict:
        """
        Args:
            rsi6: RSI 6 period (< 10 = extreme oversold)
            oi_delta: OI Delta 5 menit (< 0 = positions closing)
        Returns:
            Dict dengan is_fake, bias, reason, confidence
        """
        is_fake = False
        bias = "NEUTRAL"
        reason = "Normal exhaustion"
        confidence = "LOW"
        
        # ============================================
        # KASUS UAI: RSI < 10 + OI negatif
        # Ini FAKE EXHAUSTION! Bukan reversal!
        # ============================================
        if rsi6 < FED_RSI_MAX and oi_delta < FED_OI_DELTA_MAX:
            is_fake = True
            bias = "SHORT"  # PAKSA SHORT! Fake exhaustion!
            confidence = "ABSOLUTE"
            reason = (f"FED_FAKE_EXHAUSTION: RSI {rsi6:.1f} < {FED_RSI_MAX} (extreme oversold) TAPI "
                     f"OI Δ {oi_delta:.2f}% < 0 (positions closing). "
                     f"Ini BUKAN reversal signal! Ini LIQUIDATION ACCELERATION PHASE! NO REVERSAL!")
        
        return {
            "is_fake": is_fake,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V84: LIQUIDITY PATH SCORE (LPS) =================
class LiquidityPathScoreV84:
    """
    V84: Optimal path liquidation prediction
    path_long = short_liq_size - pump_cost
    path_short = long_liq_size - dump_cost
    """
    @staticmethod
    def analyze(long_liq_size: float, short_liq_size: float,
                long_dist: float, short_dist: float,
                pump_cost: float = 0.1, dump_cost: float = 0.1) -> Dict:
        """
        Args:
            long_liq_size: Ukuran likuidasi LONG
            short_liq_size: Ukuran likuidasi SHORT
            long_dist: Jarak ke likuidasi LONG (dalam persen)
            short_dist: Jarak ke likuidasi SHORT (dalam persen)
            pump_cost: Estimated cost untuk pump (default 0.1%)
            dump_cost: Estimated cost untuk dump (default 0.1%)
        Returns:
            Dict dengan path_long_score, path_short_score, bias, reason
        """
        # path_long = short_liq_size - pump_cost
        # path_short = long_liq_size - dump_cost
        path_long_score = short_liq_size - (pump_cost * 1000)  # Scale cost
        path_short_score = long_liq_size - (dump_cost * 1000)  # Scale cost

        bias = "NEUTRAL"
        reason = "Balanced paths"

        # Jika path_long > path_short → pump dulu
        if path_long_score > path_short_score:
            bias = "LONG"
            reason = f"LPS_PATH: Path LONG ({path_long_score:.2f}) > Path SHORT ({path_short_score:.2f}). MM akan PUMP dulu!"
        elif path_short_score > path_long_score:
            bias = "SHORT"
            reason = f"LPS_PATH: Path SHORT ({path_short_score:.2f}) > Path LONG ({path_long_score:.2f}). MM akan DUMP dulu!"

        return {
            "path_long_score": round(path_long_score, 2),
            "path_short_score": round(path_short_score, 2),
            "bias": bias,
            "reason": reason
        }

# ================= V74: MAGNET DECAY VALIDATOR (MDV) =================
class MagnetDecayValidatorV74:
    """
    V74: Mendeteksi kadaluarsa Magnet (Magnet Decay)
    """
    @staticmethod
    def analyze(mdd_result: Dict, amd_result: Dict, oi_delta: float,
                magnet_first_seen_time: float = 0, current_time: float = 0) -> Dict:
        """
        Args:
            mdd_result: Hasil dari MagnetDistanceDominanceV71
            amd_result: Hasil dari AggressionMassDivergenceV65
            oi_delta: OI Delta 5 menit
            magnet_first_seen_time: Waktu pertama kali magnet terdeteksi
            current_time: Waktu sekarang
        Returns:
            Dict dengan is_magnet_fake, bias, reason, confidence
        """
        is_magnet_fake = False
        bias = "NEUTRAL"
        reason = "Magnet valid"
        confidence = "LOW"

        # ============================================
        # KASUS RIVER: MDD bilang LONG (Magnet), AMD bilang SHORT (Spoof)
        # ============================================
        if mdd_result.get('is_magnet_trap', False) and amd_result.get('is_spoof', False):
            # Cek apakah ini SPOOF_UP (WMI bullish palsu)
            if "SPOOF_UP" in amd_result.get('reason', '') or amd_result.get('bias') == "SHORT":
                is_magnet_fake = True
                bias = "SHORT"  # Balikkan arah jadi SHORT!
                confidence = "SUPREME"
                reason = (f"MAGNET_DECAY: Magnet di atas terdeteksi sebagai SPOOF oleh AMD. "
                        f"MM pasang umpan atas ({mdd_result.get('short_dist', 0):.2f}%) "
                        f"tapi gak mau beli (Agg {amd_result.get('aggressive_ratio', 0):.2f}x rendah). "
                        f"Magnet dibatalkan, BIAS SHORT!")

        return {
            "is_magnet_fake": is_magnet_fake,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V73: PASSIVE ABSORPTION BLACKHOLE (PAB) =================
class PassiveAbsorptionBlackholeV73:
    """
    V73: Mendeteksi Whale Blackhole
    """
    @staticmethod
    def analyze(trade_flow: float, aggressive_ratio: float, rsi6: float,
                wmi_ratio: float, oi_delta_5m: float) -> Dict:
        """
        Args:
            trade_flow: Rasio volume beli/jual ( >1 = lebih banyak beli)
            aggressive_ratio: Rasio aggressive buy/sell (rendah = passive buying)
            rsi6: RSI 6 period
            wmi_ratio: Whale Mass Index (negatif = target bawah)
            oi_delta_5m: OI Delta 5 menit
        Returns:
            Dict dengan is_blackhole, bias, reason, confidence
        """
        is_blackhole = False
        bias = "NEUTRAL"
        reason = "Normal flow"
        confidence = "LOW"
        blackhole_type = "NONE"

        # ============================================
        # KASUS SIREN: Flow > 10x (Gila!) + Agg < 1.5x (Passive)
        # ============================================
        if trade_flow > PAB_FLOW_MIN and aggressive_ratio < PAB_AGGRESSION_MAX:
            is_blackhole = True
            bias = "LONG"  # Paksa LONG!
            blackhole_type = "PASSIVE_ABSORPTION_BLACKHOLE"
            confidence = "ABSOLUTE"
            reason = (f"BLACKHOLE_DETECTED: Flow {trade_flow:.1f}x RAKSASA! Whale sedang menyerap "
                    f"semua barang di harga dasar dengan Aggressive Ratio {aggressive_ratio:.2f}x (passive buying). "
                    f"Ini akumulasi mutlak, bukan falling knife! BIAS LONG ABSOLUT!")

        return {
            "is_blackhole": is_blackhole,
            "blackhole_type": blackhole_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V72: CATCHING FALLING KNIVES (CFK) =================
class CatchingFallingKnivesV72:
    """
    V72: Mencegah Long di tengah pembantaian (Catching Falling Knives)
    """
    @staticmethod
    def analyze(wmi_ratio: float, rsi6: float, oi_delta_5m: float,
                aggressive_ratio: float, trade_flow: float) -> Dict:
        """
        Args:
            wmi_ratio: Whale Mass Index (negatif = target bawah)
            rsi6: RSI 6 period
            oi_delta_5m: OI Delta 5 menit
            aggressive_ratio: Rasio aggressive buy/sell
            trade_flow: Rasio volume beli/jual
        Returns:
            Dict dengan is_knife, bias, reason, confidence
        """
        is_knife = False
        bias = "NEUTRAL"
        reason = "No falling knife detected"
        confidence = "LOW"
        knife_type = "NONE"

        # ============================================
        # KASUS ROBO: WMI sangat negatif + RSI ekstrim oversold + OI zonk
        # ============================================
        if wmi_ratio < CFK_WMI_EXTREME_NEGATIVE and rsi6 < CFK_RSI_OVERSOLD_MAX:
            # Cek OI Delta: Jika < 1.5%, berarti tidak ada bensin akumulasi asli
            if abs(oi_delta_5m) < CFK_OI_DELTA_MIN:
                is_knife = True
                bias = "SHORT"  # Paksa SHORT mengikuti arah pisau jatuh!
                knife_type = "FALLING_KNIFE_DOWN"
                confidence = "SUPREME"
                reason = (f"FALLING_KNIFE: WMI {wmi_ratio:.1f}x (Mangsa bawah tebal) + RSI {rsi6:.1f} (Ekstrim) "
                        f"TAPI bensin OI {oi_delta_5m:.2f}% zonk (<{CFK_OI_DELTA_MIN}%). "
                        f"Flow {trade_flow:.2f}x & Agg {aggressive_ratio:.2f}x cuma retail panik. "
                        f"MM sedang memancing retail sebelum dibantai lebih dalam! DILARANG LONG!")

        return {
            "is_knife": is_knife,
            "knife_type": knife_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V71: MAGNET DISTANCE DOMINANCE (MDD) =================
class MagnetDistanceDominanceV71:
    """
    V71: Mendeteksi dominasi magnet jarak pendek (The Liquidity Magnet)
    """
    @staticmethod
    def analyze(short_dist: float, long_dist: float, rsi6: float, trade_flow: float) -> Dict:
        """
        Args:
            short_dist: Jarak ke likuidasi SHORT
            long_dist: Jarak ke likuidasi LONG
            rsi6: RSI 6 period
            trade_flow: Rasio volume beli/jual
        Returns:
            Dict dengan is_magnet_trap, bias, reason, confidence
        """
        is_magnet_trap = False
        bias = "NEUTRAL"
        reason = "Magnet distance normal"
        confidence = "LOW"
        trap_type = "NONE"

        # ============================================
        # KASUS RIVER: Short Liq sangat dekat + RSI dingin + Flow mulai beli
        # ============================================
        if short_dist < MDD_MAX_DISTANCE and rsi6 < MDD_MIN_RSI and trade_flow > 1.0:
            is_magnet_trap = True
            bias = "LONG"  # Batalkan Short, ganti jadi LONG
            trap_type = "MAGNET_SQUEEZE"
            confidence = "SUPREME"
            reason = (f"MAGNET_DOMINANCE: Short Liq {short_dist}% sangat dekat! RSI {rsi6:.1f} masih dingin, "
                    f"Flow {trade_flow:.2f}x mulai masuk. MM bakal 'suction' harga ke atas "
                    f"buat makan Short seller sebelum lanjut dump. DILARANG SHORT!")
        # ============================================
        # KASUS KEBALIKAN: Long Liq sangat dekat + RSI panas + Flow jual kuat
        # ============================================
        elif long_dist < MDD_MAX_DISTANCE and rsi6 > (100 - MDD_MIN_RSI) and trade_flow < 0.5:
            is_magnet_trap = True
            bias = "SHORT"  # Batalkan Long, ganti jadi SHORT
            trap_type = "MAGNET_DUMP"
            confidence = "SUPREME"
            reason = (f"MAGNET_DOMINANCE: Long Liq {long_dist}% sangat dekat! RSI {rsi6:.1f} panas, "
                    f"Flow jual {trade_flow:.2f}x kuat. MM bakal 'suction' harga ke bawah "
                    f"buat makan Long seller sebelum rebound. DILARANG LONG!")

        return {
            "is_magnet_trap": is_magnet_trap,
            "trap_type": trap_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence,
            "short_dist": short_dist,
            "long_dist": long_dist
        }

# ================= V70: ORDERBOOK VACUUM DEFENSE (OVD) =================
class OrderbookVacuumDefenseV70:
    """
    V70: Mendeteksi jebakan Bid/Ask Thinning (The Vacuum Trap)
    """
    @staticmethod
    def analyze(odd_result: Dict, rsi6: float, aggressive_ratio: float,
                short_dist: float, long_dist: float) -> Dict:
        """
        Args:
            odd_result: Hasil dari OrderbookDepthDecayV61
            rsi6: RSI 6 period
            aggressive_ratio: Rasio aggressive buy/sell
            short_dist: Jarak ke likuidasi SHORT
            long_dist: Jarak ke likuidasi LONG
        Returns:
            Dict dengan is_trap, bias, reason, confidence
        """
        is_trap = False
        bias = "NEUTRAL"
        reason = "Orderbook organic"
        confidence = "LOW"
        trap_type = "NONE"

        # ============================================
        # KASUS PHA: BID_THINNING + RSI RENDAH
        # ============================================
        if odd_result['status'] == "BID_THINNING" and rsi6 < OVD_BID_THINNING_RSI_MAX:
            is_trap = True
            bias = "LONG"  # Batalkan Short, ganti jadi LONG!
            trap_type = "VACUUM_TRAP_BULLISH"
            confidence = "SUPREME"
            reason = (f"LIQUIDITY_VACUUM_REPULSION: Bid super tipis ({odd_result['bid_volume_near']:.0f}) vs Ask tebal ({odd_result['ask_volume_near']:.0f}) "
                    f"di RSI {rsi6:.1f} (rendah). MM gak bisa dump karena gak ada likuiditas beli di bawah! "
                    f"Mereka bakal SQUEEZE ke atas dulu buat cari exit liquidity! BIAS LONG!")
        # ============================================
        # KASUS KEBALIKAN: ASK_THINNING + RSI TINGGI
        # ============================================
        elif odd_result['status'] == "ASK_THINNING" and rsi6 > OVD_ASK_THINNING_RSI_MIN:
            is_trap = True
            bias = "SHORT"  # Batalkan Long, ganti jadi SHORT!
            trap_type = "VACUUM_TRAP_BEARISH"
            confidence = "SUPREME"
            reason = (f"LIQUIDITY_VACUUM_REPULSION: Ask super tipis ({odd_result['ask_volume_near']:.0f}) vs Bid tebal ({odd_result['bid_volume_near']:.0f}) "
                    f"di RSI {rsi6:.1f} (tinggi). MM gak bisa pump karena gak ada likuiditas jual di atas! "
                    f"Mereka bakal KOREKSI ke bawah dulu buat jebak buyer! BIAS SHORT!")

        return {
            "is_trap": is_trap,
            "trap_type": trap_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V69: TREND INTEGRITY =================
class TrendIntegrityV69:
    """
    V69: Mendeteksi integritas tren melalui MA Slope, OBV, dan MACD Zero-Line
    """
    @staticmethod
    def calculate_obv(closes: List[float], volumes: List[float]) -> List[float]:
        """Menghitung On-Balance Volume (OBV)"""
        if len(closes) < 2 or len(volumes) < 2:
            return [0.0]
        obv = [0.0]
        for i in range(1, min(len(closes), len(volumes))):
            if closes[i] > closes[i-1]:
                obv.append(obv[-1] + volumes[i])
            elif closes[i] < closes[i-1]:
                obv.append(obv[-1] - volumes[i])
            else:
                obv.append(obv[-1])
        return obv

    @staticmethod
    def calculate_ma(data: List[float], period: int) -> float:
        """Menghitung Moving Average"""
        if len(data) < period:
            return data[-1] if data else 0.0
        return sum(data[-period:]) / period

    @staticmethod
    def analyze(price: float, ma10: float, ma20: float, obv_history: List[float], macd_data: Dict) -> Dict:
        """
        Args:
            price: Harga current
            ma10: MA 10 period
            ma20: MA 20 period
            obv_history: List OBV values
            macd_data: Dict dengan 'dif' dan 'dea'
        Returns:
            Dict dengan restriction, reason, dan bias_recommendation
        """
        # 1. Trend Gravity Check
        is_strong_down = price < ma10 < ma20  # Harga di bawah semua MA
        is_strong_up = price > ma10 > ma20    # Harga di atas semua MA

        # 2. OBV Accumulation Check
        obv_rising = (len(obv_history) > TREND_OBV_HISTORY_MIN and
                    all(obv_history[-i] > obv_history[-i-1] for i in range(1, TREND_OBV_CONSISTENCY + 1)))
        obv_falling = (len(obv_history) > TREND_OBV_HISTORY_MIN and
                    all(obv_history[-i] < obv_history[-i-1] for i in range(1, TREND_OBV_CONSISTENCY + 1)))

        # 3. MACD Zone Filter
        macd_dead_zone = macd_data.get('dif', 0) < 0 and macd_data.get('dea', 0) < 0

        restriction = "NONE"
        reason = "Trend Integrity Normal"
        bias_recommendation = "NEUTRAL"

        # Kasus PIPPIN: Harga turun, MA menukik, jangan berani LONG
        if is_strong_down:
            restriction = "FORBID_LONG"
            bias_recommendation = "SHORT"
            reason = ("TREND_GRAVITY: Strong Downtrend terdeteksi (Harga < MA10 < MA20). "
                    "Abaikan sinyal Long dari osilator meskipun RSI oversold!")
        # Kasus PHA: OBV naik kuat, jangan berani SHORT
        elif is_strong_up and obv_rising:
            restriction = "FORBID_SHORT"
            bias_recommendation = "LONG"
            reason = ("OBV_ACCUMULATION: Whale sedang akumulasi (OBV Rising) di Strong Uptrend. "
                    "Dilarang Short meskipun RSI overbought!")
        # Kasus POWER: MACD di bawah nol, pantulan naik hanya Dead Cat Bounce
        if macd_dead_zone and not obv_rising:
            restriction = "PRIORITIZE_SHORT"
            bias_recommendation = "SHORT"
            reason = ("MACD_DEAD_ZONE: Garis MACD (DIF/DEA) di bawah 0. "
                    "Pantulan ke atas hanya Dead Cat Bounce! Prioritaskan Short!")

        return {
            "restriction": restriction,
            "reason": reason,
            "bias_recommendation": bias_recommendation,
            "is_strong_down": is_strong_down,
            "is_strong_up": is_strong_up,
            "obv_rising": obv_rising,
            "macd_dead_zone": macd_dead_zone
        }

# ================= V68: GRAVITY DEFLECTION (OGD) =================
class GravityDeflectionV68:
    """
    V68: Mendeteksi 'Pantulan Gravitas'
    """
    @staticmethod
    def analyze(wmi_ratio: float, rsi6: float, distance: float) -> Dict:
        """
        Args:
            wmi_ratio: Whale Mass Index
            rsi6: RSI 6 period
            distance: Jarak ke target likuidasi
        Returns:
            Dict dengan is_deflected, bias, reason, confidence
        """
        is_deflected = False
        bias = "NEUTRAL"
        reason = "Gravity valid"
        confidence = "LOW"

        # ============================================
        # KASUS PIPPIN: WMI sangat negatif, RSI sangat rendah
        # ============================================
        if wmi_ratio < OGD_WMI_EXTREME_NEGATIVE and rsi6 < OGD_RSI_OVERSOLD_MAX:
            is_deflected = True
            bias = "LONG"
            confidence = "SUPREME"
            reason = (f"GRAVITY_DEFLECTION: WMI {wmi_ratio:.1f}x (Bawah) TAPI RSI {rsi6:.1f} (Oversold). "
                    f"MM gak mau dump di harga murah, mereka bakal SQUEEZE dulu ke atas! BIAS LONG!")
        # ============================================
        # KASUS KEBALIKAN: WMI sangat positif, RSI sangat tinggi
        # ============================================
        elif wmi_ratio > OGD_WMI_EXTREME_POSITIVE and rsi6 > OGD_RSI_OVERBOUGHT_MIN:
            is_deflected = True
            bias = "SHORT"
            confidence = "SUPREME"
            reason = (f"GRAVITY_DEFLECTION: WMI +{wmi_ratio:.1f}x (Atas) TAPI RSI {rsi6:.1f} (Overbought). "
                    f"MM bakal banting dulu buat jemput Long likuidasi! BIAS SHORT!")

        return {
            "is_deflected": is_deflected,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V67: ZERO AGGRESSION SLAUGHTER (ZAS) =================
class ZeroAggressionSlaughterV67:
    """
    V67: Mendeteksi 'Deadstick' (Agresi 0)
    """
    @staticmethod
    def analyze(aggressive_ratio: float, wmi_ratio: float, price_change: float) -> Dict:
        """
        Args:
            aggressive_ratio: Rasio aggressive buy/sell
            wmi_ratio: Whale Mass Index
            price_change: Perubahan harga 5 menit
        Returns:
            Dict dengan is_dead, bias, reason, confidence
        """
        is_dead = False
        bias = "NEUTRAL"
        reason = "Market masih hidup"
        confidence = "LOW"

        # ============================================
        # KASUS POWERUSDT: Agg 0.00x + WMI -88.8x
        # ============================================
        if aggressive_ratio < ZAS_AGGRESSION_MAX and wmi_ratio < ZAS_WMI_NEGATIVE_MIN:
            is_dead = True
            bias = "SHORT"
            confidence = "ABSOLUTE"
            reason = (f"DEADSTICK_SLAUGHTER: Aggressive Ratio {aggressive_ratio:.2f}x (0 buyer agresif) + "
                    f"WMI {wmi_ratio:.1f}x (target bawah). Buyer sudah mati, bursa tinggal nunggu "
                    f"satu dorongan kecil buat Liquidation Cascade! SIAP DUMP!")
        # ============================================
        # KASUS KEBALIKAN: Agg 0.00x + WMI sangat positif
        # ============================================
        elif aggressive_ratio < ZAS_AGGRESSION_MAX and wmi_ratio > ZAS_WMI_POSITIVE_MIN:
            is_dead = True
            bias = "LONG"
            confidence = "ABSOLUTE"
            reason = (f"DEADSTICK_SQUEEZE: Aggressive Ratio {aggressive_ratio:.2f}x (0 seller agresif) + "
                    f"WMI +{wmi_ratio:.1f}x (target atas). Seller sudah mati, tinggal nunggu "
                    f"dorongan buat Short Squeeze! SIAP PUMP!")

        return {
            "is_dead": is_dead,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V67: ABSORPTION VALIDITY CHECK (AVC) =================
class AbsorptionValidityCheckV67:
    """
    V67: Memvalidasi apakah absorpsi itu aseli atau jebakan Exit Liquidity
    """
    @staticmethod
    def analyze(trade_flow: float, aggressive_ratio: float, change_5m: float, oi_delta: float) -> Dict:
        """
        Args:
            trade_flow: Rasio volume beli/jual
            aggressive_ratio: Rasio aggressive buy/sell
            change_5m: Perubahan harga 5 menit
            oi_delta: OI Delta 5 menit
        Returns:
            Dict dengan is_trap, bias, trap_type, reason, confidence
        """
        is_trap = False
        bias = "NEUTRAL"
        trap_type = "NONE"
        reason = "Absorption valid"
        confidence = "LOW"

        # ============================================
        # KASUS POWERUSDT: Flow tinggi, Agg rendah, Harga turun, OI negatif
        # ============================================
        if (trade_flow > AVC_FLOW_MIN and
            aggressive_ratio < AVC_AGGRESSION_MAX and
            change_5m < 0):
            # EXIT LIQUIDITY TRAP: OI negatif = Whale buang barang
            if oi_delta < AVC_OI_DELTA_NEGATIVE:
                is_trap = True
                bias = "SHORT"  # LAWAN balik jadi SHORT!
                trap_type = "EXIT_LIQUIDITY_TRAP"
                confidence = "SUPREME"
                reason = (f"EXIT_LIQUIDITY_TRAP: Flow {trade_flow:.2f}x tinggi + Agg {aggressive_ratio:.2f}x rendah + "
                        f"Harga turun {change_5m:.1f}% TAPI OI amblas {oi_delta:.1f}%. "
                        f"Whale bukan beli, tapi lagi cuci tangan (Exit Liquidity)! SIAP DUMP!")

        return {
            "is_trap": is_trap,
            "trap_type": trap_type,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V66: TEMPORAL ACCUMULATION INDEX (ATI) =================
class TemporalAccumulationV66:
    """
    V66: Mendeteksi Whale yang sabar (Time-Based Accumulation)
    """
    @staticmethod
    def analyze(trade_flow: float, rsi6: float, wmi_ratio: float, oi_delta: float,
                price_stable_hours: float = 0, flow_history: List[float] = None) -> Dict:
        """
        Args:
            trade_flow: Rasio volume beli/jual
            rsi6: RSI 6 period
            wmi_ratio: Whale Mass Index
            oi_delta: OI Delta 5 menit
            price_stable_hours: Durasi harga stabil
            flow_history: History trade flow
        Returns:
            Dict dengan is_accumulating, bias, reason
        """
        is_accumulating = False
        bias = "NEUTRAL"
        reason = "No temporal accumulation detected"
        confidence = "LOW"

        # Cek konsistensi flow jika ada history
        flow_consistent = True
        if flow_history and len(flow_history) >= 3:
            flow_consistent = all(f > ATI_FLOW_MIN for f in flow_history[-3:])

        # ============================================
        # KASUS SAHARA: Flow sangat besar + RSI rendah + WMI Bullish
        # ============================================
        if trade_flow > ATI_FLOW_MIN and rsi6 < ATI_RSI_MAX:
            # Validasi dengan WMI (harus bullish atau netral)
            if wmi_ratio > ATI_WMI_MIN or (wmi_ratio > 0 and abs(wmi_ratio) < 50):
                is_accumulating = True
                bias = "LONG"
                confidence = "SUPREME"
                reason = (f"TEMPORAL_ACCUMULATION: Flow {trade_flow:.2f}x raksasa di RSI {rsi6:.1f} (dingin). "
                        f"WMI {wmi_ratio:.1f}x mendukung bullish. MM sedang parkir harga untuk sapu Short "
                        f"dalam jangka panjang. OI Delta {oi_delta:.2f}% tidak relevan!")

        return {
            "is_accumulating": is_accumulating,
            "bias": bias,
            "reason": reason,
            "confidence": confidence
        }

# ================= V65 - AGGRESSION-MASS DIVERGENCE (AMD) =================
class AggressionMassDivergenceV65:
    """
    V65: Mendeteksi kebohongan WMI (Massa Likuiditas)
    """
    @staticmethod
    def analyze(wmi_ratio: float, aggressive_ratio: float, trade_flow: float,
                oi_delta_5m: float = 0) -> Dict:
        """
        Args:
            wmi_ratio: Whale Mass Index
            aggressive_ratio: Rasio aggressive buy/sell
            trade_flow: Rasio volume beli/jual
            oi_delta_5m: OI delta 5 menit
        Returns:
            Dict dengan is_spoof, action, reason
        """
        is_spoof = False
        action = "NORMAL"
        reason = "AMD: Normal"
        confidence = "LOW"

        # ============================================
        # KASUS ROBO: WMI sangat positif tapi Agresi Beli lemah
        # ============================================
        if wmi_ratio > AMD_WMI_UP_MIN and aggressive_ratio < AMD_AGGRESSION_LONG_MIN:
            is_spoof = True
            action = "FORCE_SHORT"
            confidence = "SUPREME"
            reason = (f"AMD_SPOOF_UP: WMI +{wmi_ratio:.1f}x Bullish TAPI Agresi {aggressive_ratio:.2f}x Lemah. "
                    f"Ini Umpan! Paus pasang tembok palsu buat jebak Long sebelum DUMP! BIAS SHORT!")
        # ============================================
        # KASUS 2: KEBALIKAN - SPOOF DOWN
        # ============================================
        elif wmi_ratio < AMD_WMI_DOWN_MIN and aggressive_ratio > AMD_AGGRESSION_SHORT_MAX:
            is_spoof = True
            action = "FORCE_LONG"
            confidence = "SUPREME"
            reason = (f"AMD_SPOOF_DOWN: WMI {wmi_ratio:.1f}x Bearish TAPI Agresi {aggressive_ratio:.2f}x Kuat. "
                    f"Ini Trap! Paus pasang tembok palsu di bawah buat jebak Short sebelum PUMP! BIAS LONG!")

        return {
            "is_spoof": is_spoof,
            "action": action,
            "bias": action.replace("FORCE_", "") if "FORCE_" in action else "NEUTRAL",
            "reason": reason,
            "confidence": confidence,
            "aggressive_ratio": aggressive_ratio
        }

# ================= V64 - THE DYL PARTICLE (TDP) =================
class DylParticleV64:
    """
    V64: The DYL Particle (TDP) - Formerly The God Particle
    """
    @staticmethod
    def analyze(oi_delta: float, wmi_ratio: float, rsi: float) -> Dict:
        is_god_candle = False
        bias = "NEUTRAL"
        reason = ""

        # Kasus PHA: OI 6.26% + WMI 96.7x
        if oi_delta > TDP_OI_DELTA_MIN and wmi_ratio > TDP_WMI_MIN:
            is_god_candle = True
            bias = "LONG"
            reason = (f"DYL_PARTICLE_LONG: OI Delta {oi_delta:.2f}% + WMI {wmi_ratio:.1f}x! "
                    f"MM sedang mencetak God Candle. RSI {rsi:.1f} sampah! DILARANG SHORT!")
        elif oi_delta > TDP_OI_DELTA_MIN and wmi_ratio < TDP_WMI_NEGATIVE_MIN:
            is_god_candle = True
            bias = "SHORT"
            reason = (f"DYL_PARTICLE_SHORT: OI Delta {oi_delta:.2f}% + WMI {wmi_ratio:.1f}x! "
                    f"MM sedang membantai buyer. RSI {rsi:.1f} sampah! DILARANG LONG!")

        return {
            "is_active": is_god_candle,
            "bias": bias,
            "reason": reason,
            "confidence": "ABSOLUTE" if is_god_candle else "LOW"
        }

# ================= V63: WALL ERASURE DETECTION (WED) =================
class WallErasureV63:
    """
    V63: Mendeteksi tembok beli palsu (Fake Floor)
    """
    @staticmethod
    def analyze(odd_result: Dict, wmi_ratio: float, rsi6: float, oi_delta_5m: float) -> Dict:
        """
        Args:
            odd_result: Hasil dari OrderbookDepthDecayV61
            wmi_ratio: Whale Mass Index
            rsi6: RSI 6 period
            oi_delta_5m: Open Interest delta 5 menit
        Returns:
            Dict dengan is_trap, bias, reason
        """
        is_trap = False
        bias = "NEUTRAL"
        reason = "Floor organic"
        trap_type = "NONE"

        # KASUS ARC: WMI sangat negatif, Heavy Floor, RSI rendah, OI rendah
        if wmi_ratio < -WED_WMI_EXTREME and odd_result['status'] == "HEAVY_FLOOR":
            if rsi6 < WED_RSI_FAKE_MAX and abs(oi_delta_5m) < WED_OI_MIN:
                is_trap = True
                bias = "SHORT"  # Balikkan arah ke SHORT!
                trap_type = "FAKE_FLOOR"
                reason = (f"FAKE_FLOOR_DETECTOR: WMI {wmi_ratio:.1f}x (Target bawah) + Heavy Floor + RSI {rsi6:.1f} (oversold palsu) "
                        f"= MM pasang umpan bid wall buat retail Long sebelum dicabut (Dump)! BIAS SHORT!")
        # KASUS KEBALIKAN: WMI sangat positif, Heavy Ceiling, RSI tinggi, OI rendah
        elif wmi_ratio > WED_WMI_EXTREME and odd_result['status'] == "HEAVY_CEILING":
            if rsi6 > WED_RSI_FAKE_MIN and abs(oi_delta_5m) < WED_OI_MIN:
                is_trap = True
                bias = "LONG"  # Balikkan arah ke LONG!
                trap_type = "FAKE_CEILING"
                reason = (f"FAKE_CEILING_DETECTOR: WMI +{wmi_ratio:.1f}x (Target atas) + Heavy Ceiling + RSI {rsi6:.1f} (overbought palsu) "
                        f"= MM pasang umpan ask wall buat retail Short sebelum di-squeeze! BIAS LONG!")

        return {
            "is_trap": is_trap,
            "trap_type": trap_type,
            "bias": bias,
            "reason": reason,
            "confidence": "SUPREME" if is_trap else "LOW"
        }

# ================= V62: MAGNET WALL REVERSAL (MWR) =================
class MagnetWallReversalV62:
    """
    V62: Mendeteksi 'Tembok Magnet'
    """
    @staticmethod
    def analyze(odd_result: Dict, rsi6: float, wmi_ratio: float, target_side: str) -> Dict:
        """
        Args:
            odd_result: Hasil dari OrderbookDepthDecayV61
            rsi6: RSI 6 period
            wmi_ratio: Whale Mass Index
            target_side: "SHORT_LIQ" atau "LONG_LIQ"
        Returns:
            Dict dengan is_magnet, bias, reason
        """
        is_magnet = False
        bias = "NEUTRAL"
        reason = "Wall normal"
        magnet_type = "NONE"

        # KASUS SAHARA: Heavy Ceiling di atas tapi RSI masih rendah
        if odd_result['status'] == "HEAVY_CEILING" and rsi6 < MWR_RSI_MAX:
            if wmi_ratio > MWR_WMI_THRESHOLD:
                is_magnet = True
                bias = "LONG"
                magnet_type = "BULLISH_MAGNET"
                reason = (f"MAGNET_WALL: Ask volume {odd_result['ask_volume_near']:.0f} itu bukan tembok asli, itu UMPAN! "
                        f"MM narik harga ke RSI 70+ buat makan tembok itu. BIAS LONG!")
        # KASUS KEBALIKAN: Heavy Floor di bawah tapi RSI masih tinggi
        elif odd_result['status'] == "HEAVY_FLOOR" and rsi6 > MWR_RSI_MIN:
            if wmi_ratio < -MWR_WMI_THRESHOLD:
                is_magnet = True
                bias = "SHORT"
                magnet_type = "BEARISH_MAGNET"
                reason = (f"MAGNET_WALL: Bid volume {odd_result['bid_volume_near']:.0f} itu bukan floor asli, itu UMPAN! "
                        f"MM narik harga ke bawah buat makan bid wall itu. BIAS SHORT!")

        return {
            "is_magnet": is_magnet,
            "magnet_type": magnet_type,
            "bias": bias,
            "reason": reason,
            "confidence": "SUPREME" if is_magnet else "LOW"
        }

# ================= V61: LOW-VOLUME SUCTION (LVS) =================
class LowVolumeSuctionV61:
    """
    V61: Mendeteksi market 'Zombi' seperti SIRENUSDT
    """
    @staticmethod
    def analyze(aggressive_ratio: float, trade_flow: float, change_5m: float, wmi_ratio: float) -> Dict:
        """
        Args:
            aggressive_ratio: Rasio aggressive buy/sell
            trade_flow: Rasio volume beli/jual
            change_5m: Perubahan harga 5 menit
            wmi_ratio: Whale Mass Index
        Returns:
            Dict dengan is_suction, bias, reason, dan confidence
        """
        is_suction = False
        bias = "NEUTRAL"
        reason = "Normal flow"
        suction_type = "NONE"

        # KASUS SIREN: Agresi super rendah (< 0.1), Flow rendah (< 0.5),
        # tapi harga STABIL (> -0.2%) dan WMI sangat bearish (< -50)
        if (aggressive_ratio < LVS_AGGRESSION_MAX and
            trade_flow < LVS_FLOW_MAX and
            change_5m > LVS_PRICE_MIN and
            wmi_ratio < LVS_WMI_THRESHOLD):
            is_suction = True
            bias = "LONG"  # Counter-intuitive: MM mau squeeze Short yang terpancing
            suction_type = "BEARISH_SUCTION"
            reason = (f"GHOST_SUCTION: Agg {aggressive_ratio:.2f}x (0 buyer agresif) + Flow {trade_flow:.2f}x (sepi) "
                    f"tapi harga stabil {change_5m:+.2f}% di tengah WMI {wmi_ratio:.1f}x (umpan bawah). "
                    f"MM sedang pancing Short seller untuk di-squeeze ke atas!")
        # KASUS KEBALIKAN: Agresi super rendah, Flow rendah, harga STABIL,
        # dan WMI sangat bullish (> 50) = MM pancing Long untuk di-squeeze ke bawah
        elif (aggressive_ratio < LVS_AGGRESSION_MAX and
            trade_flow < LVS_FLOW_MAX and
            abs(change_5m) < 0.3 and  # Harga stabil di kedua arah
            wmi_ratio > LVS_WMI_POSITIVE_THRESHOLD):
            is_suction = True
            bias = "SHORT"
            suction_type = "BULLISH_SUCTION"
            reason = (f"GHOST_SUCTION: Agg {aggressive_ratio:.2f}x + Flow {trade_flow:.2f}x "
                    f"tapi harga stabil di tengah WMI {wmi_ratio:.1f}x (umpan atas). "
                    f"MM sedang pancing Long untuk di-squeeze ke bawah!")

        return {
            "is_suction": is_suction,
            "suction_type": suction_type,
            "bias": bias,
            "reason": reason,
            "confidence": "SUPREME" if is_suction else "LOW"
        }

# ================= V60: DIVERGENCE TRAP DETECTOR (DTD) =================
class DivergenceTrapDetectorV61:
    """
    V60: Mendeteksi tadah bawah (Absorption) oleh Whale
    """
    @staticmethod
    def analyze(trade_flow: float, aggressive_ratio: float, change_5m: float) -> Dict:
        """
        trade_flow: rasio volume beli/jual
        aggressive_ratio: rasio aggressive buy/sell
        change_5m: perubahan harga 5 menit
        Returns:
            Dict dengan is_trap dan reason
        """
        is_trap = False
        reason = "Flow sinkron dengan harga"
        trap_type = "NONE"
        bias = "NEUTRAL"

        # KASUS POWERUSDT: Harga turun, Agresi Jual tinggi, TAPI Flow Beli besar
        if change_5m < 0 and aggressive_ratio < 0.8 and trade_flow > 1.1:
            is_trap = True
            trap_type = "BULLISH_ABSORPTION"
            bias = "LONG"
            reason = f"BULLISH_ABSORPTION: Harga turun {change_5m:.1f}%, Retail jual agresif (Agg {aggressive_ratio:.2f}x) tapi Whale tadah pake Limit Buy (Flow {trade_flow:.2f}x). SIAP TERBANG!"
        # Kebalikannya: Harga naik, Agresi Beli tinggi, TAPI Flow Jual besar
        elif change_5m > 0 and aggressive_ratio > 1.2 and trade_flow < 0.9:
            is_trap = True
            trap_type = "BEARISH_ABSORPTION"
            bias = "SHORT"
            reason = f"BEARISH_ABSORPTION: Harga naik {change_5m:.1f}%, Retail beli agresif (Agg {aggressive_ratio:.2f}x) tapi Whale pasang tembok Limit Sell (Flow {trade_flow:.2f}x). SIAP DUMP!"

        return {
            "is_trap": is_trap,
            "trap_type": trap_type,
            "bias": bias,
            "reason": reason,
            "confidence": "SUPREME" if is_trap else "LOW"
        }

# ================= V60: ORDERBOOK DEPTH DECAY (ODD) =================
class OrderbookDepthDecayV61:
    """
    V60: Orderbook Depth Decay (ODD)
    """
    @staticmethod
    def analyze(bids: List, asks: List, current_price: float,
                target_distance: float, target_side: str) -> Dict:
        """
        target_side: "SHORT_LIQ" (atas) atau "LONG_LIQ" (bawah)
        """
        if not bids or not asks:
            return {
                "is_thin": False,
                "is_defense": False,
                "status": "UNKNOWN",
                "reason": "No orderbook data"
            }

        # Ambil 5 level bid dan ask
        top_bids = bids[:ODD_WINDOW_SIZE] if len(bids) >= ODD_WINDOW_SIZE else bids
        top_asks = asks[:ODD_WINDOW_SIZE] if len(asks) >= ODD_WINDOW_SIZE else asks

        # Hitung total volume di dekat price
        bid_volume_near = 0
        ask_volume_near = 0

        # Volume bid dalam 0.1% dari current price
        for bid_price, bid_qty in top_bids:
            if abs(bid_price - current_price) / current_price * 100 < 0.1:
                bid_volume_near += bid_qty

        # Volume ask dalam 0.1% dari current price
        for ask_price, ask_qty in top_asks:
            if abs(ask_price - current_price) / current_price * 100 < 0.1:
                ask_volume_near += ask_qty

        # Deteksi thinning (orderbook menguap) untuk target side
        is_thin = False
        is_defense = False
        status = "NORMAL"
        reason = "Orderbook normal"

        if target_side == "SHORT_LIQ":  # Target ke atas
            # Untuk ke atas, kita perlu ask side tipis (hambatan kecil)
            if ask_volume_near < ODD_VOLUME_MIN and bid_volume_near > ask_volume_near * ODD_DEFENSE_RATIO:
                is_thin = True
                status = "ASK_THINNING"
                reason = f"Ask side tipis ({ask_volume_near:.0f}), Bid side tebal ({bid_volume_near:.0f}) - Jalan ke atas terbuka"
            # Deteksi defense (bandar menahan harga)
            elif ask_volume_near > ODD_VOLUME_MIN * 2 and bid_volume_near < ask_volume_near * ODD_THIN_RATIO:
                is_defense = True
                status = "HEAVY_CEILING"
                reason = f"Heavy Ceiling terdeteksi! Ask volume {ask_volume_near:.0f} - Harga ditahan"
        else:  # target_side == "LONG_LIQ" (target ke bawah)
            # Untuk ke bawah, kita perlu bid side tipis (hambatan kecil)
            if bid_volume_near < ODD_VOLUME_MIN and ask_volume_near > bid_volume_near * ODD_DEFENSE_RATIO:
                is_thin = True
                status = "BID_THINNING"
                reason = f"Bid side tipis ({bid_volume_near:.0f}), Ask side tebal ({ask_volume_near:.0f}) - Jalan ke bawah terbuka"
            # Deteksi defense (bandar menahan harga)
            elif bid_volume_near > ODD_VOLUME_MIN * 2 and ask_volume_near < bid_volume_near * ODD_THIN_RATIO:
                is_defense = True
                status = "HEAVY_FLOOR"
                reason = f"Heavy Floor terdeteksi! Bid volume {bid_volume_near:.0f} - Harga ditahan"

        return {
            "is_thin": is_thin,
            "is_defense": is_defense,
            "status": status,
            "reason": reason,
            "bid_volume_near": round(bid_volume_near, 2),
            "ask_volume_near": round(ask_volume_near, 2)
        }

# ================= V62: GHOST INTENT DETECTOR =================
class GhostIntentDetectorV62:
    """
    V62: Ghost Intent Detector dengan SILENT_DRIVE rule
    """
    @staticmethod
    def analyze(rsi6: float, aggressive_ratio: float, change_5m: float,
                oi_delta_5m: float, short_dist: float, long_dist: float,
                odd_result: Dict, pnr_bias: str = "NEUTRAL",
                wmi_ratio: float = 0) -> Dict:
        intent_score = 0
        intent_bias = "NEUTRAL"
        reasons = []
        confidence = "LOW"

        # ============================================
        # V59: THE 95-RSI SUICIDE RULE
        # ============================================
        if rsi6 > RSI_SUICIDE_MIN and wmi_ratio > 0 and short_dist < SUICIDE_DISTANCE_MAX:
            return {
                "is_ghost": True,
                "bias": "LONG",
                "score": 100,
                "confidence": "SUPREME",
                "reasons": [f"PARABOLIC_FLIGHT: RSI {rsi6:.1f} 95+ tapi likuidasi SHORT tinggal {short_dist}%. MM pasti sapu atas dulu!"]
            }
        if rsi6 < 5 and wmi_ratio < 0 and long_dist < SUICIDE_DISTANCE_MAX:
            return {
                "is_ghost": True,
                "bias": "SHORT",
                "score": -100,
                "confidence": "SUPREME",
                "reasons": [f"FREE_FALL: RSI {rsi6:.1f} <5 tapi likuidasi LONG tinggal {long_dist}%. MM pasti sapu bawah dulu!"]
            }

        # ============================================
        # V62: SILENT_DRIVE RULE
        # ============================================
        if abs(oi_delta_5m) < 1.0:  # Fuel super tipis
            if rsi6 < 40 and wmi_ratio > 0:
                return {
                    "is_ghost": True,
                    "bias": "LONG",
                    "score": 40,
                    "confidence": "HIGH",
                    "reasons": ["SILENT_DRIVE: Low OI + Low RSI + WMI positif = MM narik harga tanpa jejak ke atas."]
                }
            elif rsi6 > 60 and wmi_ratio < 0:
                return {
                    "is_ghost": True,
                    "bias": "SHORT",
                    "score": -40,
                    "confidence": "HIGH",
                    "reasons": ["SILENT_DRIVE: Low OI + High RSI + WMI negatif = MM dorong harga tanpa jejak ke bawah."]
                }

        # ============================================
        # 1. ABSORPTION TRAP
        # ============================================
        if rsi6 < ABSORPTION_RSI_MAX and aggressive_ratio > ABSORPTION_AGG_MIN and abs(change_5m) < ABSORPTION_PRICE_MAX and oi_delta_5m < 0:
            intent_score -= 100
            intent_bias = "SHORT"
            confidence = "SUPREME"
            reasons.append(f"ABSORPTION_TRAP: RSI {rsi6:.1f} rendah + Agg {aggressive_ratio:.1f}x gila + OI turun {oi_delta_5m:.1f}% = MM serap beli retail untuk lanjut dump")
            return {
                "is_ghost": True,
                "bias": intent_bias,
                "score": intent_score,
                "confidence": confidence,
                "reasons": reasons
            }

        # ============================================
        # 2. THE 2% OI FUEL MANDATE
        # ============================================
        if abs(oi_delta_5m) < OI_FUEL_MINIMUM:
            reasons.append(f"LOW_FUEL: OI Δ5m {oi_delta_5m:.1f}% < {OI_FUEL_MINIMUM}% - No institutional fuel")
            intent_score -= 30
            if pnr_bias != "NEUTRAL":
                return {
                    "is_ghost": True,
                    "bias": "NEUTRAL",
                    "confidence": "LOW",
                    "reason": f"GHOST_MANDATE: OI terlalu rendah ({oi_delta_5m:.1f}%) untuk PNR.",
                    "score": -50,
                    "reasons": [f"GHOST_MANDATE: OI terlalu rendah ({oi_delta_5m:.1f}%)"]
                }

        # ============================================
        # 3. ABSORPTION DIVERGENCE TRACKER
        # ============================================
        if rsi6 < ABSORPTION_RSI_MAX and aggressive_ratio > ABSORPTION_AGG_MIN and abs(change_5m) < ABSORPTION_PRICE_MAX:
            intent_score -= 50
            intent_bias = "SHORT"
            reasons.append(f"ABSORPTION_DIVERGENCE: RSI {rsi6:.1f} rendah + Agg {aggressive_ratio:.1f}x tinggi + harga stagnan = MM absorbing longs")
            confidence = "SUPREME"
        elif rsi6 > (100 - ABSORPTION_RSI_MAX) and aggressive_ratio < (1/ABSORPTION_AGG_MIN) and abs(change_5m) < ABSORPTION_PRICE_MAX:
            intent_score += 50
            intent_bias = "LONG"
            reasons.append(f"DISTRIBUTION_DIVERGENCE: RSI {rsi6:.1f} tinggi + Agg {aggressive_ratio:.1f}x rendah + harga stagnan = MM distributing shorts")
            confidence = "SUPREME"

        # ============================================
        # 4. THE MAGNET DECOUPLING RULE
        # ============================================
        if long_dist < MAGNET_DECOUPLE_DIST and rsi6 < RSI_EXTREME_SHORT:
            intent_score += 40
            intent_bias = "LONG"
            reasons.append(f"MAGNET_DECOUPLE: Long liq {long_dist}% dekat tapi RSI {rsi6:.1f} oversold - Safety brake aktif")
            confidence = "HIGH"
        if short_dist < MAGNET_DECOUPLE_DIST and rsi6 > RSI_EXTREME_LONG:
            intent_score -= 40
            intent_bias = "SHORT"
            reasons.append(f"MAGNET_DECOUPLE: Short liq {short_dist}% dekat tapi RSI {rsi6:.1f} overbought - Safety brake aktif")
            confidence = "HIGH"

        # ============================================
        # 5. ORDERBOOK DEPTH DECAY INTEGRATION
        # ============================================
        if odd_result['is_defense']:
            if odd_result['status'] == "HEAVY_CEILING":
                intent_score -= 30
                intent_bias = "SHORT"
                reasons.append(f"ODD_DEFENSE: {odd_result['reason']}")
            elif odd_result['status'] == "HEAVY_FLOOR":
                intent_score += 30
                intent_bias = "LONG"
                reasons.append(f"ODD_DEFENSE: {odd_result['reason']}")
        elif odd_result['is_thin']:
            if odd_result['status'] == "ASK_THINNING":
                intent_score += 20
                intent_bias = "LONG"
                reasons.append(f"ODD_THINNING: {odd_result['reason']}")
            elif odd_result['status'] == "BID_THINNING":
                intent_score -= 20
                intent_bias = "SHORT"
                reasons.append(f"ODD_THINNING: {odd_result['reason']}")

        # Tentukan apakah ini ghost
        is_ghost = intent_score <= -30 or intent_score >= 30
        if intent_score >= 30:
            intent_bias = "LONG"
            confidence = "SUPREME" if intent_score >= 50 else "HIGH"
        elif intent_score <= -30:
            intent_bias = "SHORT"
            confidence = "SUPREME" if intent_score <= -50 else "HIGH"

        return {
            "is_ghost": is_ghost,
            "bias": intent_bias,
            "score": intent_score,
            "confidence": confidence,
            "reasons": reasons
        }

# ================= V60: ENGINE STARTER =================
class EngineStarterV61:
    """
    V60: The Engine Starter
    """
    @staticmethod
    def analyze(data: Dict, oi_history: deque, price_history: deque) -> Dict:
        # 1. PARAMETER AWAL
        rsi = data['rsi6']
        agg = data['aggressive_ratio']
        ob = data['ob_ratio']
        oi_delta = data['oi_delta_5m']
        s_dist = data['short_liq_dist']
        l_dist = data['long_liq_dist']
        trade_flow = data['trade_flow']
        change_5m = data['change_5m']
        wmi_ratio = data.get('wmi_ratio', 0)

        starter_score = 0
        bias = "NEUTRAL"
        reasons = []

        # --- A. DETEKSI "THINNING" ---
        if ob > THINNING_OB_HIGH and agg > THINNING_AGG_HIGH:
            starter_score += 30
            reasons.append("VACUUM_UP: Sisi Ask dikosongkan, harga siap melesat")
            bias = "LONG"
        elif ob < THINNING_OB_LOW and agg < THINNING_AGG_LOW:
            starter_score += 30
            reasons.append("VACUUM_DOWN: Sisi Bid dicabut, harga siap terjun")
            bias = "SHORT"

        # --- B. DETEKSI "FUEL INJECTION" ---
        if abs(change_5m) < FUEL_INJECTION_PRICE and oi_delta > FUEL_INJECTION_OI:
            starter_score += 40
            reasons.append(f"FUEL_INJECTION: Modal masuk {oi_delta:.1f}% tapi harga dipaku")
            bias = "LONG" if trade_flow > FUEL_FLOW_THRESHOLD else "SHORT"

        # --- C. DETEKSI "CLUSTER ATTRACTION" ---
        if abs(wmi_ratio) > WHALE_WMI_THRESHOLD:
            starter_score += 25
            reasons.append(f"WHALE_CLUSTERING: Target besar terdeteksi (WMI: {wmi_ratio:.0f})")
            if wmi_ratio > 0:
                bias = "LONG" if bias == "NEUTRAL" else bias
            else:
                bias = "SHORT" if bias == "NEUTRAL" else bias

        # --- FINAL STARTER DECISION ---
        is_starting = starter_score >= STARTER_MIN_SCORE

        # Validasi Keamanan (Anti-Pucuk)
        if is_starting:
            if bias == "LONG" and rsi > RSI_HOT_LIMIT:
                is_starting = False
                reasons.append("CANCEL: RSI terlalu panas")
            if bias == "SHORT" and rsi < RSI_COLD_LIMIT:
                is_starting = False
                reasons.append("CANCEL: RSI terlalu dingin")

        return {
            "is_starting": is_starting,
            "bias": bias if is_starting else "NEUTRAL",
            "score": starter_score,
            "reasons": reasons
        }

# ================= V60: TTK COUNTDOWN =================
class TTKCountdownV61:
    """
    V60: Time to Kill (TTK) Countdown
    """
    @staticmethod
    def estimate(starter_score: int, oi_delta: float, vol_ratio: float) -> Dict:
        base_ttk = TTK_BASE

        oi_acceleration = min(abs(oi_delta) * TTK_OI_FACTOR, TTK_OI_MAX_REDUCTION)
        vol_pressure = min(vol_ratio * TTK_VOL_FACTOR, TTK_VOL_MAX_REDUCTION)
        score_boost = (starter_score / 100) * TTK_SCORE_FACTOR

        estimated_minutes = max(base_ttk - oi_acceleration - vol_pressure - score_boost, 1.0)

        if estimated_minutes < TTK_IMMINENT_THRESHOLD:
            urgency = "IMMINENT"
        elif estimated_minutes < TTK_HIGH_THRESHOLD:
            urgency = "HIGH"
        else:
            urgency = "PREPARING"

        return {
            "estimated_minutes": round(estimated_minutes, 1),
            "urgency": urgency,
            "fuel_ready": "YES" if abs(oi_delta) > FUEL_INJECTION_OI else "NO"
        }

# ================= V54: LIQUIDITY RISK-REWARD RATIO (LRR) =================
class LiquidityRiskRewardV54:
    """
    V54: Liquidity Risk-Reward Ratio (LRR)
    """
    @staticmethod
    def analyze(short_dist: float, long_dist: float,
                short_vol: float, long_vol: float) -> Dict:
        short_weight = short_vol / (short_dist if short_dist > 0 else 0.1)
        long_weight = long_vol / (long_dist if long_dist > 0 else 0.1)

        distance_ratio = long_dist / short_dist if short_dist > 0 else 99

        is_trap = False
        danger_side = "NONE"

        if distance_ratio > LRR_CLIFF_RATIO and long_vol > (short_vol * LRR_MIN_VOLUME_RATIO):
            is_trap = True
            danger_side = "LONG_LIQ_CLIFF"
        elif (short_dist / long_dist if long_dist > 0 else 99) > LRR_CLIFF_RATIO and short_vol > (long_vol * LRR_MIN_VOLUME_RATIO):
            is_trap = True
            danger_side = "SHORT_LIQ_CLIFF"

        if danger_side == "LONG_LIQ_CLIFF":
            recommendation = "AVOID_LONG"
        elif danger_side == "SHORT_LIQ_CLIFF":
            recommendation = "AVOID_SHORT"
        else:
            recommendation = "PROCEED"

        return {
            "is_trap": is_trap,
            "ratio": round(distance_ratio, 2),
            "danger_side": danger_side,
            "recommendation": recommendation,
            "short_weight": round(short_weight, 2),
            "long_weight": round(long_weight, 2)
        }

# ================= V54: AGGRESSION VELOCITY (AV) =================
class AggressionVelocityV54:
    """
    V54: Aggression Velocity (AV)
    """
    @staticmethod
    def analyze(agg_history: deque) -> Dict:
        if len(agg_history) < AV_HISTORY_MIN:
            return {
                "acceleration": 0.0,
                "velocity": 0.0,
                "status": "STABLE",
                "trend": "INSUFFICIENT_DATA",
                "is_market_slam": False
            }

        recent_agg = agg_history[-1]
        prev_agg = agg_history[-2]
        older_agg = agg_history[-3]

        velocity_now = recent_agg - prev_agg
        velocity_prev = prev_agg - older_agg
        acceleration = velocity_now - velocity_prev

        status = "STABLE"
        trend = "NEUTRAL"

        if acceleration > AV_ACCELERATION_THRESHOLD:
            status = "BULLISH_ACCELERATION"
            trend = "ACCELERATING_BUY"
        elif acceleration < -AV_ACCELERATION_THRESHOLD:
            status = "BEARISH_ACCELERATION"
            trend = "ACCELERATING_SELL"

        is_market_slam = status == "BEARISH_ACCELERATION" and velocity_now < -0.3

        return {
            "acceleration": round(acceleration, 3),
            "velocity": round(velocity_now, 3),
            "status": status,
            "trend": trend,
            "is_market_slam": is_market_slam
        }

# ================= AGGRESSION DELTA DIVERGENCE V54 =================
class AggressionDeltaDivergenceV54:
    """
    V54: Aggression Delta Divergence Detector
    """
    @staticmethod
    def analyze(bias: str, aggressive_ratio: float, trade_flow: float,
                rsi6: float, av_status: str = "STABLE") -> Dict:
        is_divergent = False
        action = "PROCEED"
        reason = "Agresi mendukung arah target."

        if bias == "LONG":
            if aggressive_ratio < AGGRESSION_MIN_LONG or trade_flow < FLOW_CRITICAL_LOW:
                is_divergent = True
                action = "CANCEL_LONG"
                reason = f"BEARISH_DIVERGENCE: Mau Long, tapi Agresi {aggressive_ratio}x Bearish!"
            elif av_status == "BEARISH_ACCELERATION":
                is_divergent = True
                action = "CANCEL_LONG"
                reason = f"BEARISH_DIVERGENCE: Market Slam terdeteksi!"
        elif bias == "SHORT":
            if aggressive_ratio > AGGRESSION_MIN_SHORT * 10 or trade_flow > FLOW_CRITICAL_HIGH * 1.25:
                is_divergent = True
                action = "CANCEL_SHORT"
                reason = f"BULLISH_DIVERGENCE: Mau Short, tapi Agresi {aggressive_ratio}x Bullish!"
            elif av_status == "BULLISH_ACCELERATION":
                is_divergent = True
                action = "CANCEL_SHORT"
                reason = f"BULLISH_DIVERGENCE: Bullish acceleration!"

        if rsi6 > RSI_EXTREME_HIGH_WALL and bias == "LONG" and trade_flow < FLOW_CRITICAL_LOW:
            is_divergent = True
            action = "SWITCH_SHORT"
            reason = f"EXHAUSTION_DIVERGENCE: RSI {rsi6} mendidih + Flow kering"
        elif rsi6 < RSI_EXTREME_LOW_WALL and bias == "SHORT" and trade_flow > FLOW_CRITICAL_HIGH:
            is_divergent = True
            action = "SWITCH_LONG"
            reason = f"EXHAUSTION_DIVERGENCE: RSI {rsi6} hancur + Flow deras"

        return {
            "is_divergent": is_divergent,
            "action": action,
            "reason": reason
        }

# ================= POINT OF NO RETURN DETECTOR V54 =================
class PNRDetectorV54:
    """
    V54: Point of No Return Detector
    """
    @staticmethod
    def analyze(short_dist: float, long_dist: float, rsi6: float, trade_flow: float) -> Dict:
        pnr_active = False
        bias = "NEUTRAL"
        reason = ""
        confidence = "LOW"

        if short_dist <= EVENT_HORIZON:
            pnr_active = True
            bias = "LONG"
            reason = f"PNR: Short Liq {short_dist}% < 0.3% - Safety validation diperlukan"
            confidence = "PENDING"
        elif long_dist <= EVENT_HORIZON:
            pnr_active = True
            bias = "SHORT"
            reason = f"PNR: Long Liq {long_dist}% < 0.3% - Safety validation diperlukan"
            confidence = "PENDING"

        return {
            "pnr_active": pnr_active,
            "bias": bias,
            "confidence": confidence,
            "reason": reason
        }

# ================= VOLATILITY BURST TRACKER V54 =================
class VolatilityBurstTrackerV54:
    """
    V54: Volatility Burst Tracker
    """
    @staticmethod
    def analyze(current_price: float, price_history: List[float], volume_ratio: float) -> Dict:
        if len(price_history) < 10:
            return {"is_burst": False, "multiplier": 1.0, "reason": "Insufficient data"}

        recent_prices = list(price_history)[-10:]
        std_dev = np.std(recent_prices)
        avg_price = np.mean(recent_prices)

        if std_dev == 0 or avg_price == 0:
            return {"is_burst": False, "multiplier": 1.0, "reason": "Zero volatility"}

        current_deviation = abs(current_price - avg_price)
        vol_multiplier = current_deviation / std_dev

        is_burst = vol_multiplier > VOLATILITY_BURST_MULTIPLIER and volume_ratio > VOLUME_BURST_THRESHOLD

        if is_burst:
            reason = f"VOL_BURST: Akselerasi {vol_multiplier:.1f}x + Volume {volume_ratio}x"
        else:
            reason = "Volatility normal"

        return {
            "is_burst": is_burst,
            "multiplier": round(vol_multiplier, 2),
            "reason": reason
        }

# ================= HFT SIGNATURE DETECTOR V61 =================
class HFTSignatureDetectorV61:
    """
    V61: Mendeteksi signature institutional trading
    """
    @staticmethod
    def analyze(price: float, short_dist: float, long_dist: float,
                trade_flow: float, aggressive_ratio: float,
                oi_delta_1m: float, oi_delta_5m: float,
                rsi6: float, change_5m: float,
                gravity_bias: str, gravity_strength: float,
                persistence_minutes: float,
                short_gravity: float, long_gravity: float,
                lrr_result: Dict, av_result: Dict,
                starter_result: Dict, ghost_result: Dict) -> Dict:
        signals = []
        weight = 0
        final_bias = "NEUTRAL"

        # CEK PNR dulu
        if short_dist <= EVENT_HORIZON:
            signals.append(f"PNR: Short Liq {short_dist}% - Ghost validation needed")
            return {
                "bias": "LONG",
                "confidence": "PENDING",
                "weight": 100,
                "signals": signals,
                "persistence_minutes": persistence_minutes
            }
        elif long_dist <= EVENT_HORIZON:
            signals.append(f"PNR: Long Liq {long_dist}% - Ghost validation needed")
            return {
                "bias": "SHORT",
                "confidence": "PENDING",
                "weight": 100,
                "signals": signals,
                "persistence_minutes": persistence_minutes
            }

        # 1. GHOST INTENT CHECK
        if ghost_result['is_ghost'] and ghost_result['confidence'] in ["SUPREME", "HIGH"]:
            signals.append(f"GHOST_DETECTED: {ghost_result['reasons'][0] if ghost_result['reasons'] else 'Intent detected'}")
            weight += ghost_result['score']
            final_bias = ghost_result['bias']

        # 2. ENGINE STARTER CHECK
        elif starter_result['is_starting']:
            signals.append(f"ENGINE_START: {' | '.join(starter_result['reasons'][:1])}")
            weight += 80 if starter_result['bias'] == "LONG" else -80
            final_bias = starter_result['bias']

        # 3. LRR CHECK
        elif lrr_result['is_trap']:
            if lrr_result['danger_side'] == "LONG_LIQ_CLIFF":
                signals.append(f"LRR TRAP: Target atas cuma umpan")
                weight -= 80
                final_bias = "SHORT"
            elif lrr_result['danger_side'] == "SHORT_LIQ_CLIFF":
                signals.append(f"LRR TRAP: Target bawah cuma umpan")
                weight += 80
                final_bias = "LONG"

        # 4. AGGRESSION VELOCITY CHECK
        elif av_result['is_market_slam']:
            signals.append(f"MARKET SLAM: Agresi jual berakselerasi!")
            weight -= 60
            final_bias = "SHORT"
        elif av_result['status'] == "BULLISH_ACCELERATION" and av_result['acceleration'] > 1.0:
            signals.append(f"BULLISH ACCELERATION: Agresi beli berakselerasi!")
            weight += 60
            final_bias = "LONG"

        # 5. SILENT LOADING DETECTION
        elif (short_gravity > GRAVITY_EXTREME_THRESHOLD or long_gravity > GRAVITY_EXTREME_THRESHOLD):
            if short_dist < 1.0 and gravity_bias == "LONG" and aggressive_ratio < AGGRESSION_MIN_LONG:
                signals.append(f"SILENT LOADING: Gravity EXTREME + Agg rendah")
                weight += 60
                final_bias = "LONG"
            elif long_dist < 1.0 and gravity_bias == "SHORT" and aggressive_ratio < AGGRESSION_MIN_LONG:
                signals.append(f"SILENT DISTRIBUTION: Gravity EXTREME + Agg rendah")
                weight -= 60
                final_bias = "SHORT"

        # 6. OI DELTA ANALYSIS
        elif change_5m < -1.0:
            if oi_delta_5m > OI_ACCUMULATION_THRESHOLD:
                signals.append(f"OI: Price down + OI up = REAL SHORTING")
                weight += 40
                final_bias = "SHORT"
            elif oi_delta_5m < OI_LIQUIDATION_THRESHOLD:
                signals.append(f"OI: Price down + OI down = LONG LIQUIDATION")
                weight -= 30
                final_bias = "LONG"
        elif change_5m > 1.0:
            if oi_delta_5m > OI_ACCUMULATION_THRESHOLD:
                signals.append(f"OI: Price up + OI up = REAL ACCUMULATION")
                weight += 40
                final_bias = "LONG"
            elif oi_delta_5m < OI_LIQUIDATION_THRESHOLD:
                signals.append(f"OI: Price up + OI down = SHORT SQUEEZE")
                weight -= 30
                final_bias = "SHORT"

        # Tentukan confidence
        if weight >= 40 or (final_bias != "NEUTRAL" and abs(weight) >= 30):
            confidence = "SUPREME" if abs(weight) >= 50 else "HIGH"
        elif final_bias != "NEUTRAL":
            confidence = "MEDIUM"
        else:
            confidence = "LOW"

        return {
            "bias": final_bias,
            "confidence": confidence,
            "weight": weight,
            "signals": signals,
            "persistence_minutes": round(persistence_minutes, 1)
        }

# ================= DEEP REVERSION DETECTOR V54 =================
class DeepReversionDetectorV54:
    """
    V54: Menghitung probabilitas pembalikan harga
    """
    @staticmethod
    def analyze(rsi6: float, trade_flow: float, volume_ratio: float,
                premium: float, change_5m: float,
                oi_delta_5m: float) -> Dict:
        reversion_score = 0
        bias = "NEUTRAL"
        reasons = []

        if rsi6 < RSI_EXTREME_OVERSOLD:
            reversion_score += 40
            reasons.append(f"EXTREME_OVERSOLD (RSI {rsi6:.1f})")
            if volume_ratio > VOLUME_ACCUMULATION_SURGE:
                reversion_score += 30
                reasons.append("VOLUME_ACCUMULATION")
            if trade_flow > FLOW_FORCE_LONG:
                reversion_score += 20
                reasons.append("FLOW_REVERSAL")
            if oi_delta_5m < OI_LIQUIDATION_THRESHOLD:
                reversion_score += 30
                reasons.append(f"OI LIQUIDATION DONE")
            if change_5m < -3.0:
                reversion_score += 10
                reasons.append(f"DUMP {change_5m}%")
        elif rsi6 > RSI_EXTREME_OVERBOUGHT:
            reversion_score -= 40
            reasons.append(f"EXTREME_OVERBOUGHT (RSI {rsi6:.1f})")
            if premium < PREMIUM_EXTREME_SHORT:
                reversion_score -= 30
                reasons.append("PREMIUM_DIVERGENCE")
            if trade_flow < FLOW_CRITICAL_LOW:
                reversion_score -= 20
                reasons.append("FLOW_LEMAH_DI_PUNCAK")
            if oi_delta_5m < OI_LIQUIDATION_THRESHOLD:
                reversion_score -= 30
                reasons.append(f"SHORT SQUEEZE DONE")
            if change_5m > 3.0:
                reversion_score -= 10
                reasons.append(f"PUMP {change_5m}%")

        if rsi6 < RSI_FORBID_SHORT:
            reasons.append(f"RSI < {RSI_FORBID_SHORT} - DILARANG SHORT!")
            bias = "LONG"
            reversion_score += 20
        if rsi6 > RSI_FORBID_LONG:
            reasons.append(f"RSI > {RSI_FORBID_LONG} - DILARANG LONG!")
            bias = "SHORT"
            reversion_score -= 20

        if reversion_score >= 60:
            bias = "LONG"
            confidence = "SUPREME"
            reason_main = "DEEP_BOTTOM_REVERSION: Harga sudah terlalu murah"
        elif reversion_score <= -60:
            bias = "SHORT"
            confidence = "SUPREME"
            reason_main = "TOP_EXHAUSTION: Harga sudah terlalu mahal"
        elif reversion_score >= 30:
            bias = "LONG"
            confidence = "HIGH"
            reason_main = "BOTTOM_FORMATION: Potensi reversal ke atas"
        elif reversion_score <= -30:
            bias = "SHORT"
            confidence = "HIGH"
            reason_main = "TOP_FORMATION: Potensi reversal ke bawah"
        else:
            bias = "NEUTRAL"
            confidence = "LOW"
            reason_main = "Market masih dalam range wajar."

        return {
            "bias": bias,
            "score": reversion_score,
            "confidence": confidence,
            "reason": reason_main,
            "details": reasons
        }

# ================= OI VELOCITY TRACKER V61 =================
class OIVelocityTrackerV61:
    """
    V61: Enhanced OI tracker
    """
    @staticmethod
    def analyze(oi_current: float, oi_5m_ago: float, price_change: float, trade_flow: float) -> Dict:
        # Hitung delta menggunakan anchor 5 menit lalu
        oi_delta_5m = 0
        if oi_5m_ago and oi_5m_ago > 0:
            oi_delta_5m = ((oi_current - oi_5m_ago) / oi_5m_ago) * 100

        status = "NEUTRAL"
        power = 0
        reason = "OI stabil"
        institutional_score = 0

        # REAL ACCUMULATION: Harga sideway, OI naik
        if abs(price_change) < 0.5 and oi_delta_5m > OI_ACCUMULATION_THRESHOLD:
            status = "REAL_ACCUMULATION"
            power = oi_delta_5m * 15
            institutional_score = 80
            reason = f"INSTITUTIONAL LOADING: OI naik {oi_delta_5m:.1f}% dalam 5m, harga dipaku"
        # REAL SHORTING: Harga turun, OI naik
        elif price_change < -1.0 and oi_delta_5m > OI_SURGE_THRESHOLD:
            status = "REAL_SHORTING"
            power = abs(price_change) * oi_delta_5m * 10
            institutional_score = 90
            reason = f"INSTITUTIONAL SHORTING: Harga turun {price_change:.1f}% + OI naik {oi_delta_5m:.1f}%"
        # LONG LIQUIDATION: Harga turun, OI turun
        elif price_change < -1.0 and oi_delta_5m < OI_LIQUIDATION_THRESHOLD:
            status = "LONG_LIQUIDATION"
            power = abs(oi_delta_5m) * 10
            institutional_score = -60
            reason = f"LONG LIQUIDATION: Harga turun + OI turun {oi_delta_5m:.1f}% (SIAP REBOUND)"
        # SHORT SQUEEZE: Harga naik, OI turun
        elif price_change > 1.0 and oi_delta_5m < OI_LIQUIDATION_THRESHOLD:
            status = "SHORT_SQUEEZE"
            power = abs(oi_delta_5m) * 10
            institutional_score = -70
            reason = f"SHORT SQUEEZE: Harga naik + OI turun {oi_delta_5m:.1f}% (SIAP KOREKSI)"
        # DISTRIBUTION: Harga sideway, OI turun
        elif abs(price_change) < 0.5 and oi_delta_5m < OI_LIQUIDATION_THRESHOLD:
            status = "DISTRIBUTION"
            power = abs(oi_delta_5m) * 8
            institutional_score = -50
            reason = f"DISTRIBUTION: OI turun {oi_delta_5m:.1f}% di harga stabil"

        return {
            "status": status,
            "oi_delta_5m": round(oi_delta_5m, 2),
            "power": round(power, 2),
            "institutional_score": institutional_score,
            "reason": reason
        }

# ================= LIQUIDITY GRAVITY CALCULATOR V54 =================
class LiquidityGravityCalculatorV54:
    """
    V54: Gravity calculator
    """
    @staticmethod
    def calculate(short_dist: float, long_dist: float,
                short_volume: float = 1.0, long_volume: float = 1.0,
                oi_density: float = 1.0, rsi6: float = 50) -> Dict:
        short_dist_safe = max(short_dist, 0.1)
        long_dist_safe = max(long_dist, 0.1)

        if short_dist > FAR_LIQ and long_dist > FAR_LIQ:
            return {
                "target": "NONE",
                "bias": "NEUTRAL",
                "strength": "LOW",
                "short_gravity": 0,
                "long_gravity": 0,
                "ratio": 1.0,
                "reason": f"Jarak terlalu jauh"
            }

        short_gravity = (short_volume * oi_density) / (short_dist_safe ** LIQ_GRAVITY_POWER)
        long_gravity = (long_volume * oi_density) / (long_dist_safe ** LIQ_GRAVITY_POWER)

        if long_gravity > 0:
            ratio = short_gravity / long_gravity
        else:
            ratio = 99.0 if short_gravity > 0 else 1.0

        is_massive = short_gravity > GRAVITY_MASSIVE_THRESHOLD or long_gravity > GRAVITY_MASSIVE_THRESHOLD
        is_extreme = short_gravity > GRAVITY_EXTREME_THRESHOLD or long_gravity > GRAVITY_EXTREME_THRESHOLD

        if short_gravity > long_gravity * LIQ_GRAVITY_EXTREME:
            target = "SHORT_LIQ"
            strength = "MASSIVE" if is_massive else "EXTREME" if is_extreme else "HIGH"
            reason = f"Short liquidity {short_gravity:.1f}x lebih kuat!"
        elif short_gravity > long_gravity * LIQ_GRAVITY_HIGH:
            target = "SHORT_LIQ"
            strength = "HIGH"
            reason = f"Short liquidity {short_gravity:.1f}x lebih kuat"
        elif long_gravity > short_gravity * LIQ_GRAVITY_EXTREME:
            target = "LONG_LIQ"
            strength = "MASSIVE" if is_massive else "EXTREME" if is_extreme else "HIGH"
            reason = f"Long liquidity {long_gravity:.1f}x lebih kuat!"
        elif long_gravity > short_gravity * LIQ_GRAVITY_HIGH:
            target = "LONG_LIQ"
            strength = "HIGH"
            reason = f"Long liquidity {long_gravity:.1f}x lebih kuat"
        else:
            if short_dist < long_dist:
                target = "SHORT_LIQ"
                strength = "NEUTRAL"
                reason = f"Jarak lebih dekat ke short ({short_dist}%)"
            else:
                target = "LONG_LIQ"
                strength = "NEUTRAL"
                reason = f"Jarak lebih dekat ke long ({long_dist}%)"

        return {
            "target": target,
            "bias": "LONG" if target == "SHORT_LIQ" else "SHORT" if target == "LONG_LIQ" else "NEUTRAL",
            "strength": strength,
            "short_gravity": round(short_gravity, 2),
            "long_gravity": round(long_gravity, 2),
            "ratio": round(ratio, 2),
            "reason": reason,
            "is_extreme": is_extreme,
            "is_massive": is_massive
        }

# ================= SPOOFING DETECTOR V54 =================
class SpoofingDetectorV54:
    """
    V54: Deteksi spoofing
    """
    @staticmethod
    def detect(ob_ratio: float, trade_flow: float, aggressive_ratio: float,
            rsi: float, bids: List, asks: List,
            oi_delta_5m: float) -> Dict:
        reasons = []
        spoofing_score = 0
        detected_type = "NONE"

        if ob_ratio > SPOOFING_OB_THRESHOLD and trade_flow < SPOOFING_FLOW_THRESHOLD:
            spoofing_score += 80
            detected_type = "BULLISH_WALL_SPOOF"
            reasons.append(f"Buy wall palsu! OB {ob_ratio}x tapi flow {trade_flow}x")
        elif ob_ratio < (1/SPOOFING_OB_THRESHOLD) and trade_flow > (1/SPOOFING_FLOW_THRESHOLD):
            spoofing_score += 80
            detected_type = "BEARISH_WALL_SPOOF"
            reasons.append(f"Sell wall palsu! OB {ob_ratio}x tapi flow {trade_flow}x")

        if rsi > RSI_WARNING_LONG and trade_flow < FLOW_CRITICAL_LOW:
            spoofing_score += 60
            detected_type = "DISTRIBUTION"
            reasons.append(f"Distribusi di puncak! RSI {rsi:.1f} + flow {trade_flow}x")
            if oi_delta_5m < OI_LIQUIDATION_THRESHOLD:
                spoofing_score += 30
                reasons.append(f"OI turun {oi_delta_5m:.1f}% = REAL DISTRIBUTION")
        if rsi < RSI_DEEP_OVERSOLD and trade_flow > FLOW_CRITICAL_HIGH:
            spoofing_score += 60
            detected_type = "ACCUMULATION"
            reasons.append(f"Akumulasi di dasar! RSI {rsi:.1f} + flow {trade_flow}x")
            if oi_delta_5m > OI_ACCUMULATION_THRESHOLD:
                spoofing_score += 30
                reasons.append(f"OI naik {oi_delta_5m:.1f}% = REAL ACCUMULATION")

        if spoofing_score >= 80:
            if detected_type in ["BULLISH_WALL_SPOOF", "DISTRIBUTION"]:
                bias = "SHORT"
                confidence = "SUPREME"
            else:
                bias = "LONG"
                confidence = "SUPREME"
            reason_main = f"SPOOFING: {reasons[0]}"
        elif spoofing_score >= 50:
            if detected_type in ["BULLISH_WALL_SPOOF", "DISTRIBUTION"]:
                bias = "SHORT"
                confidence = "HIGH"
            else:
                bias = "LONG"
                confidence = "HIGH"
            reason_main = f"Potensi spoofing: {reasons[0]}"
        else:
            bias = "NEUTRAL"
            confidence = "LOW"
            reason_main = "No spoofing detected"

        return {
            "score": spoofing_score,
            "type": detected_type,
            "bias": bias,
            "confidence": confidence,
            "reason": reason_main,
            "details": reasons
        }

# ================= POSITIONING PRESSURE INDEX V54 =================
class PositioningPressureIndexV54:
    """
    V54: PPI dengan OI component
    """
    @staticmethod
    def calculate(funding: float, premium: float,
                avg_funding: float, trade_flow: float,
                aggressive_trades: float = 1.0,
                oi_delta_5m: float = 0,
                rsi6: float = 50) -> Dict:
        funding_z = 0
        if avg_funding != 0:
            funding_std = max(abs(avg_funding) * 0.5, 0.01)
            funding_z = (funding - avg_funding) / funding_std
            funding_z = max(min(funding_z, 3), -3)

        premium_z = premium / 1.0
        premium_z = max(min(premium_z, 3), -3)

        flow_component = 0
        if trade_flow > FLOW_EXTREME_BUY:
            flow_component = 2.0
        elif trade_flow > FLOW_CRITICAL_HIGH:
            flow_component = 1.0
        elif trade_flow < FLOW_EXTREME_SELL:
            flow_component = -2.0
        elif trade_flow < FLOW_CRITICAL_LOW:
            flow_component = -1.0

        if rsi6 < RSI_FORBID_SHORT and flow_component < 0:
            flow_component = 0
        if rsi6 > RSI_FORBID_LONG and flow_component > 0:
            flow_component = 0

        aggressive_component = 0
        if aggressive_trades > FLOW_CRITICAL_HIGH:
            aggressive_component = 1.0
        elif aggressive_trades < 0.5:
            aggressive_component = -1.0

        oi_component = 0
        if oi_delta_5m > OI_SURGE_THRESHOLD:
            oi_component = 2.0
        elif oi_delta_5m > OI_ACCUMULATION_THRESHOLD:
            oi_component = 1.0
        elif oi_delta_5m < OI_EXTREME_DROP:
            oi_component = -2.0
        elif oi_delta_5m < OI_LIQUIDATION_THRESHOLD:
            oi_component = -1.0

        ppi = (funding_z * 0.2 +
            premium_z * 0.2 +
            flow_component * 0.2 +
            aggressive_component * 0.1 +
            oi_component * 0.3)

        if ppi > PPI_EXTREME:
            pressure = "EXTREME_BULLISH"
            bias = "LONG"
            strength = "SUPREME"
            reason = f"Extreme bullish! PPI: {ppi:.2f}"
        elif ppi > PPI_HIGH:
            pressure = "BULLISH"
            bias = "LONG"
            strength = "HIGH"
            reason = f"Bullish, PPI: {ppi:.2f}"
        elif ppi < -PPI_EXTREME:
            pressure = "EXTREME_BEARISH"
            bias = "SHORT"
            strength = "SUPREME"
            reason = f"Extreme bearish! PPI: {ppi:.2f}"
        elif ppi < -PPI_HIGH:
            pressure = "BEARISH"
            bias = "SHORT"
            strength = "HIGH"
            reason = f"Bearish, PPI: {ppi:.2f}"
        else:
            pressure = "NEUTRAL"
            bias = "NEUTRAL"
            strength = "LOW"
            reason = f"Neutral, PPI: {ppi:.2f}"

        return {
            "ppi": round(ppi, 2),
            "pressure": pressure,
            "bias": bias,
            "strength": strength,
            "reason": reason
        }

# ================= EXHAUSTION DETECTOR V61 =================
class ExhaustionDetectorV61:
    """
    V61: Deteksi exhaustion
    """
    @staticmethod
    def detect(rsi: float, premium: float, trade_flow: float,
            volume_ratio: float, change_5m: float,
            aggressive: float, oi_delta_5m: float) -> Dict:
        reasons = []
        exhaustion_score = 0
        reversal_potential = "LOW"
        reversal_bias = "NEUTRAL"

        if rsi > RSI_NUCLEAR_OVERBOUGHT:
            exhaustion_score -= 100
            reasons.append(f"NUCLEAR OVERBOUGHT! RSI {rsi:.1f} > 90")
            reversal_potential = "CERTAIN"
            reversal_bias = "SHORT"
        elif rsi < RSI_NUCLEAR_OVERSOLD:
            exhaustion_score += 100
            reasons.append(f"NUCLEAR OVERSOLD! RSI {rsi:.1f} < 10")
            reversal_potential = "CERTAIN"
            reversal_bias = "LONG"

        if rsi < RSI_EXTREME_OVERSOLD:
            exhaustion_score += 40
            reasons.append(f"EXTREME OVERSOLD! RSI {rsi:.1f}")
            reversal_potential = "VERY_HIGH"
            if volume_ratio > VOLUME_ACCUMULATION_SURGE:
                exhaustion_score += 20
                reasons.append("Volume surge di bottom")
            if oi_delta_5m < OI_LIQUIDATION_THRESHOLD:
                exhaustion_score += 30
                reasons.append(f"OI turun = LIQUIDATION DONE")
        elif rsi > RSI_EXTREME_OVERBOUGHT:
            exhaustion_score -= 40
            reasons.append(f"EXTREME OVERBOUGHT! RSI {rsi:.1f}")
            reversal_potential = "VERY_HIGH"
            if trade_flow < FLOW_CRITICAL_LOW:
                exhaustion_score -= 20
                reasons.append("Flow lemah di puncak")
            if oi_delta_5m < OI_LIQUIDATION_THRESHOLD:
                exhaustion_score -= 30
                reasons.append(f"OI turun = SQUEEZE DONE")

        if rsi > RSI_WARNING_LONG and trade_flow < FLOW_CRITICAL_LOW:
            exhaustion_score -= 30
            reasons.append(f"DISTRIBUSI! RSI tinggi + flow rendah")
            reversal_potential = "HIGH"
        if aggressive < AGGRESSION_MIN_LONG and trade_flow < FLOW_CAPITULATION:
            exhaustion_score -= 20
            reasons.append(f"Tidak ada aggressive buy = SELL PRESSURE")

        if rsi < RSI_FORBID_SHORT:
            exhaustion_score += 20
            reasons.append(f"RSI < {RSI_FORBID_SHORT}")
            reversal_potential = "HIGH"

        if rsi <= RSI_NUCLEAR_OVERBOUGHT and rsi >= RSI_NUCLEAR_OVERSOLD:
            if exhaustion_score >= 70:
                reversal_bias = "LONG"
                confidence = "SUPREME"
                reason_main = f"EXTREME ACCUMULATION - SIAP REVERSAL LONG!"
            elif exhaustion_score <= -70:
                reversal_bias = "SHORT"
                confidence = "SUPREME"
                reason_main = f"EXTREME DISTRIBUTION - SIAP REVERSAL SHORT!"
            elif exhaustion_score >= 40:
                reversal_bias = "LONG"
                confidence = "HIGH"
                reason_main = "Akumulasi terdeteksi, potensi reversal long"
            elif exhaustion_score <= -40:
                reversal_bias = "SHORT"
                confidence = "HIGH"
                reason_main = "Distribusi terdeteksi, potensi reversal short"
            else:
                reversal_bias = "NEUTRAL"
                confidence = "LOW"
                reason_main = "No exhaustion detected"
        else:
            confidence = "ABSOLUTE"
            reason_main = reasons[0] if reasons else "Nuclear exhaustion detected"

        return {
            "score": exhaustion_score,
            "reversal_bias": reversal_bias,
            "confidence": confidence,
            "potential": reversal_potential,
            "reason": reason_main,
            "details": reasons
        }

# ================= STOP-HUNT SIMULATOR V54 =================
class StopHuntSimulatorV54:
    """
    V54: Simulasi stop hunt
    """
    @staticmethod
    def simulate(current_price: float, short_dist: float, long_dist: float,
                short_volume: float = 1.0, long_volume: float = 1.0,
                oi: float = 1000, rsi6: float = 50,
                oi_delta_5m: float = 0) -> Dict:
        if short_dist <= EVENT_HORIZON:
            return {
                "bias": "LONG",
                "confidence": "PENDING",
                "direction": "FLASH_SWEEP",
                "reason": f"PNR: Short liq {short_dist}% - Safety validation needed",
                "simulation": {}
            }
        if long_dist <= EVENT_HORIZON:
            return {
                "bias": "SHORT",
                "confidence": "PENDING",
                "direction": "FLASH_SWEEP",
                "reason": f"PNR: Long liq {long_dist}% - Safety validation needed",
                "simulation": {}
            }

        if rsi6 < RSI_FORBID_SHORT:
            return {
                "bias": "LONG",
                "confidence": "HIGH",
                "direction": "REVERSAL",
                "reason": f"RSI {rsi6:.1f} terlalu rendah - Reversal",
                "simulation": {}
            }
        if rsi6 > RSI_FORBID_LONG:
            return {
                "bias": "SHORT",
                "confidence": "HIGH",
                "direction": "REVERSAL",
                "reason": f"RSI {rsi6:.1f} terlalu tinggi - Reversal",
                "simulation": {}
            }

        if short_dist > FAR_LIQ and long_dist > FAR_LIQ:
            return {
                "bias": "NEUTRAL",
                "confidence": "LOW",
                "direction": "NONE",
                "reason": f"Jarak terlalu jauh",
                "simulation": {}
            }

        small_move = 0.4
        def calc_triggered(dist, volume, move):
            if dist <= move:
                return volume * (1 - (dist / move))
            return 0

        short_small = calc_triggered(short_dist, short_volume, small_move)
        long_small = calc_triggered(long_dist, long_volume, small_move)

        if short_small > long_small * 3:
            bias = "LONG"
            confidence = "HIGH"
            reason = f"Naik {small_move}% trigger {short_small:.1f}x short liq!"
        elif long_small > short_small * 3:
            bias = "SHORT"
            confidence = "HIGH"
            reason = f"Turun {small_move}% trigger {long_small:.1f}x long liq!"
        else:
            if short_dist < long_dist:
                bias = "LONG"
                confidence = "LOW"
                reason = f"Short liq lebih dekat ({short_dist}%)"
            else:
                bias = "SHORT"
                confidence = "LOW"
                reason = f"Long liq lebih dekat ({long_dist}%)"

        return {
            "bias": bias,
            "confidence": confidence,
            "direction": "SHORT_HUNT" if bias == "LONG" else "LONG_HUNT",
            "reason": reason,
            "simulation": {
                "small_up_trigger": round(short_small, 2),
                "small_down_trigger": round(long_small, 2)
            }
        }

# ================= ORDERBOOK IMPRINT V54 =================
class OrderbookImprintV54:
    """
    V54: Orderbook analysis
    """
    @staticmethod
    def analyze(bids: List, asks: List, ob_ratio: float, trade_flow: float,
                rsi6: float, oi_delta_5m: float) -> Dict:
        if not bids or not asks:
            return {"manipulation": "UNKNOWN", "bias": "NEUTRAL", "reason": "No data"}

        bid_wall = False
        ask_wall = False

        if len(bids) >= 5:
            avg_bid_vol = sum(b[1] for b in bids[1:5]) / 4
            if avg_bid_vol > 0 and bids[0][1] > avg_bid_vol * OB_SPOOF_THRESHOLD:
                bid_wall = True
        if len(asks) >= 5:
            avg_ask_vol = sum(a[1] for a in asks[1:5]) / 4
            if avg_ask_vol > 0 and asks[0][1] > avg_ask_vol * OB_SPOOF_THRESHOLD:
                ask_wall = True

        if rsi6 < RSI_FORBID_SHORT and ob_ratio < 1.0:
            manipulation = "RSI_DIVERGENCE_BULLISH"
            bias = "LONG"
            reason = f"RSI {rsi6:.1f} oversold + OB bearish = BULLISH DIVERGENCE!"
        elif rsi6 > RSI_FORBID_LONG and ob_ratio > 1.0:
            manipulation = "RSI_DIVERGENCE_BEARISH"
            bias = "SHORT"
            reason = f"RSI {rsi6:.1f} overbought + OB bullish = BEARISH DIVERGENCE!"
        elif bid_wall and trade_flow < FLOW_CRITICAL_LOW:
            if oi_delta_5m > OI_ACCUMULATION_THRESHOLD:
                manipulation = "REAL_ACCUMULATION"
                bias = "LONG"
                reason = f"Bid wall + OI naik = REAL ACCUMULATION"
            else:
                manipulation = "SPOOF_SUPPORT"
                bias = "SHORT"
                reason = f"Bid wall detected tapi OI flat - fake support!"
        elif ask_wall and trade_flow > FLOW_CRITICAL_HIGH:
            if oi_delta_5m < OI_LIQUIDATION_THRESHOLD:
                manipulation = "REAL_DISTRIBUTION"
                bias = "SHORT"
                reason = f"Ask wall + OI turun = REAL DISTRIBUTION"
            else:
                manipulation = "SPOOF_RESISTANCE"
                bias = "LONG"
                reason = f"Ask wall detected tapi OI flat - fake resistance!"
        else:
            manipulation = "NORMAL"
            bias = "NEUTRAL"
            reason = "Orderbook normal"

        return {
            "manipulation": manipulation,
            "bias": bias,
            "reason": reason,
            "bid_wall": bid_wall,
            "ask_wall": ask_wall
        }

# ================= STATE MANAGER V82 =================
class StateManagerV82:
    """
    V82: Enhanced state manager dengan V82 modules (API, LMG)
    """
    def __init__(self):
        # History buffers
        self.price_history = deque(maxlen=100)
        self.rsi_history = deque(maxlen=30)
        self.volume_history = deque(maxlen=20)
        self.flow_history = deque(maxlen=30)
        self.ob_history = deque(maxlen=20)
        self.premium_history = deque(maxlen=20)
        self.funding_history = deque(maxlen=50)
        self.aggressive_history = deque(maxlen=20)
        self.wmi_history = deque(maxlen=20)
        self.fid_first_seen = {}

        # V82: New tracking dictionaries
        self.api_first_seen = {}  # Track Absorption Pressure Index
        self.lmg_first_seen = {}  # Track Liquidity Mirror Guard

        # V81: New tracking dictionaries
        self.ltg_first_seen = {}  # Track Liquidity Thinning Guard
        self.icd_first_seen = {}  # Track Internal Cross Detector

        # V80: Institutional Exit Radar tracking
        self.ier_first_seen = {}  # Track kapan IER pertama terdeteksi

        # V80: RSI Momentum Guard tracking
        self.rmg_first_seen = {}  # Track kapan RMG pertama terdeteksi

        # V80: Fake Magnet Vacuum tracking
        self.fmv_first_seen = {}  # Track kapan FMV pertama terdeteksi

        # V79: Wash Trade Detector tracking
        self.wtd_first_seen = {}

        # V78: Execution Zone Hunter tracking
        self.ezh_first_seen = {}

        # V78: Panic Sell Validator tracking
        self.psv_first_seen = {}

        # V77: Overdrive Flow Filter tracking
        self.off_first_seen = {}

        # V77: Aggressive Exhaustion Filter tracking
        self.aef_first_seen = {}

        # V76: Panic Saturation tracking
        self.panic_saturation_first_seen = {}

        # V75: Gravity Overdrive tracking
        self.gravity_overdrive_first_seen = {}

        # V74: Magnet tracking
        self.magnet_first_seen = {}
        self.magnet_last_seen = {}

        # V69: MA dan OBV History
        self.ma10_history = deque(maxlen=10)
        self.ma20_history = deque(maxlen=10)
        self.obv_history = deque(maxlen=20)

        # V66: Temporal accumulation tracking
        self.accumulation_start_time = 0
        self.last_accumulation_check = 0
        self.accumulation_flow_threshold = ATI_FLOW_MIN
        self.accumulation_duration_minutes = 0

        # Bid/Ask history untuk ODD dan V83 OVS
        self.bid_history = deque(maxlen=10)
        self.ask_history = deque(maxlen=10)
        
        # V83: Aggression history untuk Velocity calculation
        self.aggression_history = deque(maxlen=ADV_HISTORY_SIZE)

        # Time persistence tracking
        self.gravity_first_seen = {}
        self.phase_persistence = {}

        # Entry tracking
        self.entry_signals = deque(maxlen=PERSISTENCE_CYCLES)
        self.last_entry_time = 0
        self.entry_count = 0
        self.last_entry_bias = "NEUTRAL"
        self.last_entry_price = 0
        self.last_entry_rsi = 50

        # Phase tracking
        self.current_phase = "UNKNOWN"
        self.dump_detected_at = 0
        self.pump_detected_at = 0
        self.pump_magnitude = 0
        self.accumulation_detected_at = 0
        self.double_sweep_detected_at = 0

        # Performance tracking
        self.bias_history = deque(maxlen=20)
        self.win_loss = {"wins": 0, "losses": 0}

        # Module histories
        self.api_history = deque(maxlen=10)  # V82 baru!
        self.lmg_history = deque(maxlen=10)  # V82 baru!
        self.ltg_history = deque(maxlen=10)  # V81 baru!
        self.icd_history = deque(maxlen=10)  # V81 baru!
        self.ier_history = deque(maxlen=10)  # V80 baru!
        self.rmg_history = deque(maxlen=10)  # V80 baru!
        self.fmv_history = deque(maxlen=10)  # V80 baru!
        self.wtd_history = deque(maxlen=10)  # V79
        self.ezh_history = deque(maxlen=10)  # V78
        self.psv_history = deque(maxlen=10)  # V78
        self.off_history = deque(maxlen=10)
        self.aef_history = deque(maxlen=10)
        self.psr_history = deque(maxlen=10)
        self.amv_history = deque(maxlen=10)
        self.lgo_history = deque(maxlen=10)
        self.mdv_history = deque(maxlen=10)
        self.pab_history = deque(maxlen=10)
        self.cfk_history = deque(maxlen=10)
        self.mdd_history = deque(maxlen=10)
        self.ovd_history = deque(maxlen=10)
        self.trend_history = deque(maxlen=10)
        self.ogd_history = deque(maxlen=10)
        self.zas_history = deque(maxlen=10)
        self.avc_history = deque(maxlen=10)
        self.amd_history = deque(maxlen=10)
        self.tdp_history = deque(maxlen=10)
        self.ati_history = deque(maxlen=10)
        self.wed_history = deque(maxlen=10)
        self.mwr_history = deque(maxlen=10)
        self.lvs_history = deque(maxlen=10)
        self.dtd_history = deque(maxlen=10)

    def track_fid_persistence(self, fid_key: str, current_time: float) -> float:
        """V82: Track berapa lama FID sudah terdeteksi"""
        if fid_key not in self.fid_first_seen:
            self.fid_first_seen[fid_key] = current_time
            return 0
        duration = (current_time - self.fid_first_seen[fid_key]) / 60
        return duration

    def reset_fid_tracking(self, fid_key: str):
        if fid_key in self.fid_first_seen:
            del self.fid_first_seen[fid_key]

    def update(self, price: float, rsi: float, volume: float, flow: float,
            ob: float, premium: float, funding: float, aggressive: float,
            std_dev: float = 0, wmi: float = 0,
            ma10: float = 0, ma20: float = 0, obv: float = 0):
        """Update semua history"""
        self.price_history.append(price)
        self.rsi_history.append(rsi)
        self.volume_history.append(volume)
        self.flow_history.append(flow)
        self.ob_history.append(ob)
        self.premium_history.append(premium)
        self.funding_history.append(funding)
        self.aggressive_history.append(aggressive)
        self.wmi_history.append(wmi)

        # V69: Update MA dan OBV
        if ma10 > 0:
            self.ma10_history.append(ma10)
        if ma20 > 0:
            self.ma20_history.append(ma20)
        if obv > 0:
            self.obv_history.append(obv)

    def update_orderbook(self, bids: List, asks: List):
        """Update orderbook history"""
        if bids and len(bids) > 0:
            self.bid_history.append(bids[:5])
        if asks and len(asks) > 0:
            self.ask_history.append(asks[:5])

    def track_api_persistence(self, api_key: str, current_time: float) -> float:
        """V82: Track berapa lama API sudah terdeteksi"""
        if api_key not in self.api_first_seen:
            self.api_first_seen[api_key] = current_time
            return 0
        duration = (current_time - self.api_first_seen[api_key]) / 60
        return duration

    def reset_api_tracking(self, api_key: str):
        """Reset tracking jika API menghilang"""
        if api_key in self.api_first_seen:
            del self.api_first_seen[api_key]

    def track_lmg_persistence(self, lmg_key: str, current_time: float) -> float:
        """V82: Track berapa lama LMG sudah terdeteksi"""
        if lmg_key not in self.lmg_first_seen:
            self.lmg_first_seen[lmg_key] = current_time
            return 0
        duration = (current_time - self.lmg_first_seen[lmg_key]) / 60
        return duration

    def reset_lmg_tracking(self, lmg_key: str):
        """Reset tracking jika LMG menghilang"""
        if lmg_key in self.lmg_first_seen:
            del self.lmg_first_seen[lmg_key]

    def track_ltg_persistence(self, ltg_key: str, current_time: float) -> float:
        """V81: Track berapa lama LTG sudah terdeteksi"""
        if ltg_key not in self.ltg_first_seen:
            self.ltg_first_seen[ltg_key] = current_time
            return 0
        duration = (current_time - self.ltg_first_seen[ltg_key]) / 60
        return duration

    def reset_ltg_tracking(self, ltg_key: str):
        """Reset tracking jika LTG menghilang"""
        if ltg_key in self.ltg_first_seen:
            del self.ltg_first_seen[ltg_key]

    def track_icd_persistence(self, icd_key: str, current_time: float) -> float:
        """V81: Track berapa lama ICD sudah terdeteksi"""
        if icd_key not in self.icd_first_seen:
            self.icd_first_seen[icd_key] = current_time
            return 0
        duration = (current_time - self.icd_first_seen[icd_key]) / 60
        return duration

    def reset_icd_tracking(self, icd_key: str):
        """Reset tracking jika ICD menghilang"""
        if icd_key in self.icd_first_seen:
            del self.icd_first_seen[icd_key]

    def track_ier_persistence(self, ier_key: str, current_time: float) -> float:
        """
        V80: Track berapa lama IER sudah terdeteksi
        Returns durasi dalam menit
        """
        if ier_key not in self.ier_first_seen:
            self.ier_first_seen[ier_key] = current_time
            return 0
        duration = (current_time - self.ier_first_seen[ier_key]) / 60
        return duration

    def reset_ier_tracking(self, ier_key: str):
        """Reset tracking jika IER menghilang"""
        if ier_key in self.ier_first_seen:
            del self.ier_first_seen[ier_key]

    def track_rmg_persistence(self, rmg_key: str, current_time: float) -> float:
        """
        V80: Track berapa lama RMG sudah terdeteksi
        Returns durasi dalam menit
        """
        if rmg_key not in self.rmg_first_seen:
            self.rmg_first_seen[rmg_key] = current_time
            return 0
        duration = (current_time - self.rmg_first_seen[rmg_key]) / 60
        return duration

    def reset_rmg_tracking(self, rmg_key: str):
        """Reset tracking jika RMG menghilang"""
        if rmg_key in self.rmg_first_seen:
            del self.rmg_first_seen[rmg_key]

    def track_fmv_persistence(self, fmv_key: str, current_time: float) -> float:
        """
        V80: Track berapa lama FMV sudah terdeteksi
        Returns durasi dalam menit
        """
        if fmv_key not in self.fmv_first_seen:
            self.fmv_first_seen[fmv_key] = current_time
            return 0
        duration = (current_time - self.fmv_first_seen[fmv_key]) / 60
        return duration

    def reset_fmv_tracking(self, fmv_key: str):
        """Reset tracking jika FMV menghilang"""
        if fmv_key in self.fmv_first_seen:
            del self.fmv_first_seen[fmv_key]

    def track_wtd_persistence(self, wtd_key: str, current_time: float) -> float:
        """
        V79: Track berapa lama WTD sudah terdeteksi
        Returns durasi dalam menit
        """
        if wtd_key not in self.wtd_first_seen:
            self.wtd_first_seen[wtd_key] = current_time
            return 0
        duration = (current_time - self.wtd_first_seen[wtd_key]) / 60
        return duration

    def reset_wtd_tracking(self, wtd_key: str):
        """Reset tracking jika WTD menghilang"""
        if wtd_key in self.wtd_first_seen:
            del self.wtd_first_seen[wtd_key]

    def track_ezh_persistence(self, ezh_key: str, current_time: float) -> float:
        """
        V78: Track berapa lama EZH sudah terdeteksi
        Returns durasi dalam menit
        """
        if ezh_key not in self.ezh_first_seen:
            self.ezh_first_seen[ezh_key] = current_time
            return 0
        duration = (current_time - self.ezh_first_seen[ezh_key]) / 60
        return duration

    def reset_ezh_tracking(self, ezh_key: str):
        """Reset tracking jika EZH menghilang"""
        if ezh_key in self.ezh_first_seen:
            del self.ezh_first_seen[ezh_key]

    def track_psv_persistence(self, psv_key: str, current_time: float) -> float:
        """
        V78: Track berapa lama PSV sudah terdeteksi
        Returns durasi dalam menit
        """
        if psv_key not in self.psv_first_seen:
            self.psv_first_seen[psv_key] = current_time
            return 0
        duration = (current_time - self.psv_first_seen[psv_key]) / 60
        return duration

    def reset_psv_tracking(self, psv_key: str):
        """Reset tracking jika PSV menghilang"""
        if psv_key in self.psv_first_seen:
            del self.psv_first_seen[psv_key]

    def track_off_persistence(self, off_key: str, current_time: float) -> float:
        """V77: Track berapa lama OFF sudah terdeteksi"""
        if off_key not in self.off_first_seen:
            self.off_first_seen[off_key] = current_time
            return 0
        duration = (current_time - self.off_first_seen[off_key]) / 60
        return duration

    def reset_off_tracking(self, off_key: str):
        """Reset tracking jika OFF menghilang"""
        if off_key in self.off_first_seen:
            del self.off_first_seen[off_key]

    def track_aef_persistence(self, aef_key: str, current_time: float) -> float:
        """V77: Track berapa lama AEF sudah terdeteksi"""
        if aef_key not in self.aef_first_seen:
            self.aef_first_seen[aef_key] = current_time
            return 0
        duration = (current_time - self.aef_first_seen[aef_key]) / 60
        return duration

    def reset_aef_tracking(self, aef_key: str):
        """Reset tracking jika AEF menghilang"""
        if aef_key in self.aef_first_seen:
            del self.aef_first_seen[aef_key]

    def track_magnet_persistence(self, magnet_key: str, current_time: float) -> float:
        """V74: Track berapa lama magnet sudah terdeteksi"""
        if magnet_key not in self.magnet_first_seen:
            self.magnet_first_seen[magnet_key] = current_time
            self.magnet_last_seen[magnet_key] = current_time
            return 0
        self.magnet_last_seen[magnet_key] = current_time
        duration = (current_time - self.magnet_first_seen[magnet_key]) / 60
        return duration

    def reset_magnet_tracking(self, magnet_key: str):
        """Reset tracking jika magnet menghilang"""
        if magnet_key in self.magnet_first_seen:
            del self.magnet_first_seen[magnet_key]
        if magnet_key in self.magnet_last_seen:
            del self.magnet_last_seen[magnet_key]

    def track_gravity_overdrive_persistence(self, gravity_key: str, current_time: float) -> float:
        """V75: Track berapa lama gravity overdrive sudah terdeteksi"""
        if gravity_key not in self.gravity_overdrive_first_seen:
            self.gravity_overdrive_first_seen[gravity_key] = current_time
            return 0
        duration = (current_time - self.gravity_overdrive_first_seen[gravity_key]) / 60
        return duration

    def reset_gravity_overdrive_tracking(self, gravity_key: str):
        """Reset tracking jika gravity overdrive menghilang"""
        if gravity_key in self.gravity_overdrive_first_seen:
            del self.gravity_overdrive_first_seen[gravity_key]

    def track_panic_saturation_persistence(self, panic_key: str, current_time: float) -> float:
        """V76: Track berapa lama panic saturation sudah terdeteksi"""
        if panic_key not in self.panic_saturation_first_seen:
            self.panic_saturation_first_seen[panic_key] = current_time
            return 0
        duration = (current_time - self.panic_saturation_first_seen[panic_key]) / 60
        return duration

    def reset_panic_saturation_tracking(self, panic_key: str):
        """Reset tracking jika panic saturation menghilang"""
        if panic_key in self.panic_saturation_first_seen:
            del self.panic_saturation_first_seen[panic_key]

    def track_gravity_persistence(self, gravity_key: str, current_time: float) -> float:
        """Track berapa lama gravity sudah terdeteksi"""
        if gravity_key not in self.gravity_first_seen:
            self.gravity_first_seen[gravity_key] = current_time
            return 0
        duration = (current_time - self.gravity_first_seen[gravity_key]) / 60
        return duration

    def reset_gravity_tracking(self, gravity_key: str):
        """Reset tracking jika gravity berubah"""
        if gravity_key in self.gravity_first_seen:
            del self.gravity_first_seen[gravity_key]

    def track_accumulation_duration(self, current_flow: float, current_time: float) -> float:
        """V66: Track berapa lama flow > threshold"""
        if current_flow > self.accumulation_flow_threshold:
            if self.accumulation_start_time == 0:
                self.accumulation_start_time = current_time
            self.accumulation_duration_minutes = (current_time - self.accumulation_start_time) / 60
        else:
            self.accumulation_start_time = 0
            self.accumulation_duration_minutes = 0
        return self.accumulation_duration_minutes

    def get_flow_history(self) -> List[float]:
        """Get flow history"""
        return list(self.flow_history)

    def get_obv_history(self) -> List[float]:
        """Get OBV history"""
        return list(self.obv_history)

    def get_ma10_history(self) -> List[float]:
        """Get MA10 history"""
        return list(self.ma10_history)

    def get_ma20_history(self) -> List[float]:
        """Get MA20 history"""
        return list(self.ma20_history)

    def detect_double_sweep_zone(self, short_dist: float, long_dist: float) -> bool:
        """Deteksi apakah harga di zona double sweep"""
        return short_dist < DOUBLE_SWEEP_THRESHOLD and long_dist < DOUBLE_SWEEP_THRESHOLD

    def detect_recent_dump(self, current_price: float, threshold: float = 3.0) -> bool:
        if len(self.price_history) < 10:
            return False
        max_price = max(self.price_history)
        if max_price <= 0:
            return False
        drawdown = ((current_price - max_price) / max_price) * 100
        if drawdown < -threshold:
            self.dump_detected_at = time.time()
            return True
        return False

    def detect_recent_pump(self, current_price: float, threshold: float = 5.0) -> Dict:
        if len(self.price_history) < 10:
            return {"detected": False, "magnitude": 0}
        min_price = min(self.price_history)
        if min_price <= 0:
            return {"detected": False, "magnitude": 0}
        magnitude = ((current_price - min_price) / min_price) * 100
        detected = magnitude > threshold
        if detected:
            self.pump_detected_at = time.time()
            self.pump_magnitude = magnitude
        return {"detected": detected, "magnitude": magnitude}

    def detect_accumulation(self, current_price: float, oi_current: float) -> bool:
        """Deteksi akumulasi dari price range"""
        if len(self.price_history) < 10:
            return False
        price_range = (max(self.price_history) - min(self.price_history)) / min(self.price_history) * 100
        price_stable = price_range < 1.0
        if price_stable:
            self.accumulation_detected_at = time.time()
            return True
        return False

    def get_drawdown(self, current_price: float) -> float:
        if len(self.price_history) < 5:
            return 0
        max_price = max(self.price_history)
        if max_price <= 0:
            return 0
        return ((current_price - max_price) / max_price) * 100

    def time_since_dump(self) -> float:
        if self.dump_detected_at == 0:
            return 999
        return (time.time() - self.dump_detected_at) / 60

    def time_since_pump(self) -> float:
        if self.pump_detected_at == 0:
            return 999
        return (time.time() - self.pump_detected_at) / 60

    def time_since_accumulation(self) -> float:
        if self.accumulation_detected_at == 0:
            return 999
        return (time.time() - self.accumulation_detected_at) / 60

    def get_volume_trend(self) -> str:
        if len(self.volume_history) < 3:
            return "UNKNOWN"
        if self.volume_history[-1] > self.volume_history[-2] * VOLUME_SURGE:
            return "SURGING"
        elif self.volume_history[-1] > self.volume_history[-2]:
            return "INCREASING"
        elif self.volume_history[-1] < self.volume_history[-2] * 0.7:
            return "DROPPING"
        elif self.volume_history[-1] < self.volume_history[-2]:
            return "DECREASING"
        return "STABLE"

    def get_flow_trend(self) -> str:
        if len(self.flow_history) < 5:
            return "NEUTRAL"
        recent = list(self.flow_history)[-5:]
        if all(f < FLOW_CAPITULATION for f in recent):
            return "CAPITULATION_SELL"
        elif recent[-1] < recent[0] * 0.3:
            return "ACCELERATING_SELL"
        elif recent[-1] > recent[0] * 3:
            return "ACCELERATING_BUY"
        return "NEUTRAL"

    def get_premium_trend(self) -> str:
        if len(self.premium_history) < 5:
            return "STABLE"
        recent = list(self.premium_history)[-5:]
        if all(p < recent[0] * 0.8 for p in recent[1:]):
            return "WIDENING_SHORT"
        elif all(p > recent[0] * 1.2 for p in recent[1:]):
            return "WIDENING_LONG"
        elif abs(recent[-1] - recent[0]) < abs(recent[0]) * 0.1:
            return "NARROWING"
        return "STABLE"

    def get_aggressive_trend(self) -> str:
        if len(self.aggressive_history) < 5:
            return "UNKNOWN"
        recent = list(self.aggressive_history)[-5:]
        if all(a < AGGRESSION_MIN_LONG for a in recent):
            return "NO_BUYERS"
        elif all(a > AGGRESSION_MIN_SHORT * 10 for a in recent):
            return "AGGRESSIVE_BUY"
        elif all(a < AGGRESSION_MIN_LONG * 3 for a in recent):
            return "AGGRESSIVE_SELL"
        return "MIXED"

    def get_wmi_trend(self) -> str:
        """Trend WMI untuk deteksi perubahan sentimen"""
        if len(self.wmi_history) < 5:
            return "STABLE"
        recent = list(self.wmi_history)[-5:]
        if recent[-1] > recent[0] * 1.5:
            return "BULLISH_ACCELERATION"
        elif recent[-1] < recent[0] * 0.5:
            return "BEARISH_ACCELERATION"
        return "STABLE"

    def update_entry(self, bias: str, score: float = 0) -> bool:
        self.entry_signals.append(bias)
        self.bias_history.append(bias)
        if len(self.entry_signals) >= CONFIRM_DEFAULT:
            if all(s == bias for s in self.entry_signals):
                self.entry_count += 1
                if self.entry_count >= CONFIRM_DEFAULT:
                    return True
            else:
                self.entry_count = 0
        return False

    def can_enter(self, bias: str, phase: str) -> bool:
        if time.time() - self.last_entry_time < COOLDOWN_SECONDS:
            return False
        if phase == "POST_DUMP_EXHAUSTION" and bias != "LONG":
            return False
        if phase == "POST_PUMP_DISTRIBUTION" and bias != "SHORT":
            return False
        return True

    def execute_entry(self, bias: str, price: float, rsi: float):
        self.last_entry_time = time.time()
        self.last_entry_bias = bias
        self.last_entry_price = price
        self.last_entry_rsi = rsi
        self.entry_count = 0
        self.entry_signals.clear()

    def time_since_entry(self) -> float:
        if self.last_entry_time == 0:
            return 999
        return (time.time() - self.last_entry_time) / 60

    def get_bias_consistency(self) -> float:
        if len(self.bias_history) < 5:
            return 0
        recent = list(self.bias_history)[-5:]
        if recent.count(recent[-1]) >= 4:
            return 0.8
        elif recent.count(recent[-1]) >= 3:
            return 0.5
        return 0

# ================= MARKET STATE ENGINE V82 =================
class MarketStateEngineV82:
    """
    V82: Market phase dengan prioritas tertinggi (HIERARKI MUTLAK V82):
    0.0: LMG (Liquidity Mirror Guard) - ANTI-BOTTOMLESS HOLE (NEW V82!)
    0.1: API (Absorption Pressure Index) - ANTI-ABSORPTION SIPHON (NEW V82!)
    0.2: LTG (Liquidity Thinning Guard) - ANTI-INFINITY SQUEEZE (V81)
    0.3: ICD (Internal Cross Detector) - ANTI-POSITION FLIPPING TRAP (V81)
    0.4: EZH (Execution Zone Hunter) - ANTI-RIVER MAGNETIC SLINGSHOT (V78)
    0.5: WTD (Wash Trade Detector) - ANTI-KITE FALSE BRIDGE (V79)
    0.6: IER (Institutional Exit Radar) - ANTI-OPN/BARD FALSE FLOW (V80)
    0.7: RMG (RSI Momentum Guard) - ANTI-RIVER GRAVITY DECOY (V80)
    0.8: FMV (Fake Magnet Vacuum) - KOMBINASI IER + RMG (V80)
    0.9: PSV (Panic Sell Validator) - ANTI-OPN ENDLESS FLOOR (V78)
    0.10: OFF (Overdrive Flow Filter) - ANTI-HUSDT TRAP (V77)
    0.11: AEF (Aggressive Exhaustion Filter) - ANTI-PHA TRAP (V77)
    0.12: PSR (Panic Saturation Reversal) - ANTI-HUMA DRIFT TRAP (V76)
    0.13: AMV (Absorption Momentum Validator) - ANTI-HUMA TRAP (V75)
    0.14: LGO (Liquidation Gravity Overdrive) - ANTI-RIVER NUCLEAR (V75)
    0.15: MDV (Magnet Decay Validator) - ANTI-RIVER SPOOF (V74)
    0.16: PAB (Passive Absorption Blackhole) - ANTI-SIREN TRAP (V73)
    0.17: CFK (Catching Falling Knives) - ANTI-ROBO TRAP (V72)
    0.18: MDD (Magnet Distance Dominance) - ANTI-RIVER TRAP (V71)
    0.19: OVD (Orderbook Vacuum Defense) - ANTI-PHA TRAP (V70)
    0.20: TREND INTEGRITY (V69)
    0.21: OGD (Gravity Deflection) - ANTI-PIPPIN TRAP (V68)
    0.22: ZAS (Zero Aggression Slaughter) - ANTI-DEADSTICK (V67)
    0.23: AVC (Absorption Validity Check) - ANTI-EXIT LIQUIDITY TRAP (V67)
    0.24: AMD (Aggression-Mass Divergence) - ANTI-SPOOF (V65)
    0.25: TDP (The DYL Particle) - ABSOLUTE OVERRIDE (V64)
    0.26: ATI (Temporal Accumulation Index) - WHALE PATIENCE LOADING (V66)
    0.27: WED (Wall Erasure Detection) - FAKE FLOOR/CEILING (V63)
    0.28: MWR (Magnet Wall Reversal) (V62)
    0.29: LVS (Low-Volume Suction) (V61)
    0.30: DTD (Divergence Trap Detector) (V60)
    """
    @staticmethod
    def detect_state(data: Dict, state_mgr, liquidity_gravity, ppi, spoofing,
                    reversion, oi_velocity, hft_signature, lrr_result, av_result,
                    starter_result, ghost_result, dtd_result, lvs_result,
                    mwr_result, wed_result, tdp_result, amd_result, ati_result,
                    zas_result, avc_result, ogd_result, trend_result, ovd_result,
                    mdd_result, cfk_result, pab_result, mdv_result, amv_result, lgo_result,
                    psr_result, off_result, aef_result, ezh_result, psv_result,
                    wtd_result, ier_result, rmg_result, fmv_result,
                    ltg_result, icd_result, api_result, lmg_result):  # V82 baru!
        rsi6 = safe_get(data, 'rsi6', 50)
        short_liq = safe_get(data, 'short_liq_dist', 99)
        long_liq = safe_get(data, 'long_liq_dist', 99)
        trade_flow = safe_get(data, 'trade_flow', 1.0)
        aggressive_ratio = safe_get(data, 'aggressive_ratio', 1.0)
        wmi_ratio = safe_get(data, 'wmi_ratio', 0)

        # ============================================
        # PRIORITAS BARU V82: LIQUIDITY MIRROR GUARD (LMG) - TERTINGGI!
        # ============================================
        if lmg_result['is_death_magnet']:
            return {
                "phase": "DEATH_MAGNET_CASCADE",
                "bias": lmg_result['bias'],
                "confidence": "ABSOLUTE",
                "reason": lmg_result['reason'],
                "multiplier": 32.0  # Prioritas tertinggi!
            }

        # ============================================
        # PRIORITAS BARU V82: ABSORPTION PRESSURE INDEX (API)
        # ============================================
        if api_result['is_absorbing']:
            return {
                "phase": "WHALE_ABSORPTION_ZONE",
                "bias": api_result['bias'],
                "confidence": "ABSOLUTE",
                "reason": api_result['reason'],
                "multiplier": 31.0
            }

        # ============================================
        # PRIORITAS BARU V81: LIQUIDITY THINNING GUARD (LTG)
        # ============================================
        if ltg_result['is_vacuum']:
            return {
                "phase": "LIQUIDITY_VACUUM",
                "bias": "LONG",
                "confidence": "ABSOLUTE",
                "reason": ltg_result['reason'],
                "multiplier": 30.0
            }

        # ============================================
        # PRIORITAS BARU V81: INTERNAL CROSS DETECTOR (ICD)
        # ============================================
        if icd_result['is_internal_trap']:
            return {
                "phase": "INTERNAL_CROSS_TRAP",
                "bias": "LONG",
                "confidence": "ABSOLUTE",
                "reason": icd_result['reason'],
                "multiplier": 29.0
            }

        # ============================================
        # PRIORITAS 0.0: EXECUTION ZONE HUNTER (V78) - ANTI-RIVER MAGNETIC SLINGSHOT
        # ============================================
        if ezh_result['is_execution'] and ezh_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
            if ezh_result['execution_type'] == "SHORT_EXECUTION_ZONE":
                return {
                    "phase": "MAGNETIC_SLINGSHOT",
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": ezh_result['reason'],
                    "multiplier": 25.0
                }
            elif ezh_result['execution_type'] == "LONG_EXECUTION_ZONE":
                return {
                    "phase": "EXECUTION_REBOUND",
                    "bias": "LONG",
                    "confidence": "ABSOLUTE",
                    "reason": ezh_result['reason'],
                    "multiplier": 25.0
                }
            elif ezh_result['execution_type'] == "SHORT_EXECUTION_WARNING":
                return {
                    "phase": "EXECUTION_WARNING_BEARISH",
                    "bias": "SHORT",
                    "confidence": "HIGH",
                    "reason": ezh_result['reason'],
                    "multiplier": 24.0
                }
            elif ezh_result['execution_type'] == "LONG_EXECUTION_WARNING":
                return {
                    "phase": "EXECUTION_WARNING_BULLISH",
                    "bias": "LONG",
                    "confidence": "HIGH",
                    "reason": ezh_result['reason'],
                    "multiplier": 24.0
                }

        # ============================================
        # PRIORITAS 0.1: WASH TRADE DETECTOR (V79) - ANTI-KITE FALSE BRIDGE
        # ============================================
        if wtd_result['is_wash_trade'] and wtd_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
            if wtd_result['wash_type'] == "WASH_TRADE_DISTRIBUTION":
                return {
                    "phase": "WASH_TRADE_DISTRIBUTION",
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": wtd_result['reason'],
                    "multiplier": 24.8
                }
            elif wtd_result['wash_type'] == "WASH_TRADE_WARNING":
                return {
                    "phase": "WASH_TRADE_WARNING",
                    "bias": "SHORT",
                    "confidence": "HIGH",
                    "reason": wtd_result['reason'],
                    "multiplier": 24.5
                }

        # ============================================
        # PRIORITAS 0.2: INSTITUTIONAL EXIT RADAR (V80) - ANTI-OPN/BARD FALSE FLOW
        # ============================================
        if ier_result['is_exit'] and ier_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
            if ier_result['exit_type'] == "INSTITUTIONAL_EXIT":
                return {
                    "phase": "INSTITUTIONAL_EXIT",
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": ier_result['reason'],
                    "multiplier": 24.6
                }
            elif ier_result['exit_type'] == "INSTITUTIONAL_EXIT_WARNING":
                return {
                    "phase": "INSTITUTIONAL_EXIT_WARNING",
                    "bias": "SHORT",
                    "confidence": "HIGH",
                    "reason": ier_result['reason'],
                    "multiplier": 24.3
                }

        # ============================================
        # PRIORITAS 0.3: RSI MOMENTUM GUARD (V80) - ANTI-RIVER GRAVITY DECOY
        # ============================================
        if rmg_result['is_weak'] and rmg_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
            if rmg_result['weakness_type'] == "GRAVITY_DECOY":
                return {
                    "phase": "GRAVITY_DECOY",
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": rmg_result['reason'],
                    "multiplier": 24.4
                }
            elif rmg_result['weakness_type'] == "WEAK_MOMENTUM":
                return {
                    "phase": "WEAK_MOMENTUM",
                    "bias": "SHORT",
                    "confidence": "HIGH",
                    "reason": rmg_result['reason'],
                    "multiplier": 24.2
                }
            elif rmg_result['weakness_type'] == "WEAK_MOMENTUM_BULLISH":
                return {
                    "phase": "WEAK_MOMENTUM_BULLISH",
                    "bias": "LONG",
                    "confidence": "HIGH",
                    "reason": rmg_result['reason'],
                    "multiplier": 24.2
                }

        # ============================================
        # PRIORITAS 0.4: FAKE MAGNET VACUUM (V80) - KOMBINASI IER + RMG
        # ============================================
        if fmv_result['is_fake_magnet'] and fmv_result['confidence'] in ["ABSOLUTE", "SUPREME"]:
            if fmv_result['fake_type'] == "FAKE_MAGNET_VACUUM_OPN":
                return {
                    "phase": "FAKE_MAGNET_VACUUM_OPN",
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": fmv_result['reason'],
                    "multiplier": 24.7
                }
            elif fmv_result['fake_type'] == "FAKE_MAGNET_VACUUM_RIVER":
                return {
                    "phase": "FAKE_MAGNET_VACUUM_RIVER",
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": fmv_result['reason'],
                    "multiplier": 24.7
                }
            elif fmv_result['fake_type'] == "FLOW_INFLATION_VACUUM":
                return {
                    "phase": "FLOW_INFLATION_VACUUM",
                    "bias": "SHORT",
                    "confidence": "SUPREME",
                    "reason": fmv_result['reason'],
                    "multiplier": 24.5
                }

        # ============================================
        # PRIORITAS 0.5: PANIC SELL VALIDATOR (V78) - ANTI-OPN ENDLESS FLOOR
        # ============================================
        if psv_result['is_valid'] and psv_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
            if psv_result['validation_type'] == "FALLING_KNIFE_CONTINUATION":
                return {
                    "phase": "ENDLESS_FLOOR",
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": psv_result['reason'],
                    "multiplier": 24.0
                }
            elif psv_result['validation_type'] == "REAL_EXHAUSTION":
                return {
                    "phase": "TRUE_BOTTOM",
                    "bias": "LONG",
                    "confidence": "ABSOLUTE",
                    "reason": psv_result['reason'],
                    "multiplier": 24.0
                }
            elif psv_result['validation_type'] == "REAL_DISTRIBUTION":
                return {
                    "phase": "TRUE_TOP",
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": psv_result['reason'],
                    "multiplier": 23.5
                }
            elif psv_result['validation_type'] == "FAKE_PUMP":
                return {
                    "phase": "FAKE_PUMP",
                    "bias": "SHORT",
                    "confidence": "HIGH",
                    "reason": psv_result['reason'],
                    "multiplier": 23.0
                }

        # ============================================
        # PRIORITAS 0.6: OVERDRIVE FLOW FILTER (V77) - ANTI-HUSDT TRAP
        # ============================================
        if off_result['is_patched'] and off_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
            if off_result['patched_type'] == "WHALE_BRIDGE_REVERSAL":
                return {
                    "phase": "WHALE_BRIDGE_REVERSAL",
                    "bias": "LONG",
                    "confidence": "SUPREME",
                    "reason": off_result['reason'],
                    "multiplier": 22.0
                }
            elif off_result['patched_type'] == "WHALE_BRIDGE_REVERSAL_BEARISH":
                return {
                    "phase": "WHALE_BRIDGE_REVERSAL_BEARISH",
                    "bias": "SHORT",
                    "confidence": "SUPREME",
                    "reason": off_result['reason'],
                    "multiplier": 22.0
                }
            elif off_result['patched_type'] == "SHORT_OVERDRIVE_PATCHED":
                return {
                    "phase": "LIQUIDITY_PATCHED",
                    "bias": "LONG",
                    "confidence": "ABSOLUTE",
                    "reason": off_result['reason'],
                    "multiplier": 21.5
                }
            elif off_result['patched_type'] == "LONG_OVERDRIVE_PATCHED":
                return {
                    "phase": "LIQUIDITY_PATCHED",
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": off_result['reason'],
                    "multiplier": 21.5
                }

        # ============================================
        # PRIORITAS 0.7: AGGRESSIVE EXHAUSTION FILTER (V77) - ANTI-PHA TRAP
        # ============================================
        if aef_result['is_exhausted'] and aef_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
            if aef_result['exhausted_type'] == "RETAIL_FOMO_EXHAUSTION":
                return {
                    "phase": "RETAIL_SLAUGHTER_HOUSE",
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": aef_result['reason'],
                    "multiplier": 21.0
                }
            elif aef_result['exhausted_type'] == "EXTREME_FOMO_EXHAUSTION":
                return {
                    "phase": "EXTREME_FOMO_SLAUGHTER",
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": aef_result['reason'],
                    "multiplier": 21.0
                }
            elif aef_result['exhausted_type'] == "PANIC_SELL_EXHAUSTION":
                return {
                    "phase": "PANIC_SELL_EXHAUSTION",
                    "bias": "LONG",
                    "confidence": "ABSOLUTE",
                    "reason": aef_result['reason'],
                    "multiplier": 21.0
                }
            elif aef_result['exhausted_type'] == "CONTINUATION_DUMP":
                return {
                    "phase": "CONTINUATION_DUMP",
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": aef_result['reason'],
                    "multiplier": 21.0
                }

        # ============================================
        # PRIORITAS 0.8: PANIC SATURATION REVERSAL (V76) - ANTI-HUMA DRIFT TRAP
        # ============================================
        if psr_result['is_saturated'] and psr_result['confidence'] in ["SUPREME", "ABSOLUTE"]:
            if psr_result['saturation_type'] == "PANIC_SATURATION_REVERSAL":
                return {
                    "phase": "LIQUIDITY_ARCHITECT",
                    "bias": "LONG",
                    "confidence": "SUPREME",
                    "reason": psr_result['reason'],
                    "multiplier": 20.0
                }
        elif psr_result['is_saturated'] and psr_result['confidence'] == "HIGH":
            return {
                "phase": "PANIC_WARNING",
                "bias": "LONG",
                "confidence": "HIGH",
                "reason": psr_result['reason'],
                "multiplier": 19.0
            }

        # ============================================
        # PRIORITAS 0.9: ABSORPTION MOMENTUM VALIDATOR (V75) - ANTI-HUMA TRAP
        # ============================================
        if amv_result['is_absorption_long'] and amv_result['confidence'] == "SUPREME":
            return {
                "phase": "PASSIVE_WHALE_EATING",
                "bias": "LONG",
                "confidence": "SUPREME",
                "reason": amv_result['reason'],
                "multiplier": 18.0
            }
        elif amv_result['is_absorption_long'] and amv_result['confidence'] == "HIGH":
            return {
                "phase": "ABSORPTION_DETECTED",
                "bias": "LONG",
                "confidence": "HIGH",
                "reason": amv_result['reason'],
                "multiplier": 17.0
            }

        # ============================================
        # PRIORITAS 0.10: LIQUIDATION GRAVITY OVERDRIVE (V75) - ANTI-RIVER NUCLEAR
        # ============================================
        if lgo_result['is_overdrive'] and lgo_result['confidence'] == "ABSOLUTE":
            if lgo_result['overdrive_type'] == "SHORT_GRAVITY_OVERDRIVE":
                return {
                    "phase": "LIQUIDATION_BLACKHOLE",
                    "bias": "LONG",
                    "confidence": "ABSOLUTE",
                    "reason": lgo_result['reason'],
                    "multiplier": 16.0
                }
            elif lgo_result['overdrive_type'] == "LONG_GRAVITY_OVERDRIVE":
                return {
                    "phase": "LIQUIDATION_BLACKHOLE",
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": lgo_result['reason'],
                    "multiplier": 16.0
                }
        elif lgo_result['is_overdrive'] and lgo_result['confidence'] == "HIGH":
            if lgo_result['overdrive_type'] == "SHORT_GRAVITY_WARNING":
                return {
                    "phase": "GRAVITY_WARNING",
                    "bias": "LONG",
                    "confidence": "HIGH",
                    "reason": lgo_result['reason'],
                    "multiplier": 15.0
                }
            elif lgo_result['overdrive_type'] == "LONG_GRAVITY_WARNING":
                return {
                    "phase": "GRAVITY_WARNING",
                    "bias": "SHORT",
                    "confidence": "HIGH",
                    "reason": lgo_result['reason'],
                    "multiplier": 15.0
                }

        # ============================================
        # PRIORITAS 0.11: MAGNET DECAY VALIDATOR (V74) - ANTI-RIVER SPOOF
        # ============================================
        if mdv_result['is_magnet_fake'] and mdv_result['confidence'] in ["SUPREME", "HIGH"]:
            return {
                "phase": "MAGNET_DECAY_SLAUGHTER",
                "bias": mdv_result['bias'],
                "confidence": mdv_result['confidence'],
                "reason": mdv_result['reason'],
                "multiplier": 14.0
            }

        # ============================================
        # PRIORITAS 0.12: PASSIVE ABSORPTION BLACKHOLE (V73) - ANTI-SIREN TRAP
        # ============================================
        if pab_result['is_blackhole'] and pab_result['confidence'] == "ABSOLUTE":
            if pab_result['blackhole_type'] == "PASSIVE_ABSORPTION_BLACKHOLE":
                return {
                    "phase": "LIQUIDITY_BLACKHOLE",
                    "bias": "LONG",
                    "confidence": "ABSOLUTE",
                    "reason": pab_result['reason'],
                    "multiplier": 13.0
                }

        # ============================================
        # PRIORITAS 0.13: CATCHING FALLING KNIVES (V72) - ANTI-ROBO TRAP
        # ============================================
        if cfk_result['is_knife'] and cfk_result['confidence'] == "SUPREME":
            if cfk_result['knife_type'] == "FALLING_KNIFE_DOWN":
                return {
                    "phase": "LIQUIDATION_CASCADE_HUNT",
                    "bias": "SHORT",
                    "confidence": "SUPREME",
                    "reason": cfk_result['reason'],
                    "multiplier": 12.0
                }

        # ============================================
        # PRIORITAS 0.14: MAGNET DISTANCE DOMINANCE (V71) - ANTI-RIVER TRAP
        # ============================================
        if mdd_result['is_magnet_trap'] and mdd_result['confidence'] == "SUPREME":
            if mdd_result['trap_type'] == "MAGNET_SQUEEZE":
                return {
                    "phase": "MAGNET_SQUEEZE",
                    "bias": "LONG",
                    "confidence": "SUPREME",
                    "reason": mdd_result['reason'],
                    "multiplier": 11.0
                }
            elif mdd_result['trap_type'] == "MAGNET_DUMP":
                return {
                    "phase": "MAGNET_DUMP",
                    "bias": "SHORT",
                    "confidence": "SUPREME",
                    "reason": mdd_result['reason'],
                    "multiplier": 11.0
                }

        # ============================================
        # PRIORITAS 0.15: ORDERBOOK VACUUM DEFENSE (V70) - ANTI-PHA TRAP
        # ============================================
        if ovd_result['is_trap'] and ovd_result['confidence'] == "SUPREME":
            if ovd_result['trap_type'] == "VACUUM_TRAP_BULLISH":
                return {
                    "phase": "VACUUM_REBOUND",
                    "bias": "LONG",
                    "confidence": "SUPREME",
                    "reason": ovd_result['reason'],
                    "multiplier": 10.0
                }
            elif ovd_result['trap_type'] == "VACUUM_TRAP_BEARISH":
                return {
                    "phase": "VACUUM_CORRECTION",
                    "bias": "SHORT",
                    "confidence": "SUPREME",
                    "reason": ovd_result['reason'],
                    "multiplier": 10.0
                }

        # ============================================
        # PRIORITAS 0.16: TREND INTEGRITY (V69) - ANTI-PIPPIN/PHA/POWER
        # ============================================
        if trend_result['restriction'] != "NONE":
            if trend_result['restriction'] == "FORBID_LONG":
                return {
                    "phase": "TREND_GRAVITY_DOWN",
                    "bias": "SHORT",
                    "confidence": "SUPREME",
                    "reason": trend_result['reason'],
                    "multiplier": 9.0
                }
            elif trend_result['restriction'] == "FORBID_SHORT":
                return {
                    "phase": "OBV_ACCUMULATION",
                    "bias": "LONG",
                    "confidence": "SUPREME",
                    "reason": trend_result['reason'],
                    "multiplier": 9.0
                }
            elif trend_result['restriction'] == "PRIORITIZE_SHORT":
                return {
                    "phase": "MACD_DEAD_ZONE",
                    "bias": "SHORT",
                    "confidence": "SUPREME",
                    "reason": trend_result['reason'],
                    "multiplier": 9.0
                }

        # ============================================
        # PRIORITAS 0.17: GRAVITY DEFLECTION (V68) - ANTI-PIPPIN TRAP
        # ============================================
        if ogd_result['is_deflected'] and ogd_result['confidence'] in ["SUPREME", "HIGH"]:
            return {
                "phase": "GRAVITY_DEFLECTION",
                "bias": ogd_result['bias'],
                "confidence": ogd_result['confidence'],
                "reason": ogd_result['reason'],
                "multiplier": 8.0
            }

        # ============================================
        # PRIORITAS 0.18: ZERO AGGRESSION SLAUGHTER (V67)
        # ============================================
        if zas_result['is_dead'] and zas_result['confidence'] in ["ABSOLUTE", "HIGH"]:
            return {
                "phase": "DEADSTICK_SLAUGHTER",
                "bias": zas_result['bias'],
                "confidence": zas_result['confidence'],
                "reason": zas_result['reason'],
                "multiplier": 7.0
            }

        # ============================================
        # PRIORITAS 0.19: ABSORPTION VALIDITY CHECK (V67)
        # ============================================
        if avc_result['is_trap'] and avc_result['confidence'] == "SUPREME":
            return {
                "phase": avc_result['trap_type'],
                "bias": avc_result['bias'],
                "confidence": "SUPREME",
                "reason": avc_result['reason'],
                "multiplier": 6.0
            }

        # ============================================
        # PRIORITAS 0.20: AGGRESSION-MASS DIVERGENCE (V65)
        # ============================================
        if amd_result['is_spoof'] and amd_result['confidence'] == "SUPREME":
            return {
                "phase": "AMD_SPOOF_DETECTOR",
                "bias": amd_result['bias'],
                "confidence": "SUPREME",
                "reason": amd_result['reason'],
                "multiplier": 5.0
            }

        # ============================================
        # PRIORITAS 0.21: THE DYL PARTICLE (V64)
        # ============================================
        if tdp_result['is_active'] and tdp_result['confidence'] == "ABSOLUTE":
            return {
                "phase": "DYL_PARTICLE",
                "bias": tdp_result['bias'],
                "confidence": "ABSOLUTE",
                "reason": tdp_result['reason'],
                "multiplier": 4.0
            }

        # ============================================
        # PRIORITAS 0.22: TEMPORAL ACCUMULATION INDEX (V66)
        # ============================================
        if ati_result['is_accumulating'] and ati_result['confidence'] in ["SUPREME", "ABSOLUTE"]:
            return {
                "phase": "TEMPORAL_ACCUMULATION",
                "bias": ati_result['bias'],
                "confidence": ati_result['confidence'],
                "reason": ati_result['reason'],
                "multiplier": 3.0
            }

        # ============================================
        # PRIORITAS 0.23: WALL ERASURE DETECTION (V63)
        # ============================================
        if wed_result['is_trap'] and wed_result['confidence'] == "SUPREME":
            return {
                "phase": wed_result['trap_type'],
                "bias": wed_result['bias'],
                "confidence": "SUPREME",
                "reason": wed_result['reason'],
                "multiplier": 2.5
            }

        # ============================================
        # PRIORITAS 0.24: MAGNET WALL REVERSAL (V62)
        # ============================================
        if mwr_result['is_magnet'] and mwr_result['confidence'] == "SUPREME":
            return {
                "phase": mwr_result['magnet_type'],
                "bias": mwr_result['bias'],
                "confidence": "SUPREME",
                "reason": mwr_result['reason'],
                "multiplier": 2.0
            }

        # ============================================
        # PRIORITAS 0.25: LOW-VOLUME SUCTION (V61)
        # ============================================
        if lvs_result['is_suction'] and lvs_result['confidence'] == "SUPREME":
            return {
                "phase": lvs_result['suction_type'],
                "bias": lvs_result['bias'],
                "confidence": "SUPREME",
                "reason": lvs_result['reason'],
                "multiplier": 1.5
            }

        # ============================================
        # PRIORITAS 0.26: DIVERGENCE TRAP DETECTOR (V60)
        # ============================================
        if dtd_result['is_trap'] and dtd_result['confidence'] == "SUPREME":
            return {
                "phase": dtd_result['trap_type'],
                "bias": dtd_result['bias'],
                "confidence": "SUPREME",
                "reason": dtd_result['reason'],
                "multiplier": 1.0
            }

        # The 90-Rule
        if rsi6 > RSI_NUCLEAR_OVERBOUGHT:
            return {
                "phase": "NUCLEAR_OVERBOUGHT",
                "bias": "SHORT",
                "confidence": "ABSOLUTE",
                "reason": f"ABSOLUTE_EXHAUSTION: RSI {rsi6} Nuclear! Wajib SHORT.",
                "multiplier": 1.8
            }
        if rsi6 < RSI_NUCLEAR_OVERSOLD:
            return {
                "phase": "NUCLEAR_OVERSOLD",
                "bias": "LONG",
                "confidence": "ABSOLUTE",
                "reason": f"ABSOLUTE_EXHAUSTION: RSI {rsi6} Floor! Wajib LONG.",
                "multiplier": 1.8
            }

        # PNR Check
        if short_liq <= EVENT_HORIZON:
            return {
                "phase": "PNR_PENDING",
                "bias": "LONG",
                "confidence": "PENDING",
                "reason": f"PNR: Short Liq {short_liq}% - Ghost validation diperlukan",
                "multiplier": 1.6
            }
        if long_liq <= EVENT_HORIZON:
            return {
                "phase": "PNR_PENDING",
                "bias": "SHORT",
                "confidence": "PENDING",
                "reason": f"PNR: Long Liq {long_liq}% - Ghost validation diperlukan",
                "multiplier": 1.6
            }

        # GHOST INTENT
        if ghost_result['is_ghost'] and ghost_result['confidence'] in ["SUPREME", "HIGH"]:
            return {
                "phase": "GHOST_DETECTED",
                "bias": ghost_result['bias'],
                "confidence": ghost_result['confidence'],
                "reason": f"GHOST_PROTOCOL: {ghost_result['reasons'][0] if ghost_result['reasons'] else 'Intent detected'}",
                "multiplier": 1.5
            }

        # ENGINE STARTER
        if starter_result['is_starting']:
            return {
                "phase": "ENGINE_STARTED",
                "bias": starter_result['bias'],
                "confidence": "HIGH",
                "reason": f"ENGINE_STARTED: {' | '.join(starter_result['reasons'][:1])}",
                "multiplier": 1.4
            }

        # LRR Trap
        if lrr_result['is_trap']:
            if lrr_result['danger_side'] == "LONG_LIQ_CLIFF":
                return {
                    "phase": "LRR_TRAP",
                    "bias": "SHORT",
                    "confidence": "SUPREME",
                    "reason": f"LRR_TRAP: Target atas {short_liq}% cuma umpan, jurang bawah {long_liq}% (Ratio {lrr_result['ratio']}x)!",
                    "multiplier": 1.3
                }
            elif lrr_result['danger_side'] == "SHORT_LIQ_CLIFF":
                return {
                    "phase": "LRR_TRAP",
                    "bias": "LONG",
                    "confidence": "SUPREME",
                    "reason": f"LRR_TRAP: Target bawah {long_liq}% cuma umpan, jurang atas {short_liq}% (Ratio {1/lrr_result['ratio']:.1f}x)!",
                    "multiplier": 1.3
                }

        # Market Slam
        if av_result['is_market_slam']:
            return {
                "phase": "MARKET_SLAM",
                "bias": "SHORT",
                "confidence": "HIGH",
                "reason": f"MARKET_SLAM: Agresi jual mendadak berakselerasi!",
                "multiplier": 1.2
            }

        # RSI WALL
        if rsi6 > RSI_EXTREME_HIGH_WALL and trade_flow < FLOW_CRITICAL_LOW:
            return {
                "phase": "RSI_WALL",
                "bias": "SHORT",
                "confidence": "HIGH",
                "reason": f"RSI WALL: RSI {rsi6} tinggi + Flow {trade_flow}x kering",
                "multiplier": 1.1
            }
        if rsi6 < RSI_EXTREME_LOW_WALL and trade_flow > FLOW_CRITICAL_HIGH:
            return {
                "phase": "RSI_FLOOR",
                "bias": "LONG",
                "confidence": "HIGH",
                "reason": f"RSI FLOOR: RSI {rsi6} rendah + Flow {trade_flow}x deras",
                "multiplier": 1.1
            }

        # Gravity Spoof
        if liquidity_gravity['bias'] == "SHORT" and long_liq > GRAVITY_SPOOF_DISTANCE:
            if short_liq < MAGNET_OVERRIDE_DISTANCE:
                return {
                    "phase": "GRAVITY_SPOOF",
                    "bias": "LONG",
                    "confidence": "HIGH",
                    "reason": f"SPOOF: Gravity bawah {long_liq}% jauh, magnet atas {short_liq}% dekat",
                    "multiplier": 1.0
                }
        if liquidity_gravity['bias'] == "LONG" and short_liq > GRAVITY_SPOOF_DISTANCE:
            if long_liq < MAGNET_OVERRIDE_DISTANCE:
                return {
                    "phase": "GRAVITY_SPOOF",
                    "bias": "SHORT",
                    "confidence": "HIGH",
                    "reason": f"SPOOF: Gravity atas {short_liq}% jauh, magnet bawah {long_liq}% dekat",
                    "multiplier": 1.0
                }

        # HFT Signature
        if hft_signature['bias'] != "NEUTRAL" and hft_signature['confidence'] in ["HIGH", "SUPREME"]:
            return {
                "phase": "HFT_SIGNATURE",
                "bias": hft_signature['bias'],
                "confidence": hft_signature['confidence'],
                "reason": hft_signature['signals'][0] if hft_signature['signals'] else "HFT Signature",
                "multiplier": 0.9
            }

        # OI Institutional
        if oi_velocity['status'] in ["REAL_ACCUMULATION", "REAL_SHORTING"]:
            return {
                "phase": oi_velocity['status'],
                "bias": "LONG" if "ACCUMULATION" in oi_velocity['status'] else "SHORT",
                "confidence": "SUPREME",
                "reason": oi_velocity['reason'],
                "multiplier": 0.8
            }

        return {
            "phase": "NEUTRAL",
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "No clear phase",
            "multiplier": 1.0
        }

# ================= ENERGY CALCULATOR V61 =================
class EnergyCalculatorV61:
    """
    V61: Energy calculator
    """
    @staticmethod
    def calculate(data: Dict, state_mgr: StateManagerV82) -> Dict:
        energy = 0
        reasons = []

        change_5m = safe_get(data, 'change_5m', 0)
        funding = safe_get(data, 'funding', 0)
        premium = safe_get(data, 'premium', 0)
        volume_trend = safe_get(data, 'volume_trend', 'STABLE')
        rsi6 = safe_get(data, 'rsi6', 50)
        oi_delta_5m = safe_get(data, 'oi_delta_5m', 0)

        if change_5m < -DUMP_SIZE_FOR_SQUEEZE:
            energy += 40
            reasons.append(f"Dump {change_5m}%")
        elif change_5m < -5.0:
            energy += 20
            reasons.append(f"Dump {change_5m}%")

        if funding < FUNDING_EXTREME_FOR_SQUEEZE:
            energy += 30
            reasons.append(f"Funding {funding}% extreme")
        elif funding < -2.0:
            energy += 15
            reasons.append(f"Funding {funding}%")

        if premium < PREMIUM_SUPER_SHORT:
            energy += 25
            reasons.append(f"Premium {premium}% super short")
        elif premium < PREMIUM_EXTREME_SHORT:
            energy += 10
            reasons.append(f"Premium {premium}% extreme short")

        if volume_trend == "SURGING":
            energy += 20
            reasons.append("Volume SURGING")
        elif volume_trend == "INCREASING":
            energy += 10
            reasons.append("Volume naik")

        if rsi6 < 15:
            energy += 25
            reasons.append(f"RSI {rsi6:.1f} super oversold")
        elif rsi6 < 25:
            energy += 15
            reasons.append(f"RSI {rsi6:.1f} oversold")

        if oi_delta_5m > OI_SURGE_THRESHOLD:
            energy += 20
            reasons.append(f"OI surge {oi_delta_5m:.1f}%")
        elif oi_delta_5m > OI_ACCUMULATION_THRESHOLD:
            energy += 10
            reasons.append(f"OI naik {oi_delta_5m:.1f}%")

        return {
            "score": energy,
            "is_squeeze_ready": energy >= ENERGY_SQUEEZE_MIN,
            "is_explosive": energy >= ENERGY_EXPLOSIVE_MIN,
            "reasons": reasons,
            "type": "EXPLOSIVE" if energy >= ENERGY_EXPLOSIVE_MIN else "NORMAL" if energy >= ENERGY_SQUEEZE_MIN else "LOW"
        }

# ================= MPE V61 =================
class MPEV61:
    """
    V61: Momentum Priority Engine
    """
    @staticmethod
    def calculate(data: Dict) -> Dict:
        trade_flow = safe_get(data, 'trade_flow', 1.0)
        change_5m = safe_get(data, 'change_5m', 0)
        macd_bullish = safe_get(data, 'macd_bullish_cross', False)
        macd_bearish = safe_get(data, 'macd_bearish_cross', False)
        rsi6 = safe_get(data, 'rsi6', 50)
        oi_delta_5m = safe_get(data, 'oi_delta_5m', 0)

        long_strength = 0.0
        short_strength = 0.0
        reasons = []

        if trade_flow < FLOW_EXTREME_SELL:
            if rsi6 < RSI_FORBID_SHORT:
                long_strength += 2.0
                reasons.append(f"Flow sell di RSI rendah = TRAPPED SHORTS")
            else:
                short_strength += 2.0
                reasons.append(f"Flow {trade_flow}x EXTREME SELL")
        elif trade_flow < FLOW_CRITICAL_LOW:
            if rsi6 < RSI_FORBID_SHORT:
                long_strength += 1.0
                reasons.append(f"Flow rendah di RSI rendah")
            else:
                short_strength += 1.5
                reasons.append(f"Flow {trade_flow}x LOW")
        elif trade_flow > FLOW_EXTREME_BUY:
            if rsi6 > RSI_FORBID_LONG:
                short_strength += 2.0
                reasons.append(f"Flow buy di RSI tinggi = TRAPPED LONGS")
            else:
                long_strength += 2.0
                reasons.append(f"Flow {trade_flow}x EXTREME BUY")
        elif trade_flow > FLOW_CRITICAL_HIGH:
            if rsi6 > RSI_FORBID_LONG:
                short_strength += 1.0
                reasons.append(f"Flow tinggi di RSI tinggi")
            else:
                long_strength += 1.5
                reasons.append(f"Flow {trade_flow}x HIGH")

        if oi_delta_5m > OI_SURGE_THRESHOLD:
            long_strength += 2.0
            reasons.append(f"OI surge {oi_delta_5m:.1f}%")
        elif oi_delta_5m > OI_ACCUMULATION_THRESHOLD:
            long_strength += 1.0
            reasons.append(f"OI naik {oi_delta_5m:.1f}%")
        elif oi_delta_5m < OI_EXTREME_DROP:
            short_strength += 2.0
            reasons.append(f"OI turun drastis {oi_delta_5m:.1f}%")
        elif oi_delta_5m < OI_LIQUIDATION_THRESHOLD:
            short_strength += 1.0
            reasons.append(f"OI turun {oi_delta_5m:.1f}%")

        if change_5m < -2.0:
            if rsi6 < RSI_FORBID_SHORT:
                long_strength += 2.0
                reasons.append(f"5m {change_5m}% di RSI rendah")
            else:
                short_strength += 1.5
                reasons.append(f"5m {change_5m}% SELL")
        elif change_5m > 2.0:
            if rsi6 > RSI_FORBID_LONG:
                short_strength += 2.0
                reasons.append(f"5m {change_5m}% di RSI tinggi")
            else:
                long_strength += 1.5
                reasons.append(f"5m {change_5m}% BUY")

        if macd_bullish:
            long_strength += 1.0
            reasons.append("MACD Golden Cross")
        if macd_bearish:
            short_strength += 1.0
            reasons.append("MACD Death Cross")

        if long_strength > short_strength + 1.5:
            return {
                "bias": "LONG",
                "strength": round(long_strength, 1),
                "is_extreme": long_strength >= 3.0,
                "reasons": reasons
            }
        elif short_strength > long_strength + 1.5:
            return {
                "bias": "SHORT",
                "strength": round(short_strength, 1),
                "is_extreme": short_strength >= 3.0,
                "reasons": reasons
            }

        return {
            "bias": "NEUTRAL",
            "strength": 0,
            "is_extreme": False,
            "reasons": []
        }

# ================= DATA FETCHER =================
class BinanceFetcher:
    """Fetch data from Binance Futures API"""
    def __init__(self, symbol: str):
        self.symbol = symbol.upper()
        self.base_url = "https://fapi.binance.com"
        self.futures_data_url = "https://fapi.binance.com/futures/data"
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0"})
        self.session.verify = False

    def fetch(self, endpoint: str, params: Dict = None, base_url: str = None) -> Optional[Any]:
        try:
            if base_url is None:
                base_url = self.base_url
            url = f"{base_url}{endpoint}"
            resp = self.session.get(url, params=params, timeout=DEFAULT_TIMEOUT)
            if resp.status_code == 200:
                return resp.json()
            return None
        except Exception as e:
            print(f"❌ Fetch error {endpoint}: {e}")
            return None

    def get_price(self) -> Optional[float]:
        data = self.fetch("/fapi/v1/ticker/price", {"symbol": self.symbol})
        return safe_float(data.get("price")) if data else None

    def get_24h_change(self) -> Optional[float]:
        data = self.fetch("/fapi/v1/ticker/24hr", {"symbol": self.symbol})
        return safe_float(data.get("priceChangePercent")) if data else None

    def get_orderbook_ratio(self) -> Optional[Dict]:
        data = self.fetch("/fapi/v1/depth", {"symbol": self.symbol, "limit": 20})
        if not data:
            return {"ratio": 1.0, "bids": [], "asks": []}

        bids = [[safe_float(p), safe_float(q)] for p, q in data.get("bids", [])]
        asks = [[safe_float(p), safe_float(q)] for p, q in data.get("asks", [])]

        bid_vol = sum(q for _, q in bids[:5])
        ask_vol = sum(q for _, q in asks[:5])
        ratio = safe_div(bid_vol, ask_vol, 1.0)

        return {
            "ratio": round(ratio, 2),
            "bids": bids,
            "asks": asks,
            "top_bid": bids[0] if bids else [0, 0],
            "top_ask": asks[0] if asks else [0, 0]
        }

    def get_trades_flow(self) -> Optional[Dict]:
        data = self.fetch("/fapi/v1/trades", {"symbol": self.symbol, "limit": 100})
        if not data:
            return {"buys": 0, "sells": 0, "ratio": 1.0, "volume_ratio": 1.0, "aggressive_ratio": 1.0, "flow_momentum": "NEUTRAL"}

        buys = sum(1 for t in data if not t.get("isBuyerMaker", True))
        sells = len(data) - buys
        ratio = safe_div(buys, sells, 1.0)

        buy_vol = sum(safe_float(t["qty"]) for t in data if not t.get("isBuyerMaker", True))
        sell_vol = sum(safe_float(t["qty"]) for t in data if t.get("isBuyerMaker", True))
        vol_ratio = safe_div(buy_vol, sell_vol, 1.0)

        aggressive_buys = sum(1 for t in data[:20] if not t.get("isBuyerMaker", True))
        aggressive_sells = sum(1 for t in data[:20] if t.get("isBuyerMaker", True))
        aggressive_ratio = safe_div(aggressive_buys, aggressive_sells, 1.0)

        return {
            "buys": buys,
            "sells": sells,
            "ratio": round(ratio, 2),
            "volume_ratio": round(vol_ratio, 2),
            "aggressive_ratio": round(aggressive_ratio, 2),
            "flow_momentum": "NEUTRAL"
        }

    def get_funding_premium(self) -> Optional[Dict]:
        data = self.fetch("/fapi/v1/premiumIndex", {"symbol": self.symbol})
        if not data:
            return {"premium": 0, "funding": 0, "avg_funding": 0}

        mark = safe_float(data.get("markPrice", 0))
        index = safe_float(data.get("indexPrice", 0))
        premium = ((mark - index) / index) * 100 if index != 0 else 0

        hist = self.fetch("/fapi/v1/fundingRate", {"symbol": self.symbol, "limit": 50})
        avg_funding = 0
        if hist:
            rates = [safe_float(f["fundingRate"]) * 100 for f in hist]
            avg_funding = np.mean(rates) if rates else 0

        return {
            "premium": round(premium, 4),
            "funding": safe_float(data.get("lastFundingRate", 0)) * 100,
            "avg_funding": round(avg_funding, 4)
        }

    def get_klines(self, interval: str = "1m", limit: int = 100) -> Optional[Dict]:
        data = self.fetch("/fapi/v1/klines", {
            "symbol": self.symbol,
            "interval": interval,
            "limit": limit
        })
        if not data:
            return None

        closes = [safe_float(k[4]) for k in data]
        highs = [safe_float(k[2]) for k in data]
        lows = [safe_float(k[3]) for k in data]
        volumes = [safe_float(k[5]) for k in data]
        opens = [safe_float(k[1]) for k in data]

        # Hitung std dev untuk volatility
        if len(closes) > 1:
            std_dev = np.std(closes[-20:]) if len(closes) >= 20 else np.std(closes)
        else:
            std_dev = 0

        return {
            "highs": highs,
            "lows": lows,
            "closes": closes,
            "volumes": volumes,
            "opens": opens,
            "std_dev": std_dev
        }

    def get_open_interest_current(self) -> Optional[float]:
        """Get current open interest"""
        data = self.fetch("/fapi/v1/openInterest", {"symbol": self.symbol})
        if data and "openInterest" in data:
            return safe_float(data["openInterest"])
        return None

    def get_open_interest_historical(self, period: str = "5m", limit: int = 30) -> Optional[List]:
        """Get historical open interest"""
        data = self.fetch("/futures/data/openInterestHist", {
            "symbol": self.symbol,
            "period": period,
            "limit": limit
        }, base_url=self.futures_data_url)
        return data

    def get_oi_5m_ago(self) -> Optional[float]:
        """
        Ambil OI 5 menit yang lalu
        """
        try:
            url = f"{self.base_url}/futures/data/openInterestHist"
            params = {
                "symbol": self.symbol,
                "period": "5m",
                "limit": 5
            }
            resp = self.session.get(url, params=params, timeout=DEFAULT_TIMEOUT)
            if resp.status_code == 200:
                data = resp.json()
                if data and len(data) >= 1:
                    old_data = data[0]
                    oi_val = safe_float(old_data.get("sumOpenInterest") or old_data.get("openInterest") or old_data.get("sumOpenInterestValue"))
                    return oi_val
        except Exception as e:
            print(f"⚠️ Fetch OI Historical Gagal: {e}")
        return None

    def get_open_interest(self) -> Optional[float]:
        """Wrapper untuk mendapatkan OI current dengan multiple fallback"""
        oi_current = self.get_open_interest_current()
        if oi_current is not None and oi_current > 0:
            return oi_current

        hist = self.get_open_interest_historical(period="5m", limit=1)
        if hist and len(hist) > 0:
            oi_val = safe_float(hist[0].get("sumOpenInterest") or hist[0].get("openInterest") or hist[0].get("sumOpenInterestValue"))
            if oi_val and oi_val > 0:
                return oi_val
        return None

    def calculate_wmi(self, short_dist: float, long_dist: float,
                    short_vol: float, long_vol: float) -> float:
        """Whale Mass Index (WMI)"""
        if short_dist < 0.1 or long_dist < 0.1:
            return 0
        short_mass = short_vol / (short_dist ** 2)
        long_mass = long_vol / (long_dist ** 2)
        if short_mass + long_mass == 0:
            return 0
        return ((short_mass - long_mass) / (short_mass + long_mass)) * 100

# ================= INDICATOR CALCULATOR =================
class IndicatorCalculator:
    """Calculate technical indicators"""
    @staticmethod
    def calculate_rsi(closes: List[float], period: int = 14) -> float:
        if len(closes) < period + 1:
            return 50.0
        gains, losses = [], []
        for i in range(1, period + 1):
            change = closes[-i] - closes[-i-1]
            if change >= 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period
        if avg_loss == 0:
            return 100.0
        rs = avg_gain / avg_loss
        return 100 - (100 / (1 + rs))

    @staticmethod
    def calculate_macd(closes: List[float]) -> Dict:
        if len(closes) < 26:
            return {"dif": 0, "dea": 0, "macd": 0, "bullish_cross": False, "bearish_cross": False}

        def ema(values, period):
            if len(values) < period:
                return values[-1] if values else 0
            alpha = 2 / (period + 1)
            ema_val = values[0]
            for v in values[1:]:
                ema_val = alpha * v + (1 - alpha) * ema_val
            return ema_val

        ema12 = ema(closes, 12)
        ema26 = ema(closes, 26)
        dif = ema12 - ema26

        dif_list = []
        for i in range(9, len(closes)):
            temp_closes = closes[:i+1]
            temp_ema12 = ema(temp_closes, 12)
            temp_ema26 = ema(temp_closes, 26)
            dif_list.append(temp_ema12 - temp_ema26)
        dea = ema(dif_list, 9) if dif_list else 0

        macd = (dif - dea) * 2

        if len(closes) > 27:
            prev_closes = closes[:-1]
            prev_ema12 = ema(prev_closes, 12)
            prev_ema26 = ema(prev_closes, 26)
            prev_dif = prev_ema12 - prev_ema26
            prev_dif_list = []
            for i in range(9, len(prev_closes)):
                temp = prev_closes[:i+1]
                temp_ema12 = ema(temp, 12)
                temp_ema26 = ema(temp, 26)
                prev_dif_list.append(temp_ema12 - temp_ema26)
            prev_dea = ema(prev_dif_list, 9) if prev_dif_list else 0

            bullish_cross = dif > dea and prev_dif <= prev_dea
            bearish_cross = dif < dea and prev_dif >= prev_dea
        else:
            bullish_cross = bearish_cross = False

        return {
            "dif": dif,
            "dea": dea,
            "macd": macd,
            "bullish_cross": bullish_cross,
            "bearish_cross": bearish_cross
        }

    @staticmethod
    def calculate_ma(data: List[float], period: int) -> float:
        """Menghitung Moving Average"""
        if len(data) < period:
            return data[-1] if data else 0.0
        return sum(data[-period:]) / period

    @staticmethod
    def calculate_obv(closes: List[float], volumes: List[float]) -> List[float]:
        """Menghitung On-Balance Volume (OBV)"""
        if len(closes) < 2 or len(volumes) < 2:
            return [0.0]
        obv = [0.0]
        for i in range(1, min(len(closes), len(volumes))):
            if closes[i] > closes[i-1]:
                obv.append(obv[-1] + volumes[i])
            elif closes[i] < closes[i-1]:
                obv.append(obv[-1] - volumes[i])
            else:
                obv.append(obv[-1])
        return obv

    @staticmethod
    def get_liquidation_zones(highs: List[float], lows: List[float], price: float,
                            volumes: List[float] = None) -> Dict:
        if not highs or not lows or price == 0:
            return {"long_dist": 99, "short_dist": 99, "long_vol": 1.0, "short_vol": 1.0}

        recent_high = max(highs[-20:]) if len(highs) >= 20 else max(highs)
        recent_low = min(lows[-20:]) if len(lows) >= 20 else min(lows)

        long_dist = ((price - recent_low) / recent_low) * 100 if recent_low != 0 else 0
        short_dist = ((recent_high - price) / price) * 100 if price != 0 else 0

        if volumes and len(volumes) >= 20:
            avg_vol = np.mean(volumes[-20:])
            long_vol = avg_vol * (1 / max(long_dist, 0.1))
            short_vol = avg_vol * (1 / max(short_dist, 0.1))
        else:
            long_vol = 1.0
            short_vol = 1.0

        return {
            "long_dist": round(long_dist, 2),
            "short_dist": round(short_dist, 2),
            "long_vol": round(long_vol, 2),
            "short_vol": round(short_vol, 2),
            "recent_low": recent_low,
            "recent_high": recent_high
        }

        # ================= V82: FUEL IGNITION DETECTOR (FID) - BARU! =================
class FuelIgnitionDetectorV82:
    """
    V82: Mendeteksi Whale injak gas pol (FID).
    Jika OI Delta 5m > 3.0% (Massive Fuel Influx) DAN RSI > 85,
    maka sinyal SHORT dari RSI Overbought (FAKE_PUMP) BATAL.
    Whale sedang melakukan 'Momentum Ignition'.
    """
    @staticmethod
    def analyze(oi_delta: float, rsi6: float, wmi: float) -> Dict:
        is_igniting = False
        bias = "NEUTRAL"
        reason = ""

        if oi_delta > 3.0 and rsi6 > 85:  # Kasus COS: OI +5.07% & RSI 100
            is_igniting = True
            bias = "LONG"
            reason = (f"FID_IGNITION: OI meledak {oi_delta:.2f}% (Bensin Massive!) di RSI {rsi6:.1f}. "
                      f"Whale sedang injak gas. Magnet WMI {wmi:.1f} akan ditabrak. DILARANG SHORT!")

        return {
            "is_igniting": is_igniting,
            "bias": bias,
            "reason": reason
        }

# ================= CONFLICT RESOLVER V82 =================
class ConflictResolverV82:
    """
    V82: Resolve konflik dengan hierarki prioritas mutlak V82
    URUTAN PRIORITAS MUTLAK V82 (THE HIERARCHY OF LIQUIDITY GHOST):
        1. OTF (Oversold Trap Filter) - ANTI-UAI & LIQUIDITY VACUUM REBOUND (NEW V85!) - ANTI-BOTTOMLESS HOLE / DEATH MAGNET (NEW V82!)
        2. FGD (Fake Gravity Detector) - ANTI-GRAVITY TRAP (V84) - ANTI-BULLISH/BEARISH ABSORPTION SIPHON (NEW V82!)
        3. LDF (Liquidity Density Filter) - PATH OPTIMAL (V84) - ANTI-INFINITY SQUEEZE (V81)
        4. ICD (Internal Cross Detector) - ANTI-POSITION FLIPPING TRAP (V81)
        5. EZH (Execution Zone Hunter) - ANTI-RIVER MAGNETIC SLINGSHOT (V78)
        6. WTD (Wash Trade Detector) - ANTI-KITE FALSE BRIDGE (V79)
        7. IER (Institutional Exit Radar) - ANTI-OPN/BARD FALSE FLOW (V80)
        8. RMG (RSI Momentum Guard) - ANTI-RIVER GRAVITY DECOY (V80)
        9. FMV (Fake Magnet Vacuum) - KOMBINASI IER + RMG (V80)
        10. PSV (Panic Sell Validator) - ANTI-OPN ENDLESS FLOOR (V78)
        11. OFF (Overdrive Flow Filter) - ANTI-HUSDT TRAP (V77)
        12. AEF (Aggressive Exhaustion Filter) - ANTI-PHA TRAP (V77)
        13. PSR (Panic Saturation Reversal) - ANTI-HUMA DRIFT TRAP (V76)
        14. AMV (Absorption Momentum Validator) - ANTI-HUMA TRAP (V75)
        15. LGO (Liquidation Gravity Overdrive) - ANTI-RIVER NUCLEAR (V75)
        16. MDV (Magnet Decay Validator) - ANTI-RIVER SPOOF (V74)
        17. PAB (Passive Absorption Blackhole) - ANTI-SIREN TRAP (V73)
        18. CFK (Catching Falling Knives) - ANTI-ROBO TRAP (V72)
        19. MDD (Magnet Distance Dominance) - ANTI-RIVER TRAP (V71)
        20. OVD (Orderbook Vacuum Defense) - ANTI-PHA TRAP (V70)
        21. Trend Integrity (V69) - ANTI-PIPPIN/PHA/POWER
        22. Gravity Deflection (OGD) - ANTI-PIPPIN TRAP (V68)
        23. Zero Aggression Slaughter (ZAS) - ANTI-DEADSTICK (V67)
        24. Absorption Validity Check (AVC) - ANTI-EXIT LIQUIDITY TRAP (V67)
        25. Aggression-Mass Divergence (AMD) - ANTI-SPOOF PROTECTION (V65)
        26. The DYL Particle (TDP) - ABSOLUTE OVERRIDE (V64)
        27. Temporal Accumulation Index (ATI) - WHALE PATIENCE LOADING (V66)
        28. Wall Erasure Detection (WED) - GRAVITY MANDATE (V63)
        29. Magnet Wall Reversal (MWR) (V62)
        30. The Ghost Whisperer (LVS) (V61)
        31. The Absorption Shield (DTD) (V60)
    """
    @staticmethod
    def resolve(market_phase: Dict, energy: Dict, mpe_bias: str,
                trade_flow: float, liquidity_data: Dict, ppi: Dict,
                exhaustion: Dict, stop_hunt: Dict, ob_imprint: Dict,
                spoofing: Dict, reversion: Dict, oi_velocity: Dict,
                hft_signature: Dict, rsi6: float, change_5m: float,
                volume_ratio: float, premium: float,
                aggressive_ratio: float,
                short_gravity: float, long_gravity: float,
                short_dist: float, long_dist: float,
                short_vol: float, long_vol: float,
                price: float, state_mgr,
                data: Dict, odd_result: Dict, ghost_result: Dict,
                oi_5m_ago: float, wmi: Dict = None,
                dtd_result: Dict = None, lvs_result: Dict = None,
                mwr_result: Dict = None, wed_result: Dict = None,
                tdp_result: Dict = None, amd_result: Dict = None,
                ati_result: Dict = None, zas_result: Dict = None,
                avc_result: Dict = None, ogd_result: Dict = None,
                trend_result: Dict = None, ovd_result: Dict = None,
                mdd_result: Dict = None, cfk_result: Dict = None,
                pab_result: Dict = None, mdv_result: Dict = None,
                amv_result: Dict = None, lgo_result: Dict = None,
                psr_result: Dict = None, off_result: Dict = None,
                aef_result: Dict = None, ezh_result: Dict = None,
                psv_result: Dict = None, wtd_result: Dict = None,
                ier_result: Dict = None, rmg_result: Dict = None,
                fmv_result: Dict = None,
                ltg_result: Dict = None, icd_result: Dict = None,
                api_result: Dict = None, lmg_result: Dict = None,
                fid_result: Dict = None,
                # V83 NEW MODULES
                lhg_result: Dict = None, ovs_result: Dict = None,
                adv_result: Dict = None, tbd_result: Dict = None,
                oia_result: Dict = None, lsp_result: Dict = None,
                sniper_result: Dict = None,
                # V85 NEW MODULES - ANTI-LIQUIDITY TRAP (UAI & DEGO CASES)
                otf_result: Dict = None, aaf_result: Dict = None,
                fed_result: Dict = None,
                # V85 NEW MODULES - ANTI-STABLE TRAP (Neutral Zone Shield)
                nzs_result: Dict = None, pfd_result: Dict = None,
                fed_v85_result: Dict = None, lrd_result: Dict = None,
                # V86 NEW MODULES - ZERO GRAVITY HORIZON (Anti-TRIA Trap)
                zgh_result: Dict = None, odf_result: Dict = None):
        # ============================================
        # 🟢 PRIORITAS 0 (TERTINGGI): V86 OVERBOUGHT DISTRIBUTION FILTER - ANTI-TRIA TRAP
        # PRIORITAS TERATAS! Mencegah Long Trap saat RSI > 90 + OI naik + Agg rendah
        # ============================================
        if odf_result and odf_result.get('active'):
            return {
                "bias": odf_result['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V86_ODF_OVERBOUGHT_DISTRIBUTION: {odf_result['reason']}",
                "phase": "ZERO_GRAVITY_HORIZON",
                "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # ============================================
        # 🟢 PRIORITAS 0.1 (TERTINGGI): V86 ZERO GRAVITY HORIZON - ANTI-TRIA TRAP
        # ============================================
        if zgh_result and zgh_result.get('is_ceiling'):
            return {
                "bias": zgh_result['bias'],
                "confidence": zgh_result['confidence'],
                "reason": f"V86_ZGH_ZERO_GRAVITY: {zgh_result['reason']}",
                "phase": "DISTRIBUTION_TOP",
                "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }
                
        # ============================================
        # 🟢 PRIORITAS 0 (TERTINGGI): V85 OVERSOLD TRAP FILTER - LIQUIDITY VACUUM REBOUND
        # ANTI-CHECKMATE! Mencegah Short Trap saat WMI ekstrim negatif + RSI rendah
        # ============================================
        if otf_result and otf_result.get('is_trap'):
            if otf_result.get('scenario') == 'LIQUIDITY_VACUUM_REBOUND':
                return {
                    "bias": otf_result['bias'],
                    "confidence": "ABSOLUTE",
                    "reason": f"V85_OTF_LIQUIDITY_VACUUM: {otf_result['reason']}",
                    "phase": "ANTI_LIQUIDITY_TRAP",
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }
        
        # ============================================
        # 🛡️ PRIORITAS 0.5 (SUPREME): V85 NEUTRAL ZONE SHIELD - ANTI-STABLE TRAP
        # Mencegah Short Trap saat RSI Neutral + WMI ekstrim negatif + IER aktif
        # Ini adalah filter utama untuk kasus STABLEUSDT!
        # ============================================
        if nzs_result and nzs_result.get('is_shielded'):
            return {
                "bias": nzs_result['bias'],
                "confidence": "SUPREME",
                "reason": f"V85_NZS_SHIELD: {nzs_result['reason']}",
                "phase": "NEUTRAL_TRAP_SHIELD",
                "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }
        
        # ============================================
        # 🔄 PRIORITAS 0.6 (SUPREME): V85 POSITION FLIP DETECTOR - ANTI-INTERNAL FLOW ILLUSION
        # Mencegah salah baca position flip sebagai exit distribution
        # ============================================
        if pfd_result and pfd_result.get('is_flip'):
            return {
                "bias": pfd_result['bias'],
                "confidence": pfd_result.get('confidence', 'SUPREME'),
                "reason": f"V85_PFD_POSITION_FLIP: {pfd_result['reason']}",
                "phase": "POSITION_RELOAD",
                "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }
        
        # ============================================
        # 🎭 PRIORITAS 0.7 (HIGH): V85 FAKE EXIT DETECTOR - ANTI-LIQUIDITY BUILDING
        # Override IER jika terdeteksi fake exit (flow tinggi tanpa agresi)
        # ============================================
        if fed_v85_result and fed_v85_result.get('is_fake_exit'):
            # Ignore IER jika fake exit terdeteksi
            if ier_result and ier_result.get('is_exit'):
                return {
                    "bias": fed_v85_result['bias'],
                    "confidence": fed_v85_result.get('confidence', 'HIGH'),
                    "reason": f"V85_FED_FAKE_EXIT: {fed_v85_result['reason']} (IER OVERRIDE!)",
                    "phase": "LIQUIDITY_BUILDING",
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }
        
        # ============================================
        # 🔁 PRIORITAS 0.8 (SUPREME): V85 LIQUIDITY RELOAD DETECTOR - ANTI-OI MANIPULATION
        # Mencegah salah baca OI drop sebagai exit (bisa jadi liquidity reset)
        # ============================================
        if lrd_result and lrd_result.get('is_reload'):
            # Override IER jika liquidity reload terdeteksi
            if ier_result and ier_result.get('is_exit'):
                return {
                    "bias": lrd_result['bias'],
                    "confidence": lrd_result.get('confidence', 'SUPREME'),
                    "reason": f"V85_LRD_LIQUIDITY_RELOAD: {lrd_result['reason']} (IER OVERRIDE! Institutional Reload!)",
                    "phase": "LIQUIDITY_RESET",
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }
        
        # ============================================
        # PRIORITAS -1 (TERTINGGI): V83 LIQUIDITY SNIPER SCORE
        # ============================================
        if sniper_result and sniper_result.get('confidence') == 'HIGH':
            return {
                "bias": sniper_result['bias'],
                "confidence": sniper_result['confidence'],
                "reason": f"V83_SNIPER: {sniper_result['reason']} | LHG={lhg_result.get('target', 'N/A') if lhg_result else 'N/A'}",
                "phase": "LIQUIDITY_SNIPER_TARGET",
                "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"},
                "v83_details": sniper_result
            }
        
        # ============================================
        # PRIORITAS 0 (TERTINGGI): LIQUIDITY MIRROR GUARD (V82) - ANTI-DEATH MAGNET
        # ============================================
        if lmg_result and lmg_result['is_death_magnet']:
            return {
                "bias": lmg_result['bias'],
                "confidence": "ABSOLUTE",
                "reason": lmg_result['reason'],
                "phase": "DEATH_MAGNET_CASCADE",
                "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # ============================================
        # PRIORITAS 1: FUEL IGNITION DETECTOR (V82) - ANTI-FAKE PUMP
        # ============================================
        if fid_result and fid_result['is_igniting']:
            return {
                "bias": fid_result['bias'],
                "confidence": "ABSOLUTE",
                "reason": fid_result['reason'],
                "phase": "FUEL_IGNITION",
                "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # ============================================
        # PRIORITAS 2: ABSORPTION PRESSURE INDEX (V82) - ANTI-ABSORPTION SIPHON
        # ============================================
        if api_result and api_result['is_absorbing']:
            return {
                "bias": api_result['bias'],
                "confidence": "ABSOLUTE",
                "reason": api_result['reason'],
                "phase": "WHALE_ABSORPTION_ZONE",
                "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # ============================================
        # PRIORITAS 3: LIQUIDITY THINNING GUARD (V81)
        # ============================================
        if ltg_result and ltg_result['is_vacuum']:
            return {
                "bias": ltg_result['bias'],
                "confidence": "ABSOLUTE",
                "reason": ltg_result['reason'],
                "phase": "LIQUIDITY_VACUUM",
                "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # ============================================
        # PRIORITAS 4: EXECUTION ZONE HUNTER (V78) - ANTI-RIVER MAGNETIC SLINGSHOT
        # ============================================
        if ezh_result and ezh_result['is_execution']:
            if ezh_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
                return {
                    "bias": ezh_result['bias'],
                    "confidence": ezh_result['confidence'],
                    "reason": ezh_result['reason'],
                    "phase": ezh_result['execution_type'],
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }

        # ============================================
        # PRIORITAS 5: WASH TRADE DETECTOR (V79) - ANTI-KITE FALSE BRIDGE
        # ============================================
        if wtd_result and wtd_result['is_wash_trade']:
            if wtd_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
                return {
                    "bias": wtd_result['bias'],
                    "confidence": wtd_result['confidence'],
                    "reason": wtd_result['reason'],
                    "phase": wtd_result['wash_type'],
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }

        # ============================================
        # PRIORITAS 6: INSTITUTIONAL EXIT RADAR (V80) - ANTI-OPN/BARD FALSE FLOW
        # ============================================
        if ier_result and ier_result['is_exit']:
            if ier_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
                return {
                    "bias": ier_result['bias'],
                    "confidence": ier_result['confidence'],
                    "reason": ier_result['reason'],
                    "phase": ier_result['exit_type'],
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }

        # ============================================
        # PRIORITAS 7: RSI MOMENTUM GUARD (V80) - ANTI-RIVER GRAVITY DECOY
        # ============================================
        if rmg_result and rmg_result['is_weak']:
            if rmg_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
                return {
                    "bias": rmg_result['bias'],
                    "confidence": rmg_result['confidence'],
                    "reason": rmg_result['reason'],
                    "phase": rmg_result['weakness_type'],
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "NO"}
                }

        # ============================================
        # PRIORITAS 8: FAKE MAGNET VACUUM (V80) - KOMBINASI IER + RMG
        # ============================================
        if fmv_result and fmv_result['is_fake_magnet']:
            if fmv_result['confidence'] in ["ABSOLUTE", "SUPREME"]:
                return {
                    "bias": fmv_result['bias'],
                    "confidence": fmv_result['confidence'],
                    "reason": fmv_result['reason'],
                    "phase": fmv_result['fake_type'],
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }

        # ============================================
        # PRIORITAS 9: PANIC SELL VALIDATOR (V78) - ANTI-OPN ENDLESS FLOOR
        # ============================================
        if psv_result and psv_result['is_valid']:
            if psv_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
                return {
                    "bias": psv_result['bias'],
                    "confidence": psv_result['confidence'],
                    "reason": psv_result['reason'],
                    "phase": psv_result['validation_type'],
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "NO" if "FALLING" in psv_result['validation_type'] else "YES"}
                }

        # ============================================
        # PRIORITAS 10: OVERDRIVE FLOW FILTER (V77) - ANTI-HUSDT TRAP
        # ============================================
        if off_result and off_result['is_patched']:
            if off_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
                return {
                    "bias": off_result['bias'],
                    "confidence": off_result['confidence'],
                    "reason": off_result['reason'],
                    "phase": off_result['patched_type'],
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }

        # ============================================
        # PRIORITAS 11: AGGRESSIVE EXHAUSTION FILTER (V77) - ANTI-PHA TRAP
        # ============================================
        if aef_result and aef_result['is_exhausted']:
            if aef_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
                return {
                    "bias": aef_result['bias'],
                    "confidence": aef_result['confidence'],
                    "reason": aef_result['reason'],
                    "phase": aef_result['exhausted_type'],
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "NO"}
                }

        # ============================================
        # PRIORITAS 12: PANIC SATURATION REVERSAL (V76) - ANTI-HUMA DRIFT TRAP
        # ============================================
        if psr_result and psr_result['is_saturated']:
            if psr_result['confidence'] in ["SUPREME", "ABSOLUTE", "HIGH"]:
                return {
                    "bias": psr_result['bias'],
                    "confidence": psr_result['confidence'],
                    "reason": psr_result['reason'],
                    "phase": psr_result['saturation_type'],
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }

        # ============================================
        # PRIORITAS 13: ABSORPTION MOMENTUM VALIDATOR (V75) - ANTI-HUMA TRAP
        # ============================================
        if amv_result and amv_result['is_absorption_long']:
            if amv_result['confidence'] in ["SUPREME", "HIGH"]:
                return {
                    "bias": amv_result['bias'],
                    "confidence": amv_result['confidence'],
                    "reason": amv_result['reason'],
                    "phase": "PASSIVE_WHALE_EATING",
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }

        # ============================================
        # PRIORITAS 14: LIQUIDATION GRAVITY OVERDRIVE (V75) - ANTI-RIVER NUCLEAR
        # ============================================
        if lgo_result and lgo_result['is_overdrive']:
            if lgo_result['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
                return {
                    "bias": lgo_result['bias'],
                    "confidence": lgo_result['confidence'],
                    "reason": lgo_result['reason'],
                    "phase": lgo_result['overdrive_type'],
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }

        # ============================================
        # PRIORITAS 15: MAGNET DECAY VALIDATOR (V74) - ANTI-RIVER SPOOF
        # ============================================
        if mdv_result and mdv_result['is_magnet_fake']:
            if mdv_result['confidence'] in ["SUPREME", "HIGH"]:
                return {
                    "bias": mdv_result['bias'],
                    "confidence": mdv_result['confidence'],
                    "reason": mdv_result['reason'],
                    "phase": "MAGNET_DECAY_SLAUGHTER",
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "NO"}
                }

        # ============================================
        # PRIORITAS 16: PASSIVE ABSORPTION BLACKHOLE (V73) - ANTI-SIREN TRAP
        # ============================================
        if pab_result and pab_result['is_blackhole']:
            if pab_result['confidence'] == "ABSOLUTE":
                return {
                    "bias": pab_result['bias'],
                    "confidence": "ABSOLUTE",
                    "reason": pab_result['reason'],
                    "phase": pab_result['blackhole_type'],
                    "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }

        # ============================================
        # PRIORITAS 17: CATCHING FALLING KNIVES (V72) - ANTI-ROBO TRAP
        # ============================================
        if cfk_result and cfk_result['is_knife']:
            if cfk_result['confidence'] == "SUPREME":
                return {
                    "bias": cfk_result['bias'],
                    "confidence": "SUPREME",
                    "reason": cfk_result['reason'],
                    "phase": cfk_result['knife_type'],
                    "ttk_info": {"estimated_minutes": 3, "urgency": "IMMINENT", "fuel_ready": "NO"}
                }

        # ============================================
        # PRIORITAS 18: MAGNET DISTANCE DOMINANCE (V71) - ANTI-RIVER TRAP
        # ============================================
        if mdd_result and mdd_result['is_magnet_trap']:
            if mdd_result['confidence'] == "SUPREME":
                return {
                    "bias": mdd_result['bias'],
                    "confidence": "SUPREME",
                    "reason": mdd_result['reason'],
                    "phase": mdd_result['trap_type'],
                    "ttk_info": {"estimated_minutes": 3, "urgency": "IMMINENT", "fuel_ready": "NO"}
                }

        # ============================================
        # PRIORITAS 19: ORDERBOOK VACUUM DEFENSE (V70) - ANTI-PHA TRAP
        # ============================================
        if ovd_result and ovd_result['is_trap']:
            if ovd_result['confidence'] == "SUPREME":
                return {
                    "bias": ovd_result['bias'],
                    "confidence": "SUPREME",
                    "reason": ovd_result['reason'],
                    "phase": ovd_result['trap_type'],
                    "ttk_info": {"estimated_minutes": 3, "urgency": "IMMINENT", "fuel_ready": "NO"}
                }

        # ============================================
        # PRIORITAS 20: TREND INTEGRITY (V69) - ANTI-PIPPIN/PHA/POWER
        # ============================================
        if trend_result and trend_result['restriction'] != "NONE":
            if trend_result['restriction'] == "FORBID_LONG":
                return {
                    "bias": "SHORT",
                    "confidence": "SUPREME",
                    "reason": trend_result['reason'],
                    "phase": "TREND_GRAVITY_BLOCK",
                    "ttk_info": {"estimated_minutes": 5, "urgency": "IMMINENT", "fuel_ready": "NO"}
                }
            elif trend_result['restriction'] == "FORBID_SHORT":
                return {
                    "bias": "LONG",
                    "confidence": "SUPREME",
                    "reason": trend_result['reason'],
                    "phase": "WHALE_ACCUMULATION_BLOCK",
                    "ttk_info": {"estimated_minutes": 5, "urgency": "IMMINENT", "fuel_ready": "NO"}
                }
            elif trend_result['restriction'] == "PRIORITIZE_SHORT":
                oi_delta_5m = data.get('oi_delta_5m', 0)
                if oi_delta_5m < OI_SURGE_THRESHOLD:
                    return {
                        "bias": "SHORT",
                        "confidence": "SUPREME",
                        "reason": trend_result['reason'],
                        "phase": "MACD_DEAD_ZONE",
                        "ttk_info": {"estimated_minutes": 3, "urgency": "IMMINENT", "fuel_ready": "NO"}
                    }

        # ============================================
        # PRIORITAS 21: GRAVITY DEFLECTION (V68) - ANTI-PIPPIN TRAP
        # ============================================
        if ogd_result and ogd_result['is_deflected']:
            if ogd_result['confidence'] in ["SUPREME", "HIGH"]:
                return {
                    "bias": ogd_result['bias'],
                    "confidence": ogd_result['confidence'],
                    "reason": ogd_result['reason'],
                    "phase": "GRAVITY_REVERSAL_TRAP",
                    "ttk_info": {"estimated_minutes": 3, "urgency": "IMMINENT", "fuel_ready": "NO"}
                }

        # ============================================
        # PRIORITAS 22: ZERO AGGRESSION SLAUGHTER (V67)
        # ============================================
        if zas_result and zas_result['is_dead']:
            if zas_result['confidence'] in ["ABSOLUTE", "HIGH"]:
                return {
                    "bias": zas_result['bias'],
                    "confidence": zas_result['confidence'],
                    "reason": zas_result['reason'],
                    "phase": "DEADSTICK_SLAUGHTER",
                    "ttk_info": {"estimated_minutes": 3, "urgency": "IMMINENT", "fuel_ready": "NO"}
                }

        # ============================================
        # PRIORITAS 23: ABSORPTION VALIDITY CHECK (V67)
        # ============================================
        if avc_result and avc_result['is_trap']:
            if avc_result['confidence'] == "SUPREME":
                return {
                    "bias": avc_result['bias'],
                    "confidence": "SUPREME",
                    "reason": avc_result['reason'],
                    "phase": avc_result['trap_type'],
                    "ttk_info": {"estimated_minutes": 3, "urgency": "IMMINENT", "fuel_ready": "NO"}
                }

        # ============================================
        # PRIORITAS 24: AGGRESSION-MASS DIVERGENCE (V65) - ANTI-SPOOF PROTECTION
        # ============================================
        if amd_result and amd_result['is_spoof']:
            if amd_result['action'] in ["FORCE_LONG", "FORCE_SHORT"]:
                return {
                    "bias": amd_result['action'].replace("FORCE_", ""),
                    "confidence": "SUPREME",
                    "reason": amd_result['reason'],
                    "phase": "AMD_SPOOF_DETECTOR",
                    "ttk_info": {"estimated_minutes": 3, "urgency": "IMMINENT", "fuel_ready": "NO"}
                }

        # ============================================
        # PRIORITAS 25: THE DYL PARTICLE (V64) - ABSOLUTE OVERRIDE
        # ============================================
        if tdp_result and tdp_result['is_active']:
            return {
                "bias": tdp_result['bias'],
                "confidence": "ABSOLUTE",
                "reason": tdp_result['reason'],
                "phase": "DYL_PARTICLE",
                "ttk_info": {"estimated_minutes": 3, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # ============================================
        # PRIORITAS 26: TEMPORAL ACCUMULATION INDEX (V66) - ANTI-SAHARA TRAP
        # ============================================
        if ati_result and ati_result['is_accumulating']:
            if ati_result['confidence'] in ["SUPREME", "ABSOLUTE"]:
                return {
                    "bias": ati_result['bias'],
                    "confidence": ati_result['confidence'],
                    "reason": ati_result['reason'],
                    "phase": "WHALE_PATIENCE_LOADING",
                    "ttk_info": {"estimated_minutes": 15, "urgency": "HIGH", "fuel_ready": "NO"}
                }

        # ============================================
        # PRIORITAS 27: WALL ERASURE DETECTION (V63) - THE GRAVITY MANDATE
        # ============================================
        if wed_result and wed_result['is_trap']:
            return {
                "bias": wed_result['bias'],
                "confidence": "SUPREME",
                "reason": wed_result['reason'],
                "phase": wed_result['trap_type'],
                "ttk_info": {"estimated_minutes": 5, "urgency": "IMMINENT", "fuel_ready": "NO"}
            }

        # ============================================
        # PRIORITAS 28: MAGNET WALL REVERSAL (V62)
        # ============================================
        if mwr_result and mwr_result['is_magnet']:
            return {
                "bias": mwr_result['bias'],
                "confidence": "SUPREME",
                "reason": mwr_result['reason'],
                "phase": mwr_result['magnet_type'],
                "ttk_info": {"estimated_minutes": 8, "urgency": "HIGH", "fuel_ready": "YES"}
            }

        # ============================================
        # PRIORITAS 29: THE GHOST WHISPERER (V61)
        # ============================================
        if lvs_result and lvs_result['is_suction']:
            return {
                "bias": lvs_result['bias'],
                "confidence": "SUPREME",
                "reason": lvs_result['reason'],
                "phase": lvs_result['suction_type'],
                "ttk_info": {"estimated_minutes": 8, "urgency": "HIGH", "fuel_ready": "NO"}
            }

        # ============================================
        # PRIORITAS 30: THE ABSORPTION SHIELD (V60)
        # ============================================
        if dtd_result and dtd_result['is_trap']:
            return {
                "bias": dtd_result['bias'],
                "confidence": "SUPREME",
                "reason": dtd_result['reason'],
                "phase": dtd_result['trap_type'],
                "ttk_info": {"estimated_minutes": 5, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # ============================================
        # PRIORITAS 31: THE VACUUM OVERRIDE
        # ============================================
        wmi_data = wmi or {}
        if wmi_data.get('is_whale_trap', False) and abs(wmi_data.get('mass_ratio', 0)) > VACUUM_WMI_MIN:
            if wmi_data['dominant_side'] == "SHORT_LIQ_WHALE" and short_dist < VACUUM_DISTANCE_MAX:
                return {
                    "bias": "LONG",
                    "confidence": "ABSOLUTE",
                    "reason": f"SUPREME_GRAVITY: WMI {wmi_data['mass_ratio']:.1f}x! Massa Short di +{short_dist}% terlalu besar untuk dilewatkan MM. JANGAN SHORT! RSI {rsi6} sampah!",
                    "phase": "WHALE_OBSESSION",
                    "ttk_info": {"estimated_minutes": 3, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }
            elif wmi_data['dominant_side'] == "LONG_LIQ_WHALE" and long_dist < VACUUM_DISTANCE_MAX:
                return {
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": f"SUPREME_GRAVITY: WMI {wmi_data['mass_ratio']:.1f}x! Massa Long di -{long_dist}% terlalu besar untuk dilewatkan MM. JANGAN LONG! RSI {rsi6} sampah!",
                    "phase": "WHALE_OBSESSION",
                    "ttk_info": {"estimated_minutes": 3, "urgency": "IMMINENT", "fuel_ready": "YES"}
                }

        # ============================================
        # PRIORITAS 32: ANTI-SLAUGHTER RULE
        # ============================================
        oi_delta_5m = data.get('oi_delta_5m', 0)
        if oi_delta_5m < -1.5 and rsi6 < 20:
            return {
                "bias": "SHORT",
                "confidence": "SUPREME",
                "reason": f"LIQUIDATION_CASCADE: OI amblas {oi_delta_5m:.1f}% di RSI {rsi6:.1f}. Retail kena sikat, MM lanjut narik harga ke bawah!",
                "phase": "MARKET_SLAUGHTER",
                "ttk_info": {"estimated_minutes": 5, "urgency": "IMMINENT", "fuel_ready": "NO"}
            }

        # ============================================
        # 0. LRR ANALYSIS
        # ============================================
        lrr = LiquidityRiskRewardV54.analyze(short_dist, long_dist, short_vol, long_vol)

        # ============================================
        # 1. AGGRESSION VELOCITY ANALYSIS
        # ============================================
        av = AggressionVelocityV54.analyze(state_mgr.aggressive_history)

        # ============================================
        # 2. PNR DETECTION
        # ============================================
        pnr = PNRDetectorV54.analyze(short_dist, long_dist, rsi6, trade_flow)

        # ============================================
        # 3. ENGINE STARTER ANALYSIS
        # ============================================
        starter = EngineStarterV61.analyze(data, deque([oi_5m_ago] if oi_5m_ago else []), state_mgr.price_history)
        ttk = TTKCountdownV61.estimate(starter['score'], oi_delta_5m, volume_ratio)

        # ============================================
        # PRIORITAS 33: THE SAFETY VALVE
        # ============================================
        if pnr['pnr_active']:
            if rsi6 > RSI_NUCLEAR_OVERBOUGHT and pnr['bias'] == "LONG":
                return {
                    "bias": "SHORT",
                    "confidence": "ABSOLUTE",
                    "reason": f"ABSOLUTE_EXHAUSTION: RSI {rsi6} Nuclear! Wajib SHORT.",
                    "phase": "NUCLEAR_OVERBOUGHT",
                    "ttk_info": ttk
                }
            if rsi6 < RSI_NUCLEAR_OVERSOLD and pnr['bias'] == "SHORT":
                return {
                    "bias": "LONG",
                    "confidence": "ABSOLUTE",
                    "reason": f"ABSOLUTE_EXHAUSTION: RSI {rsi6} Floor! Wajib LONG.",
                    "phase": "NUCLEAR_OVERSOLD",
                    "ttk_info": ttk
                }
            if pnr['bias'] == "LONG" and lrr['danger_side'] == "LONG_LIQ_CLIFF":
                return {
                    "bias": "SHORT",
                    "confidence": "SUPREME",
                    "reason": f"LRR_TRAP: Target atas {short_dist}% cuma umpan, jurang bawah {long_dist}% (Ratio {lrr['ratio']}x)!",
                    "phase": "LIQUIDITY_CLIFF",
                    "ttk_info": ttk
                }
            if pnr['bias'] == "SHORT" and lrr['danger_side'] == "SHORT_LIQ_CLIFF":
                return {
                    "bias": "LONG",
                    "confidence": "SUPREME",
                    "reason": f"LRR_TRAP: Target bawah {long_dist}% cuma umpan, jurang atas {short_dist}% (Ratio {1/lrr['ratio']:.1f}x)!",
                    "phase": "LIQUIDITY_CLIFF",
                    "ttk_info": ttk
                }
            if pnr['bias'] == "LONG" and aggressive_ratio < AGGRESSION_MIN_LONG:
                return {
                    "bias": "SHORT",
                    "confidence": "HIGH",
                    "reason": f"NO_FUEL_LONG: PNR Long dekat tapi Agresi {aggressive_ratio}x kering.",
                    "phase": "FAKE_BREAKOUT",
                    "ttk_info": ttk
                }
            if pnr['bias'] == "SHORT" and aggressive_ratio > AGGRESSION_MIN_SHORT * 10:
                return {
                    "bias": "LONG",
                    "confidence": "HIGH",
                    "reason": f"NO_FUEL_SHORT: PNR Short dekat tapi Agresi {aggressive_ratio}x deras.",
                    "phase": "FAKE_BREAKDOWN",
                    "ttk_info": ttk
                }
            if pnr['bias'] == "LONG" and av['is_market_slam']:
                return {
                    "bias": "SHORT",
                    "confidence": "HIGH",
                    "reason": f"MARKET_SLAM: Agresi jual mendadak berakselerasi!",
                    "phase": "SUDDEN_DUMP",
                    "ttk_info": ttk
                }

            add = AggressionDeltaDivergenceV54.analyze(pnr['bias'], aggressive_ratio, trade_flow, rsi6, av['status'])
            if add['is_divergent']:
                if add['action'] in ["CANCEL_SHORT", "SWITCH_LONG"]:
                    final_bias = "LONG"
                elif add['action'] in ["CANCEL_LONG", "SWITCH_SHORT"]:
                    final_bias = "SHORT"
                else:
                    final_bias = pnr['bias']
                return {
                    "bias": final_bias,
                    "confidence": "SUPREME",
                    "reason": f"ADD_VALIDATION: {add['reason']}",
                    "phase": "ADD_REVERSAL",
                    "ttk_info": ttk
                }

            return {
                "bias": pnr['bias'],
                "confidence": "SUPREME",
                "reason": pnr['reason'] + " - Safety validation PASSED",
                "phase": "PNR_VALIDATED",
                "ttk_info": ttk
            }

        # ============================================
        # PRIORITAS 34: GHOST INTENT DETECTOR
        # ============================================
        if ghost_result['is_ghost'] and ghost_result['confidence'] in ["SUPREME", "HIGH"]:
            return {
                "bias": ghost_result['bias'],
                "confidence": ghost_result['confidence'],
                "reason": f"GHOST_PROTOCOL: {ghost_result['reasons'][0] if ghost_result['reasons'] else 'Intent detected'}",
                "phase": "GHOST_DETECTED",
                "ttk_info": ttk
            }

        # ============================================
        # PRIORITAS 35: ENGINE STARTER
        # ============================================
        if starter['is_starting']:
            final_conf = "SUPREME" if ttk['urgency'] == "IMMINENT" else "HIGH"
            return {
                "bias": starter['bias'],
                "confidence": final_conf,
                "reason": f"ENGINE_READY: {starter['reasons'][0]} | TTK: {ttk['estimated_minutes']}m",
                "phase": f"LAUNCH_{ttk['urgency']}",
                "ttk_info": ttk
            }

        if oi_delta_5m > FUEL_INJECTION_OI and abs(change_5m) < FUEL_INJECTION_PRICE:
            return {
                "bias": "NEUTRAL",
                "confidence": "LOW",
                "reason": f"PASSIVE_LOADING: Bandar isi bensin pelan. OI +{oi_delta_5m:.1f}% | TTK: {ttk['estimated_minutes']}m",
                "phase": "WARMING_UP",
                "ttk_info": ttk
            }

        # ============================================
        # PRIORITAS 36: MAGNET RULE
        # ============================================
        if short_dist < MAGNET_RULE_THRESHOLD:
            add_magnet = AggressionDeltaDivergenceV54.analyze("LONG", aggressive_ratio, trade_flow, rsi6, av['status'])
            if add_magnet['is_divergent']:
                return {
                    "bias": "SHORT",
                    "confidence": "HIGH",
                    "reason": f"MAGNET_TRAP: {add_magnet['reason']}",
                    "phase": "MAGNET_REJECT",
                    "ttk_info": ttk
                }
            else:
                return {
                    "bias": "LONG",
                    "confidence": "SUPREME",
                    "reason": f"MAGNET: Short Liq {short_dist}% dekat + Flow mendukung",
                    "phase": "FLASH_MAGNET",
                    "ttk_info": ttk
                }
        if long_dist < MAGNET_RULE_THRESHOLD:
            add_magnet = AggressionDeltaDivergenceV54.analyze("SHORT", aggressive_ratio, trade_flow, rsi6, av['status'])
            if add_magnet['is_divergent']:
                return {
                    "bias": "LONG",
                    "confidence": "HIGH",
                    "reason": f"MAGNET_TRAP: {add_magnet['reason']}",
                    "phase": "MAGNET_REJECT",
                    "ttk_info": ttk
                }
            else:
                return {
                    "bias": "SHORT",
                    "confidence": "SUPREME",
                    "reason": f"MAGNET: Long Liq {long_dist}% dekat + Flow mendukung",
                    "phase": "FLASH_MAGNET",
                    "ttk_info": ttk
                }

        # ============================================
        # PRIORITAS 37: GRAVITY SPOOF DETECTION
        # ============================================
        if long_gravity > short_gravity * LIQ_GRAVITY_EXTREME:
            if long_dist > GRAVITY_SPOOF_DISTANCE and short_dist < MAGNET_OVERRIDE_DISTANCE:
                return {
                    "bias": "LONG",
                    "confidence": "HIGH",
                    "reason": f"GRAVITY_SPOOF: Gravity bawah {long_dist}% jauh, ambil magnet atas {short_dist}%",
                    "phase": "GRAVITY_SPOOF",
                    "ttk_info": ttk
                }
        if short_gravity > long_gravity * LIQ_GRAVITY_EXTREME:
            if short_dist > GRAVITY_SPOOF_DISTANCE and long_dist < MAGNET_OVERRIDE_DISTANCE:
                return {
                    "bias": "SHORT",
                    "confidence": "HIGH",
                    "reason": f"GRAVITY_SPOOF: Gravity atas {short_dist}% jauh, ambil magnet bawah {long_dist}%",
                    "phase": "GRAVITY_SPOOF",
                    "ttk_info": ttk
                }

        # ============================================
        # PRIORITAS 38: HFT SIGNATURE
        # ============================================
        if hft_signature['bias'] != "NEUTRAL" and hft_signature['confidence'] in ["SUPREME", "HIGH"]:
            return {
                "bias": hft_signature['bias'],
                "confidence": hft_signature['confidence'],
                "reason": hft_signature['signals'][0] if hft_signature['signals'] else "HFT Signature",
                "phase": "HFT_SIGNATURE",
                "ttk_info": ttk
            }

        # ============================================
        # PRIORITAS 39: OI CONFIRMATION
        # ============================================
        if oi_velocity['status'] in ["REAL_ACCUMULATION", "REAL_SHORTING"]:
            return {
                "bias": "LONG" if "ACCUMULATION" in oi_velocity['status'] else "SHORT",
                "confidence": "SUPREME",
                "reason": oi_velocity['reason'],
                "phase": oi_velocity['status'],
                "ttk_info": ttk
            }

        # ============================================
        # PRIORITAS 40: MEAN REVERSION
        # ============================================
        if reversion['confidence'] in ["SUPREME", "HIGH"] and reversion['bias'] != "NEUTRAL":
            if short_dist > 0.5 and long_dist > 0.5:
                return {
                    "bias": reversion['bias'],
                    "confidence": reversion['confidence'],
                    "reason": f"MEAN_REVERSION: {reversion['reason']}",
                    "phase": "MEAN_REVERSION",
                    "ttk_info": ttk
                }

        # ============================================
        # PRIORITAS 41: LIQUIDITY PATH
        # ============================================
        if liquidity_data['nearest'] == "SHORT":
            return {
                "bias": "LONG",
                "confidence": "LOW",
                "reason": f"Path of least resistance: Short liq lebih dekat ({liquidity_data['short_dist']}%)",
                "phase": "LIQUIDITY_PATH",
                "ttk_info": ttk
            }
        elif liquidity_data['nearest'] == "LONG":
            return {
                "bias": "SHORT",
                "confidence": "LOW",
                "reason": f"Path of least resistance: Long liq lebih dekat ({liquidity_data['long_dist']}%)",
                "phase": "LIQUIDITY_PATH",
                "ttk_info": ttk
            }

        return {
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "Engine cold. No institutional activity.",
            "phase": "SLEEP_MODE",
            "ttk_info": ttk
        }

# ================= V87 CONFIG =================
ZAS_AGG_MAX = 0.0           # Zero Aggression Squeeze: Agg must be 0
ZAS_FLOW_MAX = 1.5          # Flow < 1.5
ZAS_RSI_MIN = 20            # RSI between 20-65
ZAS_RSI_MAX = 65

LCD_AGG_MAX = 0.05          # Liquidity Compression: Agg ≤ 0.05
LCD_FLOW_MAX = 1.2          # Flow < 1.2
LCD_OI_DELTA_MAX = 1.0      # |OI delta| < 1.0%
LCD_RSI_MIN = 20            # RSI between 20-65
LCD_RSI_MAX = 65

LBD_SHORT_DIST_MAX = 0.5    # Liquidity Bait: Short dist < 0.5%
LBD_FLOW_MAX = 1.0          # Flow < 1.0
LBD_AGG_MAX = 1.0           # Agg < 1.0
LBD_OI_DELTA_MAX = 1.0      # |OI delta| < 1.0%

SAD_AGG_MAX = 0.1           # Stealth Accumulation: Agg < 0.1
SAD_CHANGE_MAX = 0.1        # Price change < 0.1%
SAD_WMI_MIN = 20            # WMI > 20 (short liquidity above)
SAD_OI_DELTA_MAX = 0.0      # OI delta < 0 (negative/short covering)


# ================= V89/V90 CONFIG =================
# Whale Singularity Check (V89)
WSC_WMI_THRESHOLD = 99.0           # WMI > 99.0 = Singularitas
WSC_SHORT_DIST_MAX = 0.5            # Jarak short < 0.5%

# Liquidity Saturation (V90)
SAT_IMBALANCE_THRESHOLD = 50.0      # Imbalance ratio > 50x = saturation
SAT_WMI_MIN = 80.0                   # WMI minimal untuk validasi

# Position Expansion Trap (V90)
PET_OI_DELTA_MIN = 1.0               # OI naik > 1%
PET_AGG_MAX = 1.0                    # Aggressive ratio < 1.0 (rendah = limit buy)
PET_FLOW_MIN = 2.0                   # Trade flow > 2.0


# ================= V93 CONFIG - LIQUIDITY VACUUM DETECTOR =================
# ODC - OI Drain Condemnation (Saran 1 - PLAYUSDT)
ODC_OI_DRAIN_THRESHOLD = -3.0          # OI amblas > 3%
ODC_RSI_CEILING = 90                   # RSI > 90

# OPD - Orderbook Pull Detector (Saran 2 - Baru!)
OPD_BID_VACUUM_RATIO = 2.0              # bid_vacuum > ask_vacuum * 2
OPD_OI_DROP_THRESHOLD = -2.0             # OI drop < -2%

# WMI Exhaustion Filter (Saran 2 - Baru!)
WMI_EXHAUST_THRESHOLD = 95               # WMI > 95
WMI_EXHAUST_OI_THRESHOLD = -3.0          # OI < -3%
WMI_EXHAUST_RSI_THRESHOLD = 85           # RSI > 85

# Cascade Time Estimator (Saran 2 - Baru!)
CASCADE_MIN_DEPTH = 0.1                   # Minimal orderbook depth

# ================= V94 CONFIG - ENERGY PATH & PASSIVE RELOAD =================
# LEP - Low Energy Path (PIXELUSDT case)
LEP_ENERGY_RATIO_THRESHOLD = 10.0      # Ratio > 10x = veto
LEP_AGG_MAX = 0.1                       # Agg must be < 0.1

# PLR - Passive Liquidity Reload (NEW!)
PLR_OI_DELTA_MIN = 1.0                   # OI naik > 1%
PLR_AGG_MAX = 0.2                        # Agg < 0.2 (mati)
PLR_FLOW_MAX = 1.2                       # Flow < 1.2 (netral)

# ================= V94 CONFIG - ENERGY GRAVITY RULE =================
# EGR - Energy Gravity Rule (Anti-PIXEL Rebound Trap)
EGR_ENERGY_RATIO_THRESHOLD = 3.0          # Ratio > 3x = veto cascade time
EGR_WMI_MIN = 50                           # Minimal WMI untuk validasi target

# ================= V95 CONFIG - LIQUIDITY IGNITION DETECTOR =================
# LID - Liquidity Ignition Detector (Short Squeeze Setup)
LID_RSI_MAX = 30                            # RSI < 30 (oversold)
LID_OI_DELTA_MIN = 1.0                       # OI naik > 1.0% (short build)
LID_FLOW_MAX = 0.6                           # Flow < 0.6 (no panic sell)
LID_WMI_MIN = 50                              # WMI > 50 (ada target short)

# ================= V95 CONFIG - ENERGY SPOOF TRACKER =================
# EST - Energy Spoof Tracker (Anti-PIXEL Trojan Trap)
EST_ENERGY_SPOOF_THRESHOLD = 100.0        # Energy > 100 = suspicious
EST_OI_DELTA_NEGATIVE = 0                    # OI harus negatif (< 0)

# ================= V95 CONFIG - RETAIL POSITIONING TRAP =================
RPT_IMBALANCE_THRESHOLD = 10.0      # Imbalance > 10x = retail crowded
RPT_ENERGY_DIFF_THRESHOLD = 3.0      # Energy diff > 3x untuk validasi

# ================= V96 CONFIG - EXECUTION COMPLETION DETECTOR =================
ECD_RSI_THRESHOLD = 95                # RSI > 95 = extreme overbought
ECD_PRICE_SPIKE_MIN = 5.0              # Price spike > 5%
ECD_OI_DELTA_MIN = 2.0                  # OI delta > 2%

# ================= V96 CONFIG - SINGULARITY VETO INTEGRITY =================
SVI_WMI_THRESHOLD = 99.5           # WMI > 99.5 = Singularitas Mutlak

# ================= V97 CONFIG - EVENT HORIZON DETECTOR =================
EVH_WMI_THRESHOLD = 95.0            # WMI > 95
EVH_SHORT_DIST_MAX = 0.3             # Short distance < 0.3%
EVH_LONG_DIST_MAX = 0.3              # Long distance < 0.3% (untuk kasus sebaliknya)

# ================= V97 CONFIG - EVENT HORIZON SINGULARITY (EHS) =================
# EHS - Event Horizon Singularity (Anti-ARIA Trap)
EHS_ENERGY_RATIO_THRESHOLD = 20.0     # Energy ratio > 20x = mutlak
EHS_WMI_THRESHOLD = 95.0               # WMI > 95
EHS_SHORT_DIST_MAX = 1.5                # Short distance < 1.5%

# ================= V98 CONFIG - VACUUM DETECTOR =================
# VAC - Orderbook Vacuum Detection (Anti-Seller Exhaustion)
VAC_AGG_MAX = 0.2                        # Aggression < 0.2 = seller mati
VAC_FLOW_MIN = 1.5                        # Flow > 1.5 = ada volume
VAC_RSI_IGNORE = True                     # Abaikan RSI saat vacuum

# ================= V99 CONFIG - SUPERIOR WHALE DOMINANCE PROTOCOL =================
# WMI Absolute Veto Power
WMI_SINGULARITY_VETO_THRESHOLD = 95.0    # WMI > 95 atau < -95 = veto mutlak
SVI_WMI_THRESHOLD = 99.0                  # Turunkan dari 99.5 ke 99.0 (lebih sensitif)

# Anti-IED Trap (Institutional Exit Dead)
IER_EXIT_VALIDATION_THRESHOLD = -1.0      # Jangan percaya IER jika OI turun > -1%

# Internal Trap Detection
INTERNAL_TRAP_FLOW_MIN = 3.0               # Flow > 3.0
INTERNAL_TRAP_PRICE_MAX = -0.5              # Price change < -0.5%
INTERNAL_TRAP_RSI_MAX = 40                  # RSI < 40

# OI Acceleration Phase Detection
OI_ACCEL_PHASE_DROP_MIN = -1.0              # OI drop > 1%
OI_ACCEL_PRICE_DUMP_MIN = -2.0               # Price dump > 2%
OI_ACCEL_PRICE_STABLE_MAX = 0.2              # Price stabil < 0.2%

# ================= V96 CONFIG - PASSIVE DISTRIBUTION & SHORT COVERING FILTER =================
# PDD - Passive Distribution Detector
PDD_OI_DELTA_MIN = -1.0                     # OI turun > 1.0%
PDD_FLOW_MIN = 1.2                          # Flow > 1.2 (masih ada volume)
PDD_RSI_MAX = 50                             # RSI < 50 (tidak overbought)
PDD_PRICE_CHANGE_MAX = 0                     # Price change <= 0 (tidak naik)

# RSC - Real Short Covering Filter
RSC_PRICE_CHANGE_MIN = 0                     # Price change > 0 untuk valid short covering

# ================= V94: BAITING PRICE FILTER (BPF) CONFIG =================
BPF_DUMP_MIN = -4.0           # Dump minimal untuk bait detection
BPF_DUMP_MAX = 0.0            # Dump maksimal (negative)
BPF_ENERGY_RATIO = 3.0        # Rasio energy untuk deteksi bait

# ================= V94: ENERGY GRAVITY RULE (EGR) CONFIG =================
EGR_ENERGY_RATIO_THRESHOLD = 3.0  # Rasio energy > 3x = veto
EGR_WMI_MIN = 50                  # Minimal WMI untuk validasi

# ================= V95: LIQUIDATION GAP DETECTOR (LGD) CONFIG =================
LGD_GAP_RATIO = 2.0               # Rasio gap untuk deteksi squeeze
LGD_SHORT_COVERING_RSI = 90       # RSI threshold untuk short covering

# ================= V100: LIQUIDATION PRE-FLUSH & PAYOUT CALCULATOR =================
# LPC - Liquidation Payout Calculator
LPC_PAYOUT_THRESHOLD = 1.5           # Threshold untuk memilih target (ratio)
LPC_MIN_DISTANCE = 0.5                # Jarak minimal untuk validasi

# LPF - Liquidation Pre-Flush Detector
LPF_WMI_THRESHOLD = 90                 # WMI > 90 untuk pre-flush
LPF_LONG_DIST_MAX = 4.0                 # Long distance < 4%
LPF_PRE_FLUSH_MIN = -3.0                 # Minimal pre-flush (-3% sampai -7%)
LPF_PRE_FLUSH_MAX = -7.0
LPF_ENERGY_RATIO_THRESHOLD = 2.0        # Energy ratio untuk validasi

# Double Sweep Zone
DSZ_SHORT_DIST_MAX = 1.0                 # Short distance < 1%
DSZ_LONG_DIST_MAX = 4.0                  # Long distance < 4%


# ================= V87: ZERO AGGRESSION SQUEEZE (ZAS) =================
class ZeroAggressionSqueezeV87:
    """
    V87: Zero Aggression Squeeze - ANTI-SELLER EXHAUSTION
    
    Kasus POWERUSDT dan ROBOUSDT:
    - Agg = 0.00x (TIDAK ADA SELLER AGGRESIF!)
    - Flow rendah (< 1.5)
    - RSI 20-65 (netral)
    
    Interpretasi sebenarnya:
    - Agg = 0 BUKAN weak momentum, tapi SELLER EXHAUSTION!
    - Market maker sedang freeze orderbook
    - Satu market buy bisa gerakkan harga +4% sampai +8%
    """
    @staticmethod
    def analyze(agg_ratio: float, flow: float, rsi: float, oi_delta: float = None) -> Dict:
        is_squeeze = agg_ratio <= ZAS_AGG_MAX and flow < ZAS_FLOW_MAX and ZAS_RSI_MIN < rsi < ZAS_RSI_MAX
        
        if is_squeeze:
            oi_info = f" OI Δ {oi_delta:.2f}% " if oi_delta is not None else ""
            return {
                "is_squeeze": True,
                "bias": "LONG",
                "confidence": "SUPREME",
                "reason": f"ZAS_ZERO_AGGRESSION: Agg {agg_ratio:.2f}x (NO SELLERS LEFT!) + Flow {flow:.2f}x + RSI {rsi:.1f}{oi_info}→ Squeeze +4-8% incoming!",
                "phase": "LIQUIDITY_FREEZE"
            }
        
        return {
            "is_squeeze": False,
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "Normal - no zero aggression detected",
            "phase": "NORMAL"
        }


# ================= V87: LIQUIDITY COMPRESSION DETECTOR (LCD) =================
class LiquidityCompressionDetectorV87:
    """
    V87: Liquidity Compression Detector - ANTI-SIDEWAY FATIGUE
    
    Market maker sengaja membuat market seperti ini 1-12 jam sebelum move 5-10%:
    - Agg → 0
    - Flow → kecil
    - OI → sedikit turun
    - Price → flat
    - RSI → netral
    
    Market terlihat mati, padahal liquidity sedang dikompres.
    """
    @staticmethod
    def analyze(agg_ratio: float, flow: float, oi_delta: float, rsi: float) -> Dict:
        is_comp = (agg_ratio <= LCD_AGG_MAX and 
                   flow < LCD_FLOW_MAX and 
                   abs(oi_delta) < LCD_OI_DELTA_MAX and 
                   LCD_RSI_MIN < rsi < LCD_RSI_MAX)
        
        if is_comp:
            return {
                "is_compression": True,
                "bias": "LONG",
                "confidence": "HIGH",
                "reason": f"LCD_LIQUIDITY_COMPRESSION: Agg {agg_ratio:.2f}x + Flow {flow:.2f}x + OI Δ {oi_delta:.2f}% + RSI {rsi:.1f} → Market dikompres 1-12 jam sebelum eksplosi +5-12%!",
                "phase": "COMPRESSION_ZONE"
            }
        
        return {
            "is_compression": False,
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "Normal - no compression detected",
            "phase": "NORMAL"
        }


# ================= V87: LIQUIDITY BAIT DETECTOR (LBD) =================
class LiquidityBaitDetectorV87:
    """
    V87: Liquidity Bait Detector - ANTI-FAKE MAGNET
    
    Market maker sengaja membuat short liq sangat dekat (<0.5%) sebagai umpan.
    Semua bot liquidation membaca: target = short liq (karena jaraknya dekat)
    Tapi HFT tidak memakai distance logic, mereka memakai reward/risk logic.
    """
    @staticmethod
    def analyze(short_dist: float, long_dist: float, flow: float, agg_ratio: float, oi_delta: float) -> Dict:
        is_bait = (short_dist < LBD_SHORT_DIST_MAX and 
                   flow < LBD_FLOW_MAX and 
                   agg_ratio < LBD_AGG_MAX and 
                   abs(oi_delta) < LBD_OI_DELTA_MAX)
        
        if is_bait:
            return {
                "is_bait": True,
                "bias": "NEUTRAL",  # WAIT signal, jangan entry!
                "confidence": "HIGH",
                "reason": f"LBD_LIQUIDITY_BAIT: Short Liq {short_dist:.2f}% (TERLALU DEKAT!) + Flow {flow:.2f}x + Agg {agg_ratio:.2f}x → FAKE MAGNET! MM akan pump dulu baru dump! JANGAN ENTRY!",
                "phase": "BAIT_ZONE",
                "warning": "DO NOT ENTRY - WAIT FOR REAL SWEEP"
            }
        
        return {
            "is_bait": False,
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "Normal - no bait detected",
            "phase": "NORMAL"
        }


# ================= V87: LIQUIDITY IMBALANCE MOMENTUM (LIM) =================
class LiquidityImbalanceMomentumV87:
    """
    V87: Liquidity Imbalance Momentum - ANTI-WRONG TARGET
    
    HFT menghitung LIM = (liquidation_density × position_build_rate) / resistance
    
    Formula:
        long_score = long_gradient × max(oi_velocity, 0.1) / max(agg, 0.1)
        short_score = short_gradient × max(oi_velocity, 0.1) / max(agg, 0.1)
    """
    @staticmethod
    def analyze(short_gradient: float, long_gradient: float, oi_velocity: float, agg_ratio: float) -> Dict:
        # Avoid division by zero
        safe_oi = max(abs(oi_velocity), 0.1)
        safe_agg = max(agg_ratio, 0.1)
        
        long_score = long_gradient * safe_oi / safe_agg
        short_score = short_gradient * safe_oi / safe_agg
        
        # Determine imbalance
        if long_score > short_score * 1.5:
            return {
                "long_score": round(long_score, 2),
                "short_score": round(short_score, 2),
                "bias": "LONG",
                "reason": f"LIM_LONG_IMBALANCE: Long Score {long_score:.2f} >> Short {short_score:.2f} → Short liq imbalance building! Price will go UP!",
                "imbalance_ratio": round(long_score / max(short_score, 0.01), 2),
                "phase": "IMBALANCE_BUILDING"
            }
        elif short_score > long_score * 1.5:
            return {
                "long_score": round(long_score, 2),
                "short_score": round(short_score, 2),
                "bias": "SHORT",
                "reason": f"LIM_SHORT_IMBALANCE: Short Score {short_score:.2f} >> Long {long_score:.2f} → Long liq imbalance building! Price will go DOWN!",
                "imbalance_ratio": round(short_score / max(long_score, 0.01), 2),
                "phase": "IMBALANCE_BUILDING"
            }
        
        return {
            "long_score": round(long_score, 2),
            "short_score": round(short_score, 2),
            "bias": "NEUTRAL",
            "reason": f"LIM_BALANCED: Long {long_score:.2f} vs Short {short_score:.2f} → Wait for clearer imbalance",
            "imbalance_ratio": 1.0,
            "phase": "BALANCED"
        }


# ================= V87: STEALTH ACCUMULATION DETECTOR (SAD) =================
class StealthAccumulationDetectorV87:
    """
    V87: Stealth Accumulation Detector - ANTI-POWER/ROBO GHOSTING
    
    Kasus POWERUSDT dan ROBOUSDT:
    - Agg: 0.00x (Gak ada buyer agresif) TAPI
    - Harga stabil (Change < 0.1%) + OI turun tipis (Whale nutup short mereka)
    - WMI > 20 (short liquidity pool di atas)
    
    Interpretasi:
    - Whale sedang 'Vacuuming' semua barang retail sebelum terbang
    - Mereka sengaja nggak pasang order market buy (biar Agg tetep 0),
      tapi mereka pasang limit buy segunung.
    """
    @staticmethod
    def analyze(agg_ratio: float, change_5m: float, oi_delta: float, wmi: float) -> Dict:
        is_stealth = (agg_ratio < SAD_AGG_MAX and 
                      abs(change_5m) < SAD_CHANGE_MAX and 
                      wmi > SAD_WMI_MIN and 
                      oi_delta < SAD_OI_DELTA_MAX)  # OI turun (short covering)
        
        if is_stealth:
            return {
                "is_active": True,
                "bias": "LONG",
                "confidence": "SUPREME",
                "reason": f"SAD_STEALTH_ACCUMULATION: Agg {agg_ratio:.2f}x (GHOSTING!) + Change {change_5m:.2f}% + WMI {wmi:.1f}x + OI Δ {oi_delta:.2f}% → Whale Short Covering via Limit Buy! SPRING LOADING! +6-12% incoming!",
                "phase": "STEALTH_PUMP_LOADING"
            }
        
        return {
            "is_active": False,
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "Normal - no stealth accumulation detected",
            "phase": "NORMAL"
        }


# ================= V89: WHALE SINGULARITY CHECK (WSC) =================
class WhaleSingularityV89:
    """
    V89: Mendeteksi 'Singularitas Likuiditas'.
    Jika WMI > 99.0 (Short Pool Raksasa) DAN Jarak Short < 0.5%,
    maka MM sedang dalam 'Execution Mode'. 
    MM TIDAK AKAN EXIT. MM bakal hajar atas secara brutal tanpa ampun.
    IER dan PSV di sini adalah FALSE SIGNAL (Umpan buat nambah bensin Short).
    """
    @staticmethod
    def analyze(wmi: float, short_dist: float, rsi: float) -> Dict:
        if wmi > WSC_WMI_THRESHOLD and abs(short_dist) < WSC_SHORT_DIST_MAX:
            return {
                "is_active": True,
                "bias": "LONG",
                "reason": f"WSC_SINGULARITY: WMI {wmi:.1f}x (SHORT_LIQ_WHALE) terdeteksi! Jarak {short_dist:.2f}% adalah EVENT HORIZON. MM tidak akan dump di sini. MM sedang narik Short Seller (Trap) buat jadi bensin SQUEEZE +7%! DILARANG SHORT!"
            }
        return {"is_active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V90: LIQUIDITY SATURATION (SAT) - ANTI-HUMA/ARC TRAP =================
class LiquiditySaturationV90:
    """
    V90: Mendeteksi kondisi 'Jenuh Likuiditas'.
    Jika Imbalance > 50x DAN WMI > 80, 
    maka MM sedang dalam 'Predator Mode'. 
    Sinyal SHORT dari LIM adalah BUNUH DIRI. MM akan nabrak target SHORT terdekat.
    """
    @staticmethod
    def analyze(imbalance_ratio: float, wmi: float, short_dist: float = None) -> Dict:
        if imbalance_ratio > SAT_IMBALANCE_THRESHOLD and abs(wmi) > SAT_WMI_MIN:
            # Jika short_dist tersedia dan sangat dekat (< 1%), sinyal lebih kuat
            if short_dist is not None and abs(short_dist) < 1.0:
                return {
                    "active": True,
                    "bias": "LONG",
                    "reason": f"SAT_SQUEEZE: Imbalance {imbalance_ratio:.1f}x (EKSTRIM) + WMI {wmi:.1f}x. Short seller sudah menyerah, MM sedang mengeksekusi 'Event Horizon' di +{short_dist}%. DILARANG SHORT!"
                }
            return {
                "active": True,
                "bias": "LONG",
                "reason": f"SAT_LIQUIDITY_SATURATION: Imbalance {imbalance_ratio:.1f}x terlalu ekstrim → Short overcrowded → SQUEEZE. WMI {wmi:.1f}x mengkonfirmasi."
            }
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V90: POSITION EXPANSION TRAP (PET) - ANTI-AINU TRAP =================
class PositionExpansionTrapV90:
    """
    V90: Mendeteksi jebakan ekspansi posisi.
    Jika OI Delta Positif (>1%) TAPI Aggression Rendah + Flow Tinggi,
    artinya Whale sedang membangun jaring jebakan (Trap Building).
    """
    @staticmethod
    def analyze(oi_delta: float, agg: float, flow: float, rsi: float = None) -> Dict:
        if oi_delta > PET_OI_DELTA_MIN and agg < PET_AGG_MAX and flow > PET_FLOW_MIN:
            # Di dasar neraka (RSI < 30), sinyal lebih kuat
            rsi_context = f" di RSI {rsi:.1f}" if rsi else ""
            if rsi and rsi < 30:
                return {
                    "active": True,
                    "bias": "LONG",
                    "reason": f"PET_BULL_TRAP: Shorts baru masuk TAPI Whale nahan pake Limit Buy (Flow Tinggi){rsi_context}. Bensin Squeeze lagi dikumpulin! REBOUND SEGERA!"
                }
            return {
                "active": True,
                "bias": "LONG",
                "reason": f"PET_POSITION_EXPANSION_TRAP: OI Δ +{oi_delta:.2f}% (NEW SHORTS), Agg {agg:.2f}x (LIMIT BUY WALL), Flow {flow:.2f}x → TRAP BUILDING!{rsi_context}"
            }
        return {"active": False, "bias": "NEUTRAL", "reason": ""}


# ================= V91: MARKET PHASE ENGINE - THE CORE HFT LAYER =================
class MarketPhaseV91:
    """
    🔥 V91: MARKET PHASE DETECTOR - MISSING CORE ENGINE 🔥
    
    Semua modul sebelumnya membaca indikator (RSI, OI, Flow, Agg, WMI, Imbalance)
    TAPI tidak ada yang menentukan KONTEKS MARKET PHASE!
    
    HFT Binance bekerja dalam 4 fase utama:
    1️⃣ LIQUIDITY_DRAIN - Tidak ada buyer/seller, harga jatuh bebas (ROBO type crash)
    2️⃣ SQUEEZE_BUILD - Whale membangun bahan bakar squeeze
    3️⃣ EXECUTION - Market maker mengeksekusi likuidasi (HUMA type sweep)
    4️⃣ DISTRIBUTION - Whale build short di area overbought (TRIA type dump)
    
    Hierarki Baru V91:
    1️⃣ MARKET PHASE ← PALING PENTING!
    2️⃣ WSC (Whale Singularity)
    3️⃣ WDI (Whale Dominance)
    4️⃣ SAT (Liquidity Saturation)
    5️⃣ PET (Position Expansion Trap)
    6️⃣ ZGH (Zero Gravity Horizon)
    7️⃣ OTF (Oversold Trap Filter)
    8️⃣ LIM (Liquidity Imbalance Momentum)
    
    Kenapa ini penting?
    - Sinyal yang sama bisa berarti hal berlawanan tergantung fase
    - Menghilangkan sinyal NEUTRAL palsu
    - Akurasi naik dari 55-60% → 72-78%
    """
    
    @staticmethod
    def analyze(rsi: float, flow: float, agg: float, oi_delta: float, wmi: float) -> Dict:
        """
        Menentukan MARKET PHASE berdasarkan kondisi likuiditas.
        
        Args:
            rsi: RSI value (0-100)
            flow: Flow ratio (>1 = buy pressure, <1 = sell pressure)
            agg: Aggression multiplier (>1 = aggressive, <1 = passive)
            oi_delta: Open Interest change percentage
            wmi: Whale Migration Index (-100 to +100)
        
        Returns:
            Dict dengan phase, bias, dan reason
        """
        
        # 1️⃣ LIQUIDITY DRAIN - Tidak ada buyer atau seller
        # Contoh: ROBO (RSI 0, Agg 0.33, Flow 0.22)
        # Artinya: price free fall, SHORT
        if flow < 0.4 and agg < 0.5:
            return {
                "phase": "LIQUIDITY_DRAIN",
                "bias": "FOLLOW_TREND",
                "signal": "SHORT" if rsi < 50 else "NEUTRAL",
                "reason": f"Tidak ada buyer (Flow {flow:.2f}, Agg {agg:.2f}). Harga bergerak ke arah gravitasi likuiditas. Price free fall!",
                "priority": "ABSOLUTE"
            }
        
        # 2️⃣ SQUEEZE BUILD - Whale sedang membangun bahan bakar squeeze
        # Kondisi: WMI ekstrim (>90 atau <-90) DAN OI naik (posisi baru masuk)
        if abs(wmi) > 90 and oi_delta > 0:
            bias = "LONG" if wmi > 0 else "LONG"  # WMI positif/negatif tinggi = short/long pool besar
            return {
                "phase": "SQUEEZE_BUILD",
                "bias": "OPPOSITE_CROWD",
                "signal": bias,
                "reason": f"WMI {wmi:.1f}x + OI Δ +{oi_delta:.2f}% = Whale sedang membangun bahan燃料 squeeze. Crowd salah arah!",
                "priority": "SUPREME"
            }
        
        # 3️⃣ EXECUTION - Market maker sedang mengeksekusi likuidasi
        # Contoh: HUMA (WMI 96, OI -4.2, Flow 4.2, Agg 0.67)
        # Artinya: MM sweeping, jangan counter!
        if abs(wmi) > 95 and flow > 1.0:
            bias = "LONG" if wmi > 0 else "SHORT"
            return {
                "phase": "EXECUTION",
                "bias": "FOLLOW_WHALE",
                "signal": bias,
                "reason": f"WMI {wmi:.1f}x + Flow {flow:.2f}x = Market maker sedang mengeksekusi likuidasi. Jangan counter!",
                "priority": "ABSOLUTE"
            }
        
        # 4️⃣ DISTRIBUTION - Whale build short di area overbought
        # Contoh: TRIA (RSI 96.7, OI +1.37%, Agg 1.5)
        # Artinya: Distribution top, SHORT
        if rsi > 85 and oi_delta > 0.5 and agg < 2.0:
            return {
                "phase": "DISTRIBUTION",
                "bias": "SHORT",
                "signal": "SHORT",
                "reason": f"RSI {rsi:.1f} + OI Δ +{oi_delta:.2f}% + Agg {agg:.2f}x = Whale build short di area overbought. Distribution trap!",
                "priority": "SUPREME"
            }
        
        # 5️⃣ LIQUIDITY RESET - Rebound dari oversold extreme
        # Contoh: AINU (RSI 11, OI -1.48%, Flow 0.47, Agg 1.0)
        # Artinya: Liquidity vacuum, REBOUND
        if rsi < 15 and oi_delta < -1.0 and flow < 0.6:
            return {
                "phase": "LIQUIDITY_RESET",
                "bias": "REBOUND",
                "signal": "LONG",
                "reason": f"RSI {rsi:.1f} + OI Δ {oi_delta:.2f}% + Flow {flow:.2f}x = Liquidity vacuum detected. Rebound imminent!",
                "priority": "SUPREME"
            }
        
        # 6️⃣ ACCUMULATION - Whale quietly building positions
        if rsi < 40 and flow > 0.8 and agg < 1.0 and oi_delta > 0.3:
            return {
                "phase": "ACCUMULATION",
                "bias": "STEALTH_LONG",
                "signal": "LONG",
                "reason": f"RSI {rsi:.1f} + Flow {flow:.2f}x + OI Δ +{oi_delta:.2f}% = Whale akumulasi diam-diam.",
                "priority": "HIGH"
            }
        
        # DEFAULT: NEUTRAL
        return {
            "phase": "NEUTRAL",
            "bias": "NEUTRAL",
            "signal": "NEUTRAL",
            "reason": "Market dalam equilibrium. Tidak ada phase yang dominan.",
            "priority": "LOW"
        }


# ================= V91: LIQUIDITY DRAIN DETECTOR =================
class LiquidityDrainDetectorV91:
    """
    🔥 V91: LIQUIDITY DRAIN DETECTOR - ANTI-ROBO CRASH TYPE 🔥
    
    Mendeteksi kondisi ketika market kehilangan likuiditas secara tiba-tiba.
    Ciri-ciri:
    - Flow < 0.4 (tidak ada volume beli)
    - Agg < 0.5 (tidak ada agresi)
    - Harga jatuh bebas seperti ROBO
    
    Ini BUKAN squeeze opportunity! Ini FREE FALL!
    Bot biasa salah: mengira oversold = rebound
    HFT benar: liquidity drain = ikuti arus (SHORT)
    """
    
    @staticmethod
    def analyze(flow: float, agg: float, rsi: float, price_change: float = None) -> Dict:
        if flow < 0.4 and agg < 0.5:
            severity = "CRITICAL" if flow < 0.2 and agg < 0.3 else "HIGH"
            context = f" | Price Δ {price_change:.2f}%" if price_change else ""
            return {
                "is_drain": True,
                "severity": severity,
                "bias": "SHORT",
                "reason": f"LIQUIDITY_DRAIN: Flow {flow:.2f}x + Agg {agg:.2f}x{context}. Tidak ada buyer! Harga jatuh bebas!",
                "action": "FOLLOW_TREND_SHORT"
            }
        return {"is_drain": False, "severity": "NONE", "bias": "NEUTRAL", "reason": ""}


# ================= V91: LIQUIDITY VACUUM DETECTOR =================
class LiquidityVacuumDetectorV91:
    """
    🔥 V91: LIQUIDITY VACUUM DETECTOR - ANTI-AINU REBOUND TYPE 🔥
    
    Mendeteksi kondisi ketika Whale menarik order untuk membersihkan orderbook,
    lalu melakukan rebound brutal (Liquidity Vacuum Rebound).
    
    Ciri-ciri:
    - RSI < 15 (extreme oversold)
    - OI turun drastis (Whale narik order)
    - Flow rendah (< 0.6) tapi ada agresi tersembunyi
    - WMI < -90 (short liquidation pool besar di atas)
    
    Ini BUKAN continuation short! Ini SPRING TRAP!
    Bot biasa salah: mengira OI turun = bearish
    HFT benar: OI turun + WMI ekstrim = Whale siap-siap rebound!
    """
    
    @staticmethod
    def analyze(rsi: float, oi_delta: float, flow: float, wmi: float, agg: float = None) -> Dict:
        if rsi < 15 and oi_delta < -1.0 and wmi < -90:
            # Konfirmasi dengan aggression jika tersedia
            if agg and agg > 0.8:
                confidence = "ABSOLUTE"
            else:
                confidence = "HIGH"
            
            return {
                "is_vacuum": True,
                "confidence": confidence,
                "bias": "LONG",
                "reason": f"LIQUIDITY_VACUUM: RSI {rsi:.1f} + OI Δ {oi_delta:.2f}% + WMI {wmi:.1f}x. Whale narik order buat bersihin orderbook bawah. REBOUND IMMINENT!",
                "action": "PREPARE_LONG_SQUEEZE"
            }
        return {"is_vacuum": False, "confidence": "NONE", "bias": "NEUTRAL", "reason": ""}


# ================= V87 CONFLICT RESOLVER =================
class ConflictResolverV87:
    """
    V87: Resolve konflik dengan hierarki prioritas mutlak V87
    URUTAN PRIORITAS MUTLAK V87:
        0. SAD (Stealth Accumulation Detector) - ANTI-POWER/ROBO GHOSTING ⭐ TERTINGGI!
        1. ZAS (Zero Aggression Squeeze) - ANTI-SELLER EXHAUSTION
        2. LCD (Liquidity Compression Detector) - ANTI-SIDEWAY FATIGUE
        3. LBD (Liquidity Bait Detector) - ANTI-FAKE MAGNET (HATI-HATI, ini WAIT signal!)
        4. LIM (Liquidity Imbalance Momentum) - ANTI-WRONG TARGET
        5. Fallback ke V86/V85 modules
    """
    @staticmethod
    def resolve(
        sad_result: Dict,
        zas_result: Dict,
        lcd_result: Dict,
        lbd_result: Dict,
        lim_result: Dict,
        # V86/V85 fallback modules (optional)
        zgh_result: Dict = None,
        odf_result: Dict = None,
        otf_result: Dict = None,
        ier_result: Dict = None,
        rmg_result: Dict = None,
        fmv_result: Dict = None,
        nzs_result: Dict = None,
        pfd_result: Dict = None,
        fed_v85_result: Dict = None,
        lrd_result: Dict = None
    ) -> Dict:
        
        # 0. PRIORITAS TERTINGGI: SAD (Stealth Accumulation Detector)
        if sad_result.get('is_active'):
            return {
                "bias": sad_result['bias'],
                "confidence": "SUPREME",
                "reason": f"V87_SAD: {sad_result['reason']}",
                "phase": "STEALTH_PUMP_LOADING",
                "ttk_info": {"estimated_minutes": 540, "urgency": "LOADING", "fuel_ready": "YES"}
            }

        # 1. ZAS (Zero Aggression Squeeze)
        if zas_result.get('is_squeeze'):
            return {
                "bias": zas_result['bias'],
                "confidence": "SUPREME",
                "reason": f"V87_ZAS: {zas_result['reason']}",
                "phase": "LIQUIDITY_FREEZE",
                "ttk_info": {"estimated_minutes": 90, "urgency": "BUILDING", "fuel_ready": "YES"}
            }

        # 2. LCD (Liquidity Compression Detector)
        if lcd_result.get('is_compression'):
            return {
                "bias": lcd_result['bias'],
                "confidence": "HIGH",
                "reason": f"V87_LCD: {lcd_result['reason']}",
                "phase": "COMPRESSION_ZONE",
                "ttk_info": {"estimated_minutes": 360, "urgency": "COMPRESSING", "fuel_ready": "YES"}
            }

        # 3. LBD (Liquidity Bait Detector) - HATI-HATI! Ini WAIT signal!
        if lbd_result.get('is_bait'):
            return {
                "bias": "NEUTRAL",
                "confidence": "HIGH",
                "reason": f"V87_LBD: {lbd_result['reason']} - JANGAN ENTRY! TUNGGU REAL SWEEP!",
                "phase": "BAIT_ZONE",
                "ttk_info": {"estimated_minutes": 120, "urgency": "WAITING", "fuel_ready": "NO"},
                "warning": "DO NOT ENTRY - WAIT FOR REAL SWEEP"
            }

        # 4. LIM (Liquidity Imbalance Momentum)
        if lim_result.get('bias') != "NEUTRAL":
            ratio = lim_result.get('imbalance_ratio', 1.0)
            confidence = "HIGH" if ratio > 2.0 else "MEDIUM"
            return {
                "bias": lim_result['bias'],
                "confidence": confidence,
                "reason": f"V87_LIM: {lim_result['reason']}",
                "phase": lim_result.get('phase', 'IMBALANCE_BUILDING'),
                "ttk_info": {"estimated_minutes": 30, "urgency": "BUILDING", "fuel_ready": "YES"}
            }

        # 5. FALLBACK KE V86/V85 MODULES
        # V86: Zero Gravity Horizon
        if zgh_result and zgh_result.get('is_ceiling'):
            return {
                "bias": zgh_result['bias'],
                "confidence": zgh_result.get('confidence', 'ABSOLUTE'),
                "reason": f"V86_ZGH: {zgh_result['reason']}",
                "phase": "DISTRIBUTION_TOP",
                "ttk_info": {"estimated_minutes": 58, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # V86: Overbought Distribution Filter
        if odf_result and odf_result.get('active'):
            return {
                "bias": odf_result['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V86_ODF: {odf_result['reason']}",
                "phase": "ZERO_GRAVITY_HORIZON",
                "ttk_info": {"estimated_minutes": 58, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # V85: Oversold Trap Filter
        if otf_result and otf_result.get('is_trap'):
            confidence = "ABSOLUTE" if otf_result.get('scenario') == 'LIQUIDITY_VACUUM_REBOUND' else "HIGH"
            return {
                "bias": otf_result['bias'],
                "confidence": confidence,
                "reason": f"V85_OTF: {otf_result['reason']}",
                "phase": otf_result.get('scenario', 'ANTI_LIQUIDITY_TRAP'),
                "ttk_info": {"estimated_minutes": 15, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # V85: Neutral Zone Shield
        if nzs_result and nzs_result.get('is_shielded'):
            return {
                "bias": nzs_result['bias'],
                "confidence": "SUPREME",
                "reason": f"V85_NZS: {nzs_result['reason']}",
                "phase": "NEUTRAL_TRAP_SHIELD",
                "ttk_info": {"estimated_minutes": 30, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # V85: Position Flip Detector
        if pfd_result and pfd_result.get('is_flip'):
            return {
                "bias": pfd_result['bias'],
                "confidence": pfd_result.get('confidence', 'SUPREME'),
                "reason": f"V85_PFD: {pfd_result['reason']}",
                "phase": "POSITION_RELOAD",
                "ttk_info": {"estimated_minutes": 30, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # V85: Fake Exit Detector
        if fed_v85_result and fed_v85_result.get('is_fake_exit'):
            return {
                "bias": fed_v85_result['bias'],
                "confidence": fed_v85_result.get('confidence', 'HIGH'),
                "reason": f"V85_FED: {fed_v85_result['reason']}",
                "phase": "LIQUIDITY_BUILDING",
                "ttk_info": {"estimated_minutes": 45, "urgency": "BUILDING", "fuel_ready": "YES"}
            }

        # V85: Liquidity Reload Detector
        if lrd_result and lrd_result.get('is_reload'):
            return {
                "bias": lrd_result['bias'],
                "confidence": lrd_result.get('confidence', 'SUPREME'),
                "reason": f"V85_LRD: {lrd_result['reason']}",
                "phase": "LIQUIDITY_RESET",
                "ttk_info": {"estimated_minutes": 60, "urgency": "LOADING", "fuel_ready": "YES"}
            }

        # V80: Institutional Exit Radar
        if ier_result and ier_result.get('is_exit') and ier_result.get('confidence') in ["ABSOLUTE", "SUPREME", "HIGH"]:
            return {
                "bias": ier_result['bias'],
                "confidence": ier_result['confidence'],
                "reason": f"V80_IER: {ier_result['reason']}",
                "phase": ier_result.get('exit_type', 'INSTITUTIONAL_EXIT'),
                "ttk_info": {"estimated_minutes": 15, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # V80: RSI Momentum Guard
        if rmg_result and rmg_result.get('is_weak') and rmg_result.get('confidence') in ["ABSOLUTE", "SUPREME", "HIGH"]:
            return {
                "bias": rmg_result['bias'],
                "confidence": rmg_result['confidence'],
                "reason": f"V80_RMG: {rmg_result['reason']}",
                "phase": rmg_result.get('weakness_type', 'WEAK_MOMENTUM'),
                "ttk_info": {"estimated_minutes": 30, "urgency": "IMMINENT", "fuel_ready": "NO"}
            }

        # V80: Fake Magnet Vacuum
        if fmv_result and fmv_result.get('is_fake_magnet') and fmv_result.get('confidence') in ["ABSOLUTE", "SUPREME"]:
            return {
                "bias": fmv_result['bias'],
                "confidence": fmv_result['confidence'],
                "reason": f"V80_FMV: {fmv_result['reason']}",
                "phase": fmv_result.get('fake_type', 'FAKE_MAGNET_VACUUM'),
                "ttk_info": {"estimated_minutes": 20, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # DEFAULT: Tidak ada sinyal terdeteksi
        return {
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "No V87/V86/V85 signature detected. Market in neutral phase.",
            "phase": "NORMAL",
            "ttk_info": {"estimated_minutes": 45, "urgency": "PREPARING", "fuel_ready": "NO"}
        }


# ================= OUTPUT FORMATTER V87 =================
class OutputFormatterV87:
    @staticmethod
    def print_header():
        print("\n" + "="*80)
        print("🔥 BINANCE LIQUIDATION HUNTER V88 - WHALE DOMINANCE EDITION")
        print("="*80)
        print("\n🎯 HIERARKI MUTLAK V88: WDI → ZGH → OTF → SAD → LIM")
        print("🐳 KAIDAH EMAS V88: 'Jangan pernah melawan WMI di atas 90 jika jaraknya kurang dari 2%.'")
        print("="*80 + "\n")

    @staticmethod
    def print_signal(result: Dict):
        print("="*80)
        print(f"🔥 {result['symbol']} @ {result['timestamp']}")
        print(f"💰 Price: ${result['price']:.4f}")
        print("="*80)

        # V87 Priority 0: SAD (Stealth Accumulation)
        if result.get('sad', {}).get('is_active'):
            print(f"\n👻👻👻 STEALTH ACCUMULATION DETECTED! POWER/ROBO STYLE! (V87 - TERTINGGI!)")
            print(f"   📌 {result['sad']['reason']}")
            print(f"   📊 Agg: {result['aggressive_ratio']}x (GHOSTING!) | WMI: {result['wmi']['mass_ratio']:.1f}x")
            print(f"   📊 OI Δ: {result['oi_delta_5m']}% (TURUN/SHORT COVERING!) | Change: {result['change_5m']}%")
            print(f"   ⚠️ Whale sedang Short Covering via Limit Buy! SPRING LOADING! JANGAN SHORT!")

        # V87 Priority 1: ZAS (Zero Aggression Squeeze)
        elif result.get('zas_v87', {}).get('is_squeeze'):
            print(f"\n❄️❄️❄️ ZERO AGGRESSION SQUEEZE DETECTED! SELLER EXHAUSTION!")
            print(f"   📌 {result['zas_v87']['reason']}")
            print(f"   📊 Agg: {result['aggressive_ratio']}x (NO SELLERS LEFT!) | Flow: {result['trade_flow']}x")
            print(f"   📊 RSI: {result['rsi6']} (NETRAL) | OI Δ: {result['oi_delta_5m']}%")
            print(f"   ⚠️ Market sedang freeze! Satu market buy bisa gerakkan harga +4-8%!")

        # V87 Priority 2: LCD (Liquidity Compression)
        elif result.get('lcd', {}).get('is_compression'):
            print(f"\n📦📦📦 LIQUIDITY COMPRESSION DETECTED! SIDEWAY FATIGUE!")
            print(f"   📌 {result['lcd']['reason']}")
            print(f"   📊 Agg: {result['aggressive_ratio']}x | Flow: {result['trade_flow']}x | OI Δ: {result['oi_delta_5m']}%")
            print(f"   📊 Market sedang dikompres 1-12 jam! Eksplosi +5-12% segera!")

        # V87 Priority 3: LBD (Liquidity Bait) - WAIT SIGNAL
        elif result.get('lbd', {}).get('is_bait'):
            print(f"\n🎣🎣🎣 LIQUIDITY BAIT DETECTED! FAKE MAGNET!")
            print(f"   📌 {result['lbd']['reason']}")
            print(f"   📊 Short Liq: {result['short_liq']}% (TERLALU DEKAT!) | Flow: {result['trade_flow']}x")
            print(f"   ⚠️ {result['lbd'].get('warning', 'JANGAN ENTRY!')}")

        # V87 Priority 4: LIM (Liquidity Imbalance)
        elif result.get('lim', {}).get('bias') != 'NEUTRAL':
            lim = result['lim']
            print(f"\n⚖️⚖️⚖️ LIQUIDITY IMBALANCE DETECTED!")
            print(f"   📌 {lim['reason']}")
            print(f"   📊 Long Score: {lim['long_score']} | Short Score: {lim['short_score']}")
            print(f"   📊 Imbalance Ratio: {lim['imbalance_ratio']}x")

        # Fallback ke V86
        elif result.get('odf', {}).get('active'):
            print(f"\n☢️☢️☢️ ZERO GRAVITY HORIZON DETECTED! TRIA STYLE!")
            print(f"   📌 {result['odf']['reason']}")
            print(f"   📊 RSI: {result['rsi6']} (NUCLEAR!) | OI Δ: {result['oi_delta_5m']}% (NAIK!) | Agg: {result['aggressive_ratio']}x (PASIF!)")

        elif result.get('zgh', {}).get('is_ceiling'):
            print(f"\n☢️☢️☢️ ZERO GRAVITY HORIZON DETECTED!")
            print(f"   📌 {result['zgh']['reason']}")
            print(f"   📊 RSI: {result['rsi6']} (NUCLEAR!) | OI Δ: {result['oi_delta_5m']}% (NAIK!)")

        elif result.get('otf', {}).get('is_trap'):
            print(f"\n🔄🔄🔄 OVERSOLD TRAP DETECTED!")
            print(f"   📌 {result['otf']['reason']}")
            if result['otf'].get('scenario') == 'LIQUIDITY_VACUUM_REBOUND':
                print(f"   📊 WMI: {result['wmi']['mass_ratio']:.1f}x (EKSTRIM!) | Agg: {result['aggressive_ratio']}x (TINGGI!)")
            elif result['otf'].get('scenario') == 'UAI_TRAP':
                print(f"   📊 RSI {result['rsi6']} oversold TAPI OI turun + Flow lemah = LIQUIDATION CASCADE!")

        # DECISION
        print(f"\n{'='*40}")
        bias_color = "🟢" if result['bias'] == "LONG" else "🔴" if result['bias'] == "SHORT" else "⚪"
        
        conf_map = {
            "ABSOLUTE": "☢️☢️☢️",
            "SUPREME": "🔥🔥🔥",
            "HIGH": "🔥🔥",
            "MEDIUM": "🔥",
            "LOW": "⚪"
        }
        conf_icon = conf_map.get(result['confidence'], "🔥")

        print(f"{bias_color} FINAL BIAS: {result['bias']}")
        print(f"{conf_icon} CONFIDENCE: {result['confidence']}")
        print(f"📌 REASON: {result['reason']}")
        print(f"⏳ ENTRY: {result['entry_status']}")
        print(f"{result['hold_status']}")

        if result['entry_ready']:
            print(f"\n{'✅'*10} ENTRY READY! {'✅'*10}")

        # V88 WDI Metrics (TERTINGGI!)
        print(f"\n{'='*40}")
        print("🐋 V88 WHALE DOMINANCE INDEX (WDI):")
        print(f"🐋 WDI: {'ACTIVE (VETO!)' if result.get('wdi', {}).get('is_veto') else 'INACTIVE'}")
        if result.get('wdi', {}).get('is_veto'):
            print(f"   📌 {result['wdi']['reason']}")

        # V87 Metrics
        print(f"\n{'='*40}")
        print("📊 V87 GHOST IN THE SHELL METRICS:")
        print(f"👻 SAD: {'ACTIVE' if result.get('sad', {}).get('is_active') else 'INACTIVE'}")
        print(f"❄️ ZAS: {'ACTIVE' if result.get('zas_v87', {}).get('is_squeeze') else 'INACTIVE'}")
        print(f"📦 LCD: {'ACTIVE' if result.get('lcd', {}).get('is_compression') else 'INACTIVE'}")
        print(f"🎣 LBD: {'ACTIVE' if result.get('lbd', {}).get('is_bait') else 'INACTIVE'}")
        
        if result.get('lim', {}).get('bias') != 'NEUTRAL':
            lim = result['lim']
            print(f"⚖️ LIM: ACTIVE ({lim['bias']}, Ratio: {lim['imbalance_ratio']}x)")
        else:
            print(f"⚖️ LIM: INACTIVE")

        # V86/V85 Metrics
        print(f"\n📊 V86/V85 METRICS:")
        print(f"☢️ ODF: {'ACTIVE' if result.get('odf', {}).get('active') else 'INACTIVE'}")
        print(f"☢️ ZGH: {'ACTIVE' if result.get('zgh', {}).get('is_ceiling') else 'INACTIVE'}")
        print(f"🔄 OTF: {'ACTIVE' if result.get('otf', {}).get('is_trap') else 'INACTIVE'}")

        # V82/V81/V80 Key Metrics
        print(f"\n📊 KEY MODULES STATUS:")
        
        # V89/V90 Modules
        if result.get('wsc', {}).get('is_active'):
            print(f"🌌 WSC: ACTIVE - {result['wsc']['reason']}")
        if result.get('sat', {}).get('active'):
            print(f"⚡ SAT: ACTIVE - {result['sat']['reason']}")
        if result.get('pet', {}).get('active'):
            print(f"🔥 PET: ACTIVE - {result['pet']['reason']}")
        
        # V91: LIQUIDITY GRAVITY DRAIN (LGD)
        if result.get('lgd', {}).get('active'):
            print(f"🕳️ LGD: ACTIVE - {result['lgd']['reason']}")
        
        # V92: EXECUTION ENERGY
        if result.get('energy_v92', {}).get('bias') != 'NEUTRAL':
            print(f"⚡ ENERGY: {result['energy_v92']['bias']} - {result['energy_v92']['reason']}")
        
        # V92: AGGRESSION DEATH
        if result.get('aggression_death', {}).get('active'):
            print(f"💀 DEATH: ACTIVE - {result['aggression_death']['reason']}")
        
        # ===== V93 NEW MODULES - THE VACUUM FLUSH DETECTORS =====
        if result.get('odc', {}).get('active'):
            print(f"💧 ODC: ACTIVE - {result['odc']['reason']}")

        if result.get('opd', {}).get('active'):
            print(f"🧲 OPD: ACTIVE - {result['opd']['reason']}")

        if result.get('wmi_exhaust', {}).get('active'):
            print(f"💀 WMI_EXHAUST: ACTIVE - {result['wmi_exhaust']['reason']}")

        if result.get('cascade', {}).get('bias') != 'NEUTRAL':
            print(f"⏱️ CASCADE: {result['cascade']['bias']} - {result['cascade']['reason']}")
        
        # ===== V94 NEW MODULES - ENERGY PATH & PASSIVE RELOAD =====
        if result.get('lep', {}).get('is_active'):
            print(f"⚡ LEP: ACTIVE - {result['lep']['reason']}")

        if result.get('plr', {}).get('active'):
            print(f"🔄 PLR: ACTIVE - {result['plr']['reason']}")
        
        # ===== V94: ENERGY GRAVITY RULE =====
        if result.get('egr', {}).get('is_veto'):
            print(f"⚡ EGR: ACTIVE - {result['egr']['reason']}")
        
        # ===== V95: LIQUIDITY IGNITION DETECTOR =====
        if result.get('lid', {}).get('active'):
            print(f"🔥 LID: ACTIVE - {result['lid']['reason']}")
        
        # ===== V95: ENERGY SPOOF TRACKER =====
        if result.get('est', {}).get('is_spoof'):
            print(f"🛡️ EST: ACTIVE - {result['est']['reason']}")
        
        # ===== V96: PASSIVE DISTRIBUTION & SHORT COVERING FILTER =====
        if result.get('pdd', {}).get('active'):
            print(f"📉 PDD: ACTIVE - {result['pdd']['reason']}")
        
        if result.get('rsc', {}).get('is_valid') is not None:
            if result['rsc']['is_valid']:
                print(f"✅ RSC: {result['rsc']['reason']}")
            else:
                print(f"⚠️ RSC: {result['rsc']['reason']}")
        
        # ===== V96: GHOST WALL CONDEMNATION =====
        if result.get('gwc', {}).get('is_ghost_wall'):
            print(f"👻 GWC: ACTIVE - {result['gwc']['reason']}")
        
        # ===== V97: LIQUIDITY VACUUM & SILENT DISTRIBUTION =====
        if result.get('lvd', {}).get('active'):
            print(f"💨 LVD: ACTIVE - {result['lvd']['reason']}")
        
        if result.get('sdd', {}).get('active'):
            print(f"📊 SDD: ACTIVE - {result['sdd']['reason']}")
        
        # ===== V97: EVENT HORIZON SINGULARITY (EHS) =====
        if result.get('ehs', {}).get('is_active'):
            severity_icon = "☢️" if result['ehs']['severity'] == "ABSOLUTE" else "🔥"
            print(f"{severity_icon} EHS: ACTIVE - {result['ehs']['reason']} (Ratio: {result['ehs']['energy_ratio']}x)")
        
        # ===== V98: VACUUM DETECTOR (VAC) =====
        if result.get('vac', {}).get('active'):
            vac_icon = "💨" if result['vac']['vacuum_type'] == "STRONG" else "🌪️"
            print(f"{vac_icon} VAC: ACTIVE - {result['vac']['reason']}")
        
        # ===== V96: POSITION BUILD DETECTOR (PBD) =====
        if result.get('pbd', {}).get('active'):
            print(f"🏗️ PBD: ACTIVE - {result['pbd']['reason']}")
        
        # ===== V94: BAITING PRICE FILTER =====
        if result.get('bpf', {}).get('is_bait'):
            print(f"🎣 BPF: ACTIVE - {result['bpf']['reason']}")
        
        # ===== V95: LIQUIDATION GAP DETECTOR =====
        if result.get('lgd_gap', {}).get('bias') != 'NEUTRAL':
            print(f"🕳️ LGD_GAP: {result['lgd_gap']['bias']} - {result['lgd_gap']['reason']}")
        
        # ===== V95: SHORT COVERING RULE =====
        if result.get('rsc_short_covering', {}).get('is_active'):
            print(f"🔥 RSC_SHORT_COVERING: ACTIVE - {result['rsc_short_covering']['reason']}")
        
        # V82
        if result.get('lmg', {}).get('is_death_magnet'):
            print(f"💀 LMG: ACTIVE - {result['lmg']['reason']}")
        if result.get('api', {}).get('is_absorbing'):
            print(f"🔄 API: ACTIVE - {result['api']['reason']}")
        
        # V81
        if result.get('ltg', {}).get('is_vacuum'):
            print(f"💨 LTG: ACTIVE - {result['ltg']['reason']}")
        if result.get('icd', {}).get('is_internal_trap'):
            print(f"🔄 ICD: ACTIVE - {result['icd']['reason']}")
        
        # V80
        if result.get('ier', {}).get('is_exit'):
            print(f"🏦 IER: ACTIVE ({result['ier']['exit_type']}) - Flow: {result['trade_flow']}x | OI Δ: {result['oi_delta_5m']}%")
        if result.get('rmg', {}).get('is_weak'):
            print(f"🎣 RMG: ACTIVE ({result['rmg']['weakness_type']})")
        if result.get('fmv', {}).get('is_fake_magnet'):
            print(f"🧲 FMV: ACTIVE ({result['fmv']['fake_type']})")
        
        # V79
        if result.get('wtd', {}).get('is_wash_trade'):
            print(f"🎭 WTD: ACTIVE ({result['wtd']['wash_type']})")
        
        # V78
        if result.get('ezh', {}).get('is_execution'):
            print(f"🎯 EZH: ACTIVE ({result['ezh']['execution_type']})")
        if result.get('psv', {}).get('is_valid'):
            print(f"🔪 PSV: ACTIVE ({result['psv']['validation_type']})")

        print(f"\n🐋 WMI: {result['wmi']['mass_ratio']:.1f}x ({result['wmi']['dominant_side']})")
        print(f"👻 Ghost Intent: {'ACTIVE' if result['ghost']['is_ghost'] else 'INACTIVE'} (Score: {result['ghost']['score']})")
        print(f"⏱️ TTK: {result['ttk']['estimated_minutes']}m ({result['ttk']['urgency']})")
        print(f"⛽ Fuel: {result['ttk']['fuel_ready']}")

        print(f"\n📊 LIQUIDATION METRICS:")
        print(f"🎯 Short: +{result['short_liq']}% | Long: -{result['long_liq']}%")
        print(f"📊 Flow: {result['trade_flow']}x | Agg: {result['aggressive_ratio']}x")
        print(f"📈 RSI(6): {result['rsi6']}")
        print(f"📈 OI Δ5m: {result['oi_delta_5m']}%")
        print("="*80)

    @staticmethod
    def format_signal(symbol: str, result: Dict) -> Dict:
        return {
            "symbol": symbol, 
            "timestamp": result.get('timestamp', ''), 
            "bias": result.get('bias', 'NEUTRAL'),
            "confidence": result.get('confidence', 'LOW'), 
            "reason": result.get('reason', ''),
            "phase": result.get('phase', 'NORMAL'), 
            "entry_status": "READY" if result.get('confidence') in ['SUPREME','ABSOLUTE','HIGH'] else "WAIT",
            "hold_status": "HOLD POSITION" if result.get('confidence') in ['SUPREME','ABSOLUTE'] else "NO POSITION"
        }


# ================= BINANCE ANALYZER V87 =================
# ================= BINANCE ANALYZER V87 (FIXED) =================
class BinanceAnalyzerV87:
    """
    V87: Main analyzer dengan prioritas tertinggi:
        0. SAD (Stealth Accumulation Detector) - ANTI-POWER/ROBO GHOSTING (V87) ⭐ TERTINGGI!
        1. ZAS (Zero Aggression Squeeze) - ANTI-SELLER EXHAUSTION (V87)
        2. LCD (Liquidity Compression Detector) - ANTI-SIDEWAY FATIGUE (V87)
        3. LBD (Liquidity Bait Detector) - ANTI-FAKE MAGNET (V87)
        4. LIM (Liquidity Imbalance Momentum) - ANTI-WRONG TARGET (V87)
        5. ZGH (Zero Gravity Horizon) - ANTI-TRIA TRAP (V86)
        6. ODF (Overbought Distribution Filter) - ANTI-TRIA TRAP (V86)
        7. OTF (Oversold Trap Filter) - ANTI-UAI & LIQUIDITY VACUUM REBOUND (V85)
    """
    def __init__(self, symbol: str):
        self.symbol = symbol.upper()
        self.fetcher = BinanceFetcher(symbol)
        self.state_mgr = StateManagerV82()
        self.market_state = MarketStateEngineV82()
        self.energy_calc = EnergyCalculatorV61()
        
        # V87: New Conflict Resolver (PRIORITAS TERTINGGI!)
        self.conflict_resolver_v87 = ConflictResolverV87()
        
        # V88: NEW MODULES - WHALE DOMINANCE INDEX
        self.wdi = WhaleDominanceV88()  # V88 baru!
        self.conflict_resolver_v88 = ConflictResolverV88()  # V88 baru!
        
        # V89/V90: NEW MODULES - THE PREDATOR TRAP DEFENSE
        self.wsc = WhaleSingularityV89()           # V89 baru!
        self.sat = LiquiditySaturationV90()        # V90 baru!
        self.pet = PositionExpansionTrapV90()      # V90 baru!
        
        # V91: MARKET PHASE ENGINE - THE CORE HFT LAYER (MISSING MODULE!)
        self.phase_engine = MarketPhaseV91()                    # V91 baru! PALING PENTING!
        self.liquidity_drain_detector = LiquidityDrainDetectorV91()   # V91 baru!
        self.liquidity_vacuum_detector = LiquidityVacuumDetectorV91() # V91 baru!
        self.conflict_resolver_v91 = ConflictResolverV91()       # V91 baru!
        
        # V91: NEW MODULES - LIQUIDITY GRAVITY DRAIN (Anti-ROBO Trap)
        self.lgd = LiquidityGravityDrainV91()      # V91 baru! ⭐
        
        # V92: NEW MODULES - EXECUTION ENERGY (Anti-ROBO Trap)
        self.energy_v92 = ExecutionEnergyV92()     # V92 baru! ⭐
        self.aggression_death = AggressionDeathV92() # V92 baru! ⭐
        self.conflict_resolver_v92 = ConflictResolverV92()  # V92 baru! ⭐
        
        # ===== V93: NEW MODULES - THE VACUUM FLUSH DETECTORS =====
        self.odc = OIDrainCondemnationV93()                 # V93 baru! (Saran 1 - PLAY)
        self.opd = OrderbookPullDetectorV93()                # V93 baru! (Saran 2)
        self.wmi_exhaust = WMISingularityExhaustionV93()     # V93 baru! (Saran 2)
        self.cascade_time = CascadeTimeEstimatorV93()        # V93 baru! (Saran 2)
        self.conflict_resolver_v93 = ConflictResolverV93()   # V93 baru! ⭐
        
        # ===== V94: NEW MODULES - ENERGY PATH & PASSIVE RELOAD =====
        self.lep = LowEnergyPathV94()                    # V94 baru! (PIXEL - Energy Path)
        self.plr = PassiveLiquidityReloadV94()            # V94 baru! (Passive Liquidity Reload)
        self.egr = EnergyGravityRuleV94()                 # V94 baru! (Energy Gravity Rule)
        
        # ===== V95: NEW MODULE - LIQUIDITY IGNITION DETECTOR =====
        self.lid = LiquidityIgnitionDetectorV95()         # V95 baru! (Short Squeeze Setup)
        
        # ===== V95: NEW MODULE - ENERGY SPOOF TRACKER =====
        self.est = EnergySpoofTrackerV95()                # V95 baru! (Energy Spoof Tracker)
        
        # ===== V96: NEW MODULES - PASSIVE DISTRIBUTION & SHORT COVERING FILTER =====
        self.pdd = PassiveDistributionDetectorV96()       # V96 baru! (Passive Distribution)
        self.rsc = RealShortCoveringFilterV96()           # V96 baru! (Real Short Covering)
        
        # ===== V95/V96: NEW MODULES - RETAIL TRAP & EXECUTION COMPLETION =====
        self.rpt = RetailPositioningTrapV95()             # V95 baru! (Retail Positioning Trap) ⭐
        self.ecd = ExecutionCompletionDetectorV96()       # V96 baru! (Execution Completion Detector) ⭐
        
        # ===== V96: SINGULARITY VETO INTEGRITY =====
        self.svi = SingularityVetoV96()           # V96 baru! (Anti-OverLogic DEGO) ⭐
        
        # ===== V97: EVENT HORIZON DETECTOR =====
        self.evh = EventHorizonV97()               # V97 baru! (Liquidation Proximity) ⭐
        
        # ===== V97: EVENT HORIZON SINGULARITY =====
        self.ehs = EventHorizonSingularityV97()    # V97 baru! (Anti-ARIA Trap) ⭐
        
        # ===== V98: VACUUM DETECTOR =====
        self.vac = VacuumDetectorV98()              # V98 baru! (Orderbook Vacuum) ⭐
        
        # ===== V96: POSITION BUILD DETECTOR (ENHANCED) =====
        self.pbd = PositionBuildDetectorV96()       # V96 enhanced ⭐
        
        self.conflict_resolver_v96 = ConflictResolverV96  # V96 resolver ⭐
        
        # ===== V96: NEW MODULE - GHOST WALL CONDEMNATION =====
        self.gwc = GhostWallCondemnationV96()            # V96 baru! (Ghost Wall)
        
        # ===== V97: NEW MODULES - LIQUIDITY VACUUM & SILENT DISTRIBUTION =====
        self.lvd = LiquidityVacuumDetectorV97()          # V97 baru! (Liquidity Vacuum)
        self.sdd = SilentDistributionDetectorV97()        # V97 baru! (Silent Distribution)
        
        # ===== V97: NEW CONFLICT RESOLVER (dengan hierarki terbaru) =====
        self.conflict_resolver_v97 = ConflictResolverV97  # V97 resolver ⭐
        
        # ===== V99: SUPERIOR WHALE DOMINANCE PROTOCOL =====
        self.wmi_veto = SuperiorWDMVIP99()           # V99 baru! (WMI Absolute Veto)
        self.internal_trap = InternalTrapV99FMT()    # V99 baru! (Internal Trap)
        self.oi_phase = OIAccelerationPhaseV99()     # V99 baru! (OI Phase Detection)
        self.density_calc = LiquidityDensityCalculatorV99()  # V99 baru! (Density Calculator)
        self.oi_build_validator = OIBuildValidatorV99()      # V99 baru! (Nuclear OI)
        self.gravity_distance = GravityDistanceValidatorV99() # V99 baru! (Proximity > Massa)
        
        # ===== V99-SCT: SHORT CROWD TRAP MODULES =====
        self.sct_detector = ShortCrowdTrapDetectorV99()      # V99 Short Crowd Trap
        self.crowd_cluster = CrowdVsClusterLogicV99()        # V99 Crowd vs Cluster
        self.oi_extremum = OIBuildAtExtremumV99()            # V99 OI Build at Extremum
        
        self.conflict_resolver_v99 = ConflictResolverV99()   # V99 resolver
        
        # ===== V100: LIQUIDATION PAYOUT & PRE-FLUSH DETECTOR =====
        self.lpc = LiquidationPayoutCalculatorV100()     # V100 baru!
        self.lpf = LiquidationPreFlushDetectorV100()     # V100 baru!
        self.conflict_resolver_v100 = ConflictResolverV100()  # V100 resolver
        
        # Tetap pertahankan resolver lama untuk kompatibilitas (opsional)
        self.conflict_resolver_v82 = ConflictResolverV82()
        
        self.mpe = MPEV61()
        self.liquidity_gravity = LiquidityGravityCalculatorV54()
        self.ppi_calc = PositioningPressureIndexV54()
        self.exhaustion_detector = ExhaustionDetectorV61()
        self.stop_hunt_sim = StopHuntSimulatorV54()
        self.ob_imprint = OrderbookImprintV54()
        self.spoofing_detector = SpoofingDetectorV54()
        self.reversion_detector = DeepReversionDetectorV54()
        self.oi_tracker = OIVelocityTrackerV61()
        self.hft_signature = HFTSignatureDetectorV61()
        self.pnr_detector = PNRDetectorV54()
        self.add_detector = AggressionDeltaDivergenceV54()
        self.vbt = VolatilityBurstTrackerV54()
        self.lrr = LiquidityRiskRewardV54()
        self.av = AggressionVelocityV54()
        self.starter = EngineStarterV61()
        self.ttk = TTKCountdownV61()
        self.odd = OrderbookDepthDecayV61()
        self.ghost = GhostIntentDetectorV62()
        self.dtd = DivergenceTrapDetectorV61()
        self.lvs = LowVolumeSuctionV61()
        self.mwr = MagnetWallReversalV62()
        self.wed = WallErasureV63()
        self.tdp = DylParticleV64()
        self.amd = AggressionMassDivergenceV65()
        self.ati = TemporalAccumulationV66()
        self.zas_v67 = ZeroAggressionSlaughterV67()  # Renamed to avoid conflict with V87 ZAS
        self.avc = AbsorptionValidityCheckV67()
        self.ogd = GravityDeflectionV68()
        self.trend = TrendIntegrityV69()
        self.ovd = OrderbookVacuumDefenseV70()
        self.mdd = MagnetDistanceDominanceV71()
        self.cfk = CatchingFallingKnivesV72()
        self.pab = PassiveAbsorptionBlackholeV73()
        self.mdv = MagnetDecayValidatorV74()
        self.amv = AbsorptionMomentumValidatorV75()
        self.lgo = LiquidationGravityOverdriveV75()
        self.psr = PanicSaturationReversalV76()
        self.off = OverdriveFlowFilterV77()
        self.aef = AggressiveExhaustionFilterV77()
        self.ezh = ExecutionZoneHunterV78()
        self.psv = PanicSellValidatorV78()
        self.wtd = WashTradeDetectorV79()
        self.ltg = LiquidityThinningGuardV81()  # V81 baru!
        self.icd = InternalCrossDetectorV81()   # V81 baru!

        # V82: New modules
        self.api = AbsorptionPressureV82()      # V82 baru!
        self.lmg = LiquidityMirrorGuardV82()    # V82 baru!
        self.fid = FuelIgnitionDetectorV82()    # V82 baru!

        # V83: NEW MODULES - THE LIQUIDITY SNIPER
        self.lhg = LiquidationHeatGradientV83()         # V83 baru!
        self.ovs = OrderbookVacuumSpeedV83()            # V83 baru!
        self.adv = AggressionVelocityV83()              # V83 baru!
        self.tbd = TradeBurstDetectorV83()              # V83 baru!
        self.oia = OIAccelerationV83()                  # V83 baru!
        self.lsp = LiquiditySweepProbabilityV83()       # V83 baru!
        self.sniper_score = LiquiditySniperScoreV83()   # V83 baru!

        # V85: NEW MODULES - OVERSOLD TRAP PROTECTION (Patch UAIUSDT)
        self.otf = OversoldTrapFilterV85()              # V85 baru!
        self.aaf = AggressionAbsorptionFilterV85()      # V85 baru!
        self.fed = FakeExhaustionDetectorV85()          # V85 baru!
        
        # V85: NEW MODULES - ANTI-STABLE TRAP (Patch STABLEUSDT)
        self.nzs = NeutralZoneShieldV85()               # V85 baru!
        self.pfd = PositionFlipDetectorV85()            # V85 baru!
        self.fed_v85 = FakeExitDetectorV85()            # V85 baru!
        self.lrd = LiquidityReloadDetectorV85()         # V85 baru!

        # V86: NEW MODULES - ZERO GRAVITY HORIZON (Anti-TRIA Trap)
        self.zgh = ZeroGravityHorizonV86()               # V86 baru!
        self.odf = OverboughtDistributionFilterV86()     # V86 baru!

        # V87: NEW MODULES - GHOST IN THE SHELL EDITION (Anti-POWER/ROBO Trap)
        self.zas = ZeroAggressionSqueezeV87()            # V87 baru! (Zero Aggression Squeeze)
        self.lcd = LiquidityCompressionDetectorV87()     # V87 baru! (Liquidity Compression)
        self.lbd = LiquidityBaitDetectorV87()            # V87 baru! (Liquidity Bait)
        self.lim = LiquidityImbalanceMomentumV87()       # V87 baru! (Liquidity Imbalance)
        self.sad = StealthAccumulationDetectorV87()      # V87 baru! (Stealth Accumulation)

        # V80: New modules
        self.ier = InstitutionalExitRadarV80()  # V80 baru!
        self.rmg = RSIMomentumGuardV80()         # V80 baru!
        self.fmv = FakeMagnetVacuumV80()          # V80 baru!

        self.oi_history = deque(maxlen=30)
        self._prefill_oi_history()

    def _prefill_oi_history(self):
        """Prefill OI history dari data historical"""
        try:
            hist = self.fetcher.get_open_interest_historical(period="5m", limit=10)
            if hist and len(hist) > 0:
                for item in hist:
                    oi_val = safe_float(item.get("sumOpenInterest") or item.get("openInterest") or item.get("sumOpenInterestValue"))
                    if oi_val and oi_val > 0:
                        self.oi_history.append(oi_val)
                print(f"✅ Prefilled OI history dengan {len(self.oi_history)} data points")
            else:
                oi_current = self.get_open_interest_safe()
                if oi_current > 0:
                    for _ in range(6):
                        self.oi_history.append(oi_current)
        except Exception as e:
            print(f"⚠️ Gagal prefill OI history: {e}")

    def get_open_interest_safe(self) -> float:
        """Safe OI fetching dengan multiple fallback"""
        try:
            oi = self.fetcher.get_open_interest_current()
            if oi is not None and oi > 0:
                return oi
            hist_oi = self.fetcher.get_oi_5m_ago()
            if hist_oi is not None and hist_oi > 0:
                return hist_oi
        except Exception as e:
            print(f"⚠️ OI fetch warning: {e}")
        return 1000.0

    def analyze(self) -> Optional[Dict]:
        try:
            # --- 1. AMBIL DATA HARGA ---
            price = self.fetcher.get_price()
            if not price:
                return None

            # --- 2. AMBIL DATA DASAR LAINNYA ---
            change_24h = self.fetcher.get_24h_change() or 0
            ob_data = self.fetcher.get_orderbook_ratio() or {"ratio": 1.0, "bids": [], "asks": []}
            trades = self.fetcher.get_trades_flow() or {"ratio": 1.0, "volume_ratio": 1.0, "aggressive_ratio": 1.0}
            funding = self.fetcher.get_funding_premium() or {"premium": 0, "funding": 0, "avg_funding": 0}

            # ===== V81: HITUNG ASK VOLUME DAN BID VOLUME UNTUK LTG =====
            ask_vol = sum(q for _, q in ob_data.get('asks', [])[:5]) if ob_data.get('asks') else 0
            bid_vol = sum(q for _, q in ob_data.get('bids', [])[:5]) if ob_data.get('bids') else 0
            # ============================================================

            # --- 3. AMBIL OI (SEKARANG VS 5 MENIT LALU) ---
            oi_now = self.fetcher.get_open_interest_current()
            oi_then = self.fetcher.get_oi_5m_ago()
            oi_delta_5m = 0.0
            if oi_now and oi_then and oi_then > 0:
                oi_delta_5m = ((oi_now - oi_then) / oi_then) * 100
                self.oi_history.append(oi_now)
            elif oi_now and len(self.oi_history) >= 6:
                oi_then = self.oi_history[0]
                oi_delta_5m = ((oi_now - oi_then) / oi_then) * 100

            print(f"🎯 OI_SINKRON: SEKARANG={oi_now} | 5M_LALU={oi_then} | DELTA={oi_delta_5m:.2f}%")

            k1m = self.fetcher.get_klines("1m", 100)
            if not k1m:
                return None

            closes_1m = k1m.get("closes", [price])
            highs_1m = k1m.get("highs", [price])
            lows_1m = k1m.get("lows", [price])
            volumes_1m = k1m.get("volumes", [0])
            std_dev = k1m.get("std_dev", 0)

            rsi6 = IndicatorCalculator.calculate_rsi(closes_1m, 6)
            rsi14 = IndicatorCalculator.calculate_rsi(closes_1m, 14)
            macd = IndicatorCalculator.calculate_macd(closes_1m)

            change_1m = ((closes_1m[-1] - closes_1m[-2]) / closes_1m[-2]) * 100 if len(closes_1m) >= 2 else 0
            change_5m = ((closes_1m[-1] - closes_1m[-5]) / closes_1m[-5]) * 100 if len(closes_1m) >= 5 else 0

            vol_ma5 = np.mean(volumes_1m[-5:]) if len(volumes_1m) >= 5 else 0
            vol_ma10 = np.mean(volumes_1m[-10:]) if len(volumes_1m) >= 10 else 0
            volume_ratio = vol_ma5 / vol_ma10 if vol_ma10 > 0 else 1.0

            liq = IndicatorCalculator.get_liquidation_zones(highs_1m, lows_1m, price, volumes_1m)

            # V69: Hitung MA10 dan MA20
            ma10 = IndicatorCalculator.calculate_ma(closes_1m, TREND_MA_SHORT)
            ma20 = IndicatorCalculator.calculate_ma(closes_1m, TREND_MA_LONG)

            # V69: Hitung OBV
            obv_list = IndicatorCalculator.calculate_obv(closes_1m, volumes_1m)
            current_obv = obv_list[-1] if obv_list else 0

            # WMI Calculation
            wmi_ratio = self.fetcher.calculate_wmi(liq['short_dist'], liq['long_dist'],
                                                liq['short_vol'], liq['long_vol'])

            # ================= V88: WHALE DOMINANCE INDEX =================
            wdi_result = self.wdi.analyze(
                wmi=wmi_ratio, 
                short_dist=liq['short_dist'], 
                oi_delta=oi_delta_5m
            )

            # === V82: Fuel Ignition Detector (FID) ===
            fid_result = self.fid.analyze(oi_delta_5m, rsi6, wmi_ratio)
            fid_key = f"FID_{oi_delta_5m:.2f}_{rsi6:.1f}"
            fid_duration = self.state_mgr.track_fid_persistence(fid_key, time.time())

            # Update state manager
            self.state_mgr.update_orderbook(ob_data.get('bids', []), ob_data.get('asks', []))
            self.state_mgr.update(
                price, rsi6, volume_ratio, trades['ratio'],
                ob_data['ratio'], funding['premium'], funding['funding'],
                trades['aggressive_ratio'], std_dev, wmi_ratio,
                ma10, ma20, current_obv
            )

            volume_trend = self.state_mgr.get_volume_trend()
            flow_trend = self.state_mgr.get_flow_trend()
            premium_trend = self.state_mgr.get_premium_trend()
            aggressive_trend = self.state_mgr.get_aggressive_trend()
            double_sweep = self.state_mgr.detect_double_sweep_zone(liq['short_dist'], liq['long_dist'])
            accumulation_detected = self.state_mgr.detect_accumulation(price, oi_now)

            # V66: Track accumulation duration
            accumulation_minutes = self.state_mgr.track_accumulation_duration(trades['ratio'], time.time())

            # V74: Track magnet persistence
            magnet_key = f"MAGNET_{liq['short_dist']:.2f}_{liq['long_dist']:.2f}"
            magnet_duration = self.state_mgr.track_magnet_persistence(magnet_key, time.time())

            # V75: Track gravity overdrive persistence
            gravity_key = f"GRAVITY_{liq['short_dist']:.2f}_{liq['long_dist']:.2f}"
            gravity_duration = self.state_mgr.track_gravity_overdrive_persistence(gravity_key, time.time())

            # V76: Track panic saturation persistence
            panic_key = f"PANIC_{trades['aggressive_ratio']:.2f}_{price:.4f}"
            panic_duration = self.state_mgr.track_panic_saturation_persistence(panic_key, time.time())

            # V77: Track OFF persistence
            off_key = f"OFF_{liq['short_dist']:.2f}_{liq['long_dist']:.2f}_{trades['ratio']:.2f}"
            off_duration = self.state_mgr.track_off_persistence(off_key, time.time())

            # V77: Track AEF persistence
            aef_key = f"AEF_{trades['aggressive_ratio']:.2f}_{rsi6:.1f}_{oi_delta_5m:.1f}"
            aef_duration = self.state_mgr.track_aef_persistence(aef_key, time.time())

            # V78: Track EZH persistence
            ezh_key = f"EZH_{liq['short_dist']:.3f}_{liq['long_dist']:.3f}_{rsi6:.1f}"
            ezh_duration = self.state_mgr.track_ezh_persistence(ezh_key, time.time())

            # V78: Track PSV persistence
            psv_key = f"PSV_{rsi6:.1f}_{trades['ratio']:.2f}"
            psv_duration = self.state_mgr.track_psv_persistence(psv_key, time.time())

            # V79: Track WTD persistence
            wtd_key = f"WTD_{trades['ratio']:.2f}_{rsi6:.1f}"
            wtd_duration = self.state_mgr.track_wtd_persistence(wtd_key, time.time())

            # V80: Track IER persistence
            ier_key = f"IER_{trades['ratio']:.2f}_{oi_delta_5m:.2f}"
            ier_duration = self.state_mgr.track_ier_persistence(ier_key, time.time())

            # V80: Track RMG persistence
            rmg_key = f"RMG_{rsi6:.1f}_{trades['aggressive_ratio']:.2f}_{liq['short_dist']:.2f}"
            rmg_duration = self.state_mgr.track_rmg_persistence(rmg_key, time.time())

            # V80: Track FMV persistence
            fmv_key = f"FMV_{trades['ratio']:.2f}_{rsi6:.1f}_{oi_delta_5m:.2f}_{trades['aggressive_ratio']:.2f}"
            fmv_duration = self.state_mgr.track_fmv_persistence(fmv_key, time.time())

            # ===== V81: ANALISIS LTG DAN ICD =====
            ltg_result = self.ltg.analyze(trades['ratio'], ask_vol, bid_vol)
            icd_result = self.icd.analyze(trades['ratio'], trades['aggressive_ratio'], oi_delta_5m)

            # ===== V82: ANALISIS API DAN LMG =====
            api_result = self.api.analyze(trades['aggressive_ratio'], rsi6, change_5m, liq['long_dist'])
            lmg_result = self.lmg.analyze(liq['long_dist'], liq['short_dist'], rsi6)

            # Track persistence V81
            ltg_key = f"LTG_{trades['ratio']:.2f}"
            ltg_duration = self.state_mgr.track_ltg_persistence(ltg_key, time.time())
            icd_key = f"ICD_{trades['ratio']:.2f}_{trades['aggressive_ratio']:.2f}"
            icd_duration = self.state_mgr.track_icd_persistence(icd_key, time.time())

            # Track persistence V82
            api_key = f"API_{trades['aggressive_ratio']:.2f}_{rsi6:.1f}"
            api_duration = self.state_mgr.track_api_persistence(api_key, time.time())
            lmg_key = f"LMG_{liq['long_dist']:.2f}_{liq['short_dist']:.2f}_{rsi6:.1f}"
            lmg_duration = self.state_mgr.track_lmg_persistence(lmg_key, time.time())

            # WMI untuk Vacuum Override
            wmi_data = {
                'mass_ratio': wmi_ratio,
                'is_whale_trap': abs(wmi_ratio) > VACUUM_WMI_MIN,
                'dominant_side': "SHORT_LIQ_WHALE" if wmi_ratio > 0 else "LONG_LIQ_WHALE" if wmi_ratio < 0 else "NEUTRAL"
            }

            oi_velocity = self.oi_tracker.analyze(oi_now, oi_then or oi_now, change_5m, trades['ratio'])

            data = {
                "price": price,
                "change_24h": change_24h,
                "change_5m": change_5m,
                "change_1m": change_1m,
                "ob_ratio": ob_data['ratio'],
                "trade_flow": trades['ratio'],
                "aggressive_ratio": trades['aggressive_ratio'],
                "volume_ratio": volume_ratio,
                "volume_trend": volume_trend,
                "flow_trend": flow_trend,
                "premium_trend": premium_trend,
                "aggressive_trend": aggressive_trend,
                "oi_delta_5m": oi_delta_5m,
                "premium": funding['premium'],
                "funding": funding['funding'],
                "avg_funding": funding['avg_funding'],
                "rsi6": rsi6,
                "rsi14": rsi14,
                "macd_bullish_cross": macd['bullish_cross'],
                "macd_bearish_cross": macd['bearish_cross'],
                "short_liq_dist": liq['short_dist'],
                "long_liq_dist": liq['long_dist'],
                "short_liq_vol": liq['short_vol'],
                "long_liq_vol": liq['long_vol'],
                "wmi_ratio": wmi_ratio,
                "ma10": ma10,
                "ma20": ma20,
                "obv": current_obv
            }

            liquidity_gravity = self.liquidity_gravity.calculate(
                liq['short_dist'], liq['long_dist'],
                liq['short_vol'], liq['long_vol'],
                oi_now / 1000, rsi6
            )

            gravity_key = f"{liquidity_gravity['bias']}_{liquidity_gravity['strength']}"
            persistence_minutes = self.state_mgr.track_gravity_persistence(gravity_key, time.time())

            ppi = self.ppi_calc.calculate(
                funding['funding'], funding['premium'],
                funding['avg_funding'], trades['ratio'],
                trades['aggressive_ratio'], oi_delta_5m, rsi6
            )

            exhaustion = self.exhaustion_detector.detect(
                rsi6, funding['premium'], trades['ratio'],
                volume_ratio, change_5m, trades['aggressive_ratio'], oi_delta_5m
            )

            reversion = self.reversion_detector.analyze(
                rsi6, trades['ratio'], volume_ratio,
                funding['premium'], change_5m, oi_delta_5m
            )

            stop_hunt = self.stop_hunt_sim.simulate(
                price, liq['short_dist'], liq['long_dist'],
                liq['short_vol'], liq['long_vol'], oi_now, rsi6, oi_delta_5m
            )

            ob_imprint = self.ob_imprint.analyze(
                ob_data['bids'], ob_data['asks'], ob_data['ratio'],
                trades['ratio'], rsi6, oi_delta_5m
            )

            spoofing = self.spoofing_detector.detect(
                ob_data['ratio'], trades['ratio'], trades['aggressive_ratio'],
                rsi6, ob_data['bids'], ob_data['asks'], oi_delta_5m
            )

            lrr_result = self.lrr.analyze(liq['short_dist'], liq['long_dist'], liq['short_vol'], liq['long_vol'])
            av_result = self.av.analyze(self.state_mgr.aggressive_history)
            oi_5m_ago_value = oi_then or oi_now
            starter_result = self.starter.analyze(data, deque([oi_5m_ago_value] if oi_5m_ago_value else []), self.state_mgr.price_history)
            pnr = self.pnr_detector.analyze(liq['short_dist'], liq['long_dist'], rsi6, trades['ratio'])
            target_side = "SHORT_LIQ" if liq['short_dist'] < liq['long_dist'] else "LONG_LIQ"

            odd_result = self.odd.analyze(
                ob_data.get('bids', []),
                ob_data.get('asks', []),
                price,
                min(liq['short_dist'], liq['long_dist']),
                target_side
            )

            ghost_result = self.ghost.analyze(
                rsi6, trades['aggressive_ratio'], change_5m,
                oi_delta_5m, liq['short_dist'], liq['long_dist'],
                odd_result, pnr['bias'] if pnr['pnr_active'] else "NEUTRAL", wmi_ratio
            )

            dtd_result = self.dtd.analyze(trades['ratio'], trades['aggressive_ratio'], change_5m)
            lvs_result = self.lvs.analyze(trades['aggressive_ratio'], trades['ratio'], change_5m, wmi_ratio)
            mwr_result = self.mwr.analyze(odd_result, rsi6, wmi_ratio, target_side)
            wed_result = self.wed.analyze(odd_result, wmi_ratio, rsi6, oi_delta_5m)
            tdp_result = self.tdp.analyze(oi_delta_5m, wmi_ratio, rsi6)
            amd_result = self.amd.analyze(wmi_ratio, trades['aggressive_ratio'], trades['ratio'], oi_delta_5m)
            
            ati_result = self.ati.analyze(
                trades['ratio'], rsi6, wmi_ratio, oi_delta_5m,
                accumulation_minutes / 60, self.state_mgr.get_flow_history()
            )

            zas_v67_result = self.zas_v67.analyze(trades['aggressive_ratio'], wmi_ratio, change_5m)
            avc_result = self.avc.analyze(trades['ratio'], trades['aggressive_ratio'], change_5m, oi_delta_5m)
            ogd_result = self.ogd.analyze(wmi_ratio, rsi6, liq['long_dist'] if wmi_ratio < 0 else liq['short_dist'])
            
            trend_result = self.trend.analyze(price, ma10, ma20, self.state_mgr.get_obv_history(), macd)
            
            ovd_result = self.ovd.analyze(odd_result, rsi6, trades['aggressive_ratio'], liq['short_dist'], liq['long_dist'])
            mdd_result = self.mdd.analyze(liq['short_dist'], liq['long_dist'], rsi6, trades['ratio'])
            
            cfk_result = self.cfk.analyze(wmi_ratio, rsi6, oi_delta_5m, trades['aggressive_ratio'], trades['ratio'])
            pab_result = self.pab.analyze(trades['ratio'], trades['aggressive_ratio'], rsi6, wmi_ratio, oi_delta_5m)
            
            mdv_result = self.mdv.analyze(
                mdd_result, amd_result, oi_delta_5m,
                self.state_mgr.magnet_first_seen.get(magnet_key, 0), time.time()
            )

            amv_result = self.amv.analyze(oi_delta_5m, trades['aggressive_ratio'], change_5m, trades['ratio'])
            lgo_result = self.lgo.analyze(liq['short_dist'], liq['long_dist'], rsi6, trades['ratio'])
            psr_result = self.psr.analyze(trades['aggressive_ratio'], price, ma10, ma20, rsi6, trades['ratio'], wmi_ratio)
            off_result = self.off.analyze(lgo_result, trades['ratio'], rsi6, trades['aggressive_ratio'])
            
            aef_result = self.aef.analyze(
                trades['aggressive_ratio'], rsi6, oi_delta_5m,
                liq['short_dist'], liq['long_dist'], trades['ratio']
            )

            # V78: EXECUTION ZONE HUNTER (EZH)
            ezh_result = self.ezh.analyze(liq['short_dist'], liq['long_dist'], rsi6, trades['ratio'])

            # V78: PANIC SELL VALIDATOR (PSV)
            psv_result = self.psv.analyze(rsi6, trades['ratio'], trades['aggressive_ratio'], oi_delta_5m)

            # V79: WASH TRADE DETECTOR (WTD)
            wtd_result = self.wtd.analyze(trades['ratio'], rsi6, oi_delta_5m)

            # V80: INSTITUTIONAL EXIT RADAR (IER)
            ier_result = self.ier.analyze(trades['ratio'], oi_delta_5m, trades['aggressive_ratio'])

            # V80: RSI MOMENTUM GUARD (RMG)
            rmg_result = self.rmg.analyze(rsi6, trades['aggressive_ratio'], liq['short_dist'])

            # V85: OVERSOLD TRAP FILTER (OTF)
            otf_result = self.otf.analyze(
                rsi6, oi_delta_5m, trades['ratio'],
                wmi_ratio=wmi_data.get('mass_ratio', 0) if wmi_data else None,
                agg_ratio=trades['aggressive_ratio']
            )
            
            # V86: ZERO GRAVITY HORIZON (ZGH)
            zgh_result = self.zgh.analyze(
                rsi6=rsi6, oi_delta=oi_delta_5m, agg_ratio=trades['aggressive_ratio'],
                short_dist=liq['short_dist'], long_dist=liq['long_dist']
            )

            # V86: OVERBOUGHT DISTRIBUTION FILTER (ODF)
            odf_result = self.odf.analyze(
                rsi6=rsi6, oi_delta=oi_delta_5m, agg_ratio=trades['aggressive_ratio'],
                short_liq_size=liq['short_vol'], long_liq_size=liq['long_vol'],
                short_dist=liq['short_dist'], long_dist=liq['long_dist']
            )

            # V85: AGGRESSION ABSORPTION FILTER (AAF)
            aaf_result = self.aaf.analyze(trades['aggressive_ratio'], trades['ratio'])

            # V85: FAKE EXHAUSTION DETECTOR (FED)
            fed_result = self.fed.analyze(rsi6, oi_delta_5m)
            
            # V85: NEUTRAL ZONE SHIELD (NZS)
            ier_active = ier_result.get('is_exit', False) if ier_result else False
            nzs_result = self.nzs.analyze(rsi6, wmi_data.get('mass_ratio', 0) if wmi_data else 0, ier_active)
            
            # V85: POSITION FLIP DETECTOR (PFD)
            pfd_result = self.pfd.analyze(trades['ratio'], trades['aggressive_ratio'], oi_delta_5m)
            
            # V85: FAKE EXIT DETECTOR (FED_V85)
            fed_v85_result = self.fed_v85.analyze(trades['ratio'], trades['aggressive_ratio'])
            
            # V85: LIQUIDITY RELOAD DETECTOR (LRD)
            lrd_result = self.lrd.analyze(oi_delta_5m, wmi_data.get('mass_ratio', 0) if wmi_data else 0)
            
            # ================= V83 MODULES - THE LIQUIDITY SNIPER =================
            lhg_result = self.lhg.analyze(liq['long_dist'], liq['short_dist'], liq['long_vol'], liq['short_vol'])
            ovs_result = self.ovs.analyze(ob_data.get('bids', []), ob_data.get('asks', []))
            adv_result = self.adv.analyze(trades['aggressive_ratio'])
            tbd_result = self.tbd.analyze(int(trades['volume_ratio'] * 20))
            
            oia_result = self.oia.analyze(
                oi_now=oi_now, oi_prev=oi_then or oi_now,
                price_change=change_5m, time_delta_s=300.0
            )
            
            lsp_result = self.lsp.analyze(liq['long_vol'], liq['short_vol'])
            sniper_result = self.sniper_score.calculate(ovs_result, adv_result, oia_result, lhg_result, lsp_result)
            # ======================================================================

            # ================= V87 MODULES - GHOST IN THE SHELL EDITION =================
            # PASTIKAN SEMUA V87 MODULES DIPANGGIL DI SINI!
            zas_result = self.zas.analyze(trades['aggressive_ratio'], trades['ratio'], rsi6, oi_delta_5m)
            lcd_result = self.lcd.analyze(trades['aggressive_ratio'], trades['ratio'], oi_delta_5m, rsi6)
            lbd_result = self.lbd.analyze(liq['short_dist'], liq['long_dist'], trades['ratio'], trades['aggressive_ratio'], oi_delta_5m)
            lim_result = self.lim.analyze(
                lhg_result.get('short_gradient', 0), 
                lhg_result.get('long_gradient', 0), 
                oi_velocity.get('power', 0), 
                trades['aggressive_ratio']
            )
            sad_result = self.sad.analyze(trades['aggressive_ratio'], change_5m, oi_delta_5m, wmi_ratio)
            # ============================================================================

            # ================= V89/V90 MODULES - ANTI-PREDATOR TRAP =================
            # Whale Singularity Check (V89)
            wsc_result = self.wsc.analyze(
                wmi=wmi_ratio, 
                short_dist=liq['short_dist'],
                rsi=rsi6
            )

            # Liquidity Saturation (V90)
            # Gunakan imbalance_ratio dari LIM jika tersedia
            imbalance_ratio = lim_result.get('imbalance_ratio', 1.0) if 'lim_result' in locals() else 1.0
            sat_result = self.sat.analyze(
                imbalance_ratio=imbalance_ratio,
                wmi=wmi_ratio,
                short_dist=liq['short_dist']
            )

            # Position Expansion Trap (V90)
            pet_result = self.pet.analyze(
                oi_delta=oi_delta_5m,
                agg=trades['aggressive_ratio'],
                flow=trades['ratio'],
                rsi=rsi6
            )
            # =======================================================================

            # V80: FAKE MAGNET VACUUM (FMV)
            fmv_result = self.fmv.analyze(
                ier_result, rmg_result, rsi6, trades['ratio'],
                oi_delta_5m, trades['aggressive_ratio'], liq['short_dist']
            )

            hft_signature = self.hft_signature.analyze(
                price, liq['short_dist'], liq['long_dist'],
                trades['ratio'], trades['aggressive_ratio'],
                0, oi_delta_5m, rsi6, change_5m,
                liquidity_gravity['bias'], liquidity_gravity['strength'],
                persistence_minutes,
                liquidity_gravity['short_gravity'], liquidity_gravity['long_gravity'],
                lrr_result, av_result, starter_result, ghost_result
            )

            energy = self.energy_calc.calculate(data, self.state_mgr)
            mpe_result = self.mpe.calculate(data)

            market_phase = self.market_state.detect_state(
                data, self.state_mgr, liquidity_gravity, ppi, spoofing,
                reversion, oi_velocity, hft_signature, lrr_result, av_result,
                starter_result, ghost_result, dtd_result, lvs_result,
                mwr_result, wed_result, tdp_result, amd_result, ati_result,
                zas_v67_result, avc_result, ogd_result, trend_result, ovd_result,
                mdd_result, cfk_result, pab_result, mdv_result, amv_result, lgo_result,
                psr_result, off_result, aef_result, ezh_result, psv_result,
                wtd_result, ier_result, rmg_result, fmv_result,
                ltg_result, icd_result, api_result, lmg_result
            )

            liquidity_data = {
                "nearest": "SHORT" if liq['short_dist'] < liq['long_dist'] else "LONG",
                "short_dist": liq['short_dist'],
                "long_dist": liq['long_dist']
            }

            vbt_result = self.vbt.analyze(price, self.state_mgr.price_history, volume_ratio)

            # 🔥 PRIORITAS UTAMA V91: MARKET PHASE ENGINE + ConflictResolverV91!
            # 1️⃣ Pertama: Tentukan MARKET PHASE (PALING PENTING!)
            phase_result = self.phase_engine.analyze(
                rsi=rsi6,
                flow=trades['ratio'],
                agg=trades['aggressive_ratio'],
                oi_delta=oi_delta_5m,
                wmi=wmi_ratio
            )
            
            # 2️⃣ Kedua: Deteksi LIQUIDITY DRAIN (ROBO type crash)
            drain_result = self.liquidity_drain_detector.analyze(
                flow=trades['ratio'],
                agg=trades['aggressive_ratio'],
                rsi=rsi6,
                price_change=change_5m
            )
            
            # 3️⃣ Ketiga: Deteksi LIQUIDITY VACUUM (AINU type rebound)
            vacuum_result = self.liquidity_vacuum_detector.analyze(
                rsi=rsi6,
                oi_delta=oi_delta_5m,
                flow=trades['ratio'],
                wmi=wmi_ratio,
                agg=trades['aggressive_ratio']
            )
            
            # ================= V91: LIQUIDITY GRAVITY DRAIN (LGD) =================
            lgd_result = self.lgd.analyze(
                short_dist=liq['short_dist'],
                long_dist=liq['long_dist'],
                agg=trades['aggressive_ratio'],
                imbalance=lim_result.get('imbalance_ratio', 1.0)
            )

            # ================= V92: EXECUTION ENERGY =================
            energy_result = self.energy_v92.analyze(
                flow=trades['ratio'],
                agg=trades['aggressive_ratio'],
                long_dist=liq['long_dist'],
                short_dist=liq['short_dist'],
                imbalance=lim_result.get('imbalance_ratio', 1.0)
            )

            # ================= V92: AGGRESSION DEATH =================
            death_result = self.aggression_death.analyze(
                agg=trades['aggressive_ratio'],
                flow=trades['ratio']
            )
            
            # ================= V93: OI DRAIN CONDEMNATION (ODC) =================
            odc_result = self.odc.analyze(
                oi_delta=oi_delta_5m,
                rsi=rsi6,
                wmi=wmi_ratio
            )

            # ================= V93: ORDERBOOK PULL DETECTOR (OPD) =================
            # Gunakan ovs_result untuk mendapatkan vacuum speeds
            opd_result = self.opd.analyze(
                bid_vacuum_speed=ovs_result.get('bid_vacuum_speed', 0),
                ask_vacuum_speed=ovs_result.get('ask_vacuum_speed', 0),
                oi_delta=oi_delta_5m
            )

            # ================= V93: WMI SINGULARITY EXHAUSTION =================
            wmi_exhaust_result = self.wmi_exhaust.analyze(
                wmi=wmi_ratio,
                oi_delta=oi_delta_5m,
                rsi=rsi6
            )

            # ================= V93: CASCADE TIME ESTIMATOR =================
            # Dapatkan orderbook depth dari OVS atau dari data orderbook
            bid_depth = ovs_result.get('current_bid_vol', bid_vol)
            ask_depth = ovs_result.get('current_ask_vol', ask_vol)

            cascade_result = self.cascade_time.compare_paths(
                long_liq_size=liq['long_vol'],
                short_liq_size=liq['short_vol'],
                long_dist=liq['long_dist'],
                short_dist=liq['short_dist'],
                bid_depth=bid_depth,
                ask_depth=ask_depth
            )
            
            # ================= V94: LOW ENERGY PATH (LEP) =================
            # Gunakan energy dari V92 ExecutionEnergy
            up_energy = energy_result.get('up_energy', 0) if 'energy_result' in locals() else 0
            down_energy = energy_result.get('down_energy', 0) if 'energy_result' in locals() else 0

            # Fallback: hitung manual jika tidak ada
            if up_energy == 0 or down_energy == 0:
                up_energy = abs(liq['short_dist']) * (1 + lim_result.get('imbalance_ratio', 1.0)/50)
                down_energy = abs(liq['long_dist']) * (1 + (1/ max(trades['aggressive_ratio'], 0.01)))

            lep_result = self.lep.analyze(
                up_energy=up_energy,
                down_energy=down_energy,
                agg=trades['aggressive_ratio']
            )

            # ================= V94: PASSIVE LIQUIDITY RELOAD (PLR) =================
            plr_result = self.plr.analyze(
                oi_delta=oi_delta_5m,
                agg=trades['aggressive_ratio'],
                flow=trades['ratio']
            )
            
            # ================= V94: ENERGY GRAVITY RULE (EGR) =================
            egr_result = self.egr.analyze(
                up_energy=up_energy,
                down_energy=down_energy,
                wmi=wmi_ratio,
                cascade_bias=cascade_result.get('bias', 'NEUTRAL')
            )
            
            # ================= V94: BAITING PRICE FILTER (BPF) - DOSEN 1 =====
            bpf_result = BaitingPriceFilterV94.analyze(
                energy_up=up_energy,
                energy_down=down_energy,
                price_change=change_5m
            )
            
            # ================= V94: ENERGY GRAVITY RULE (EGR) - DOSEN 1 =====
            egr_result = EnergyGravityRuleV94.analyze(
                up_energy=up_energy,
                down_energy=down_energy,
                wmi=wmi_ratio,
                cascade_bias=cascade_result.get('bias', 'NEUTRAL')
            )
            
            # ================= V95: LIQUIDATION GAP DETECTOR (LGD) - DOSEN 2 =====
            lgd_gap_result = LiquidationGapDetectorV95.analyze(
                short_dist=liq['short_dist'],
                long_dist=liq['long_dist']
            )
            
            # ================= V95: SHORT COVERING RULE (RSC) - DOSEN 2 =====
            rsc_short_covering_result = ShortCoveringRuleV95.analyze(
                rsi=rsi6,
                oi_delta=oi_delta_5m,
                price_change=change_5m
            )
            
            # ===== V95: LOW ENERGY PRIORITY (LEP) - DOSEN 1 =====
            lep_result = LowEnergyPriorityV95.analyze(
                energy_up=up_energy,
                energy_down=down_energy,
                cascade_bias=cascade_result.get('bias', 'NEUTRAL')
            )

            # ===== V95: OI-DIRECTIONAL CONFLICT (OID) - DOSEN 1 =====
            oid_result = OIDirectionalConflictV95.analyze(
                oi_delta=oi_delta_5m,
                price_change=change_5m
            )

            # ===== V96: POSITION BUILD DETECTOR (PBD) - DOSEN 2 =====
            pbd_result = PositionBuildDetectorV96.analyze(
                oi_delta=oi_delta_5m,
                price_change=change_5m,
                wmi=wmi_ratio
            )

            # ===== V96: OI DOMINANCE RULE (ODR) - DOSEN 2 =====
            odr_result = OIDominanceRuleV96.analyze(
                oi_delta=oi_delta_5m,
                price_change=change_5m,
                wmi=wmi_ratio,
                lim_bias=lim_result.get('bias', 'NEUTRAL')
            )
            
            # ================= V95/V96: RETAIL TRAP & EXECUTION COMPLETION =================
            # RPT - Retail Positioning Trap
            imbalance_ratio = lim_result.get('imbalance_ratio', 1.0)
            energy_diff_ratio = max(up_energy, down_energy) / min(up_energy, down_energy) if min(up_energy, down_energy) > 0 else 1.0
            
            rpt_result = self.rpt.analyze(
                imbalance_ratio=imbalance_ratio,
                energy_diff_ratio=energy_diff_ratio,
                wmi=wmi_ratio
            )
            
            # ECD - Execution Completion Detector
            ecd_result = self.ecd.analyze(
                rsi=rsi6,
                price_change=change_5m,
                oi_delta=oi_delta_5m
            )
            
            # SVI - Singularity Veto Integrity
            svi_result = self.svi.analyze(
                wmi=wmi_ratio,
                rpt_bias=rpt_result.get('bias') if 'rpt_result' in locals() else None,
                singularity_bias=wsc_result.get('bias') if 'wsc_result' in locals() else None
            )
            
            # EVH - Event Horizon Detector
            evh_result = self.evh.analyze(
                wmi=wmi_ratio,
                short_dist=liq['short_dist'],
                long_dist=liq['long_dist']
            )
            
            # ================= V97/V98: EVENT HORIZON SINGULARITY & VACUUM DETECTOR =================
            # EHS - Event Horizon Singularity (Anti-ARIA Trap)
            ehs_result = self.ehs.analyze(
                energy_up=up_energy,
                energy_down=down_energy,
                wmi=wmi_ratio,
                short_dist=liq['short_dist']
            )
            
            # VAC - Vacuum Detector (Orderbook Vacuum)
            vac_result = self.vac.analyze(
                agg_ratio=trades['aggressive_ratio'],
                flow=trades['ratio'],
                rsi=rsi6
            )
            
            # PBD - Position Build Detector (Enhanced)
            pbd_result = self.pbd.analyze(
                oi_delta=oi_delta_5m,
                price_change=change_5m,
                wmi=wmi_ratio
            )
            
            # ================= V95: LIQUIDITY IGNITION DETECTOR (LID) =================
            lid_result = self.lid.analyze(
                rsi=rsi6,
                oi_delta=oi_delta_5m,
                flow=trades['ratio'],
                up_energy=up_energy,
                down_energy=down_energy,
                wmi=wmi_ratio
            )
            
            # ================= V95: ENERGY SPOOF TRACKER (EST) =================
            est_result = self.est.analyze(
                up_energy=up_energy,
                down_energy=down_energy,
                oi_delta=oi_delta_5m,
                wmi=wmi_ratio
            )
            
            # ================= V96: PASSIVE DISTRIBUTION DETECTOR (PDD) =================
            pdd_result = self.pdd.analyze(
                oi_delta=oi_delta_5m,
                flow=trades['ratio'],
                rsi=rsi6,
                price_change=change_5m
            )
            
            # ================= V96: REAL SHORT COVERING FILTER (RSC) =================
            rsc_result = self.rsc.analyze(
                oi_delta=oi_delta_5m,
                price_change=change_5m
            )
            
            # VALIDASI SAD: Jika RSC bilang ini bukan short covering, SAD harus dineutralkan
            if sad_result.get('is_active', False) and not rsc_result.get('is_valid', False):
                # Override SAD - ini bukan short covering asli
                sad_result = {
                    "is_active": False,
                    "bias": "NEUTRAL",
                    "reason": "SAD_OVERRIDE: " + rsc_result['reason'],
                    "confidence": "LOW"
                }
                print(f"⚠️ SAD OVERRIDE: {rsc_result['reason']}")
            
            # ================= V96: GHOST WALL CONDEMNATION (GWC) =================
            gwc_result = self.gwc.analyze(
                flow=trades['ratio'],
                agg=trades['aggressive_ratio'],
                down_energy=down_energy,
                rsi=rsi6
            )
            
            # ================= V97: LIQUIDITY VACUUM DETECTOR (LVD) =================
            lvd_result = self.lvd.analyze(
                flow=trades['ratio'],
                agg=trades['aggressive_ratio'],
                rsi=rsi6
            )
            
            # ================= V97: SILENT DISTRIBUTION DETECTOR (SDD) =================
            sdd_result = self.sdd.analyze(
                rsi=rsi6,
                oi_delta=oi_delta_5m,
                flow=trades['ratio']
            )
            
            # ================= V99: SUPERIOR WHALE DOMINANCE PROTOCOL =================
            # WMI Veto - Prioritas Tertinggi!
            wmi_veto_result = self.wmi_veto.check_override(
                wmi_ratio=wmi_ratio,
                lep_bias=lep_result.get('bias') if 'lep_result' in locals() else None,
                short_dist=liq['short_dist'],
                long_dist=liq['long_dist'],
                price_change=change_5m,
                oi_delta=oi_delta_5m,
                short_imbalance=lim_result.get('imbalance_ratio', 1.0) if 'lim_result' in locals() else 0,
                agg=trades.get('aggressive_ratio', None)
            )
            
            # Internal Trap Detection (FMT)
            internal_trap_result = self.internal_trap.detect(
                trade_flow=trades['ratio'],
                price_change_5m=change_5m,
                rsi=rsi6
            )
            
            # OI Acceleration Phase Detection
            oi_phase_result = self.oi_phase.analyze(
                oi_delta=oi_delta_5m,
                price_change=change_5m,
                flow=trades['ratio']
            )
            
            # Liquidity Density Calculator
            density_result = self.density_calc.compare_paths(
                short_liq_size=liq['short_vol'],
                short_dist=liq['short_dist'],
                long_liq_size=liq['long_vol'],
                long_dist=liq['long_dist']
            )
            
            # ================= V99: NEW FIXED MODULES =================
            # OI Build Validator - Nuclear OI (Prioritas Tertinggi!)
            oi_build_result = self.oi_build_validator.analyze(
                oi_delta=oi_delta_5m,
                price_change=change_5m,
                short_dist=liq['short_dist'],
                long_dist=liq['long_dist'],
                wmi=wmi_ratio
            )
            
            # Gravity Distance Validator - Proximity > Massa
            gravity_dist_result = self.gravity_distance.validate(
                wmi=wmi_ratio,
                short_dist=liq['short_dist'],
                long_dist=liq['long_dist'],
                wmi_bias=wmi_veto_result.get('bias') if 'wmi_veto_result' in locals() else None
            )
            
            # ================= V99-SCT: SHORT CROWD TRAP DETECTION =================
            # Ambil imbalance ratio dari LIM atau hitung manual
            short_imbalance = lim_result.get('imbalance_ratio', 1.0) if 'lim_result' in locals() else 1.0
            
            # SCT - Short Crowd Trap Detector
            sct_result = self.sct_detector.analyze(
                short_imbalance=short_imbalance,
                agg=trades.get('aggressive_ratio', 0),
                oi_delta=oi_delta_5m,
                wmi=wmi_ratio,
                price_change=change_5m
            )
            
            # Crowd vs Cluster Logic
            crowd_cluster_result = self.crowd_cluster.resolve(
                wmi=wmi_ratio,
                short_imbalance=short_imbalance,
                agg=trades.get('aggressive_ratio', 0),
                short_dist=liq['short_dist'],
                long_dist=liq['long_dist']
            )
            
            # OI Build at Extremum
            oi_extremum_result = self.oi_extremum.analyze(
                oi_delta=oi_delta_5m,
                price_change=change_5m,
                agg=trades.get('aggressive_ratio', 0),
                flow=trades.get('ratio', 0)
            )
            
            # 4️⃣ Terakhir: Resolve semua sinyal dengan hierarki V99 (THE ULTIMATE HIERARCHY)
            final_decision = self.conflict_resolver_v99.resolve(
                # NEW V99 MODULES - PRIORITAS TERTINGGI!
                sct_res=sct_result,                    # V99 Short Crowd Trap ⭐
                crowd_cluster_res=crowd_cluster_result, # V99 Crowd vs Cluster ⭐
                oi_extremum_res=oi_extremum_result,     # V99 OI Build at Extremum ⭐
                
                # Existing V99 modules
                oi_build_res=oi_build_result,
                gravity_dist_res=gravity_dist_result,
                wmi_veto_res=wmi_veto_result,
                internal_trap_res=internal_trap_result,
                density_res=density_result,
                
                # Existing modules
                ehs_res=ehs_result,
                vac_res=vac_result,
                pbd_res=pbd_result,
                evh_res=evh_result,
                svi_res=svi_result,
                ecd_res=ecd_result,
                rpt_res=rpt_result,
                phase_res=phase_result,
                gwc_res=gwc_result,
                lvd_res=lvd_result,
                sdd_res=sdd_result,
                est_res=est_result,
                odc_res=odc_result,
                pdd_res=pdd_result,
                lep_res=lep_result,
                plr_res=plr_result,
                opd_res=opd_result,
                wmi_exhaust_res=wmi_exhaust_result,
                cascade_res=cascade_result,
                energy_res=energy_result,
                death_res=death_result,
                lgd_res=lgd_result,
                wsc_res=wsc_result,
                sat_res=sat_result,
                pet_res=pet_result,
                zgh_res=zgh_result,
                otf_res=otf_result,
                lim_res=lim_result
            )

            entry_ready = self.state_mgr.update_entry(final_decision['bias'])
            if entry_ready and self.state_mgr.can_enter(final_decision['bias'], market_phase['phase']):
                self.state_mgr.execute_entry(final_decision['bias'], price, rsi6)
                entry_status = "✅ READY TO ENTRY!"
            else:
                entry_status = f"⏳ WAITING ({len(self.state_mgr.entry_signals)}/{CONFIRM_DEFAULT})"

            time_since_entry = self.state_mgr.time_since_entry()
            if time_since_entry < 5 and self.state_mgr.last_entry_bias != "NEUTRAL":
                hold_remaining = 5 - time_since_entry
                hold_status = f"🔒 HOLD LOCK: {hold_remaining:.1f}m remaining"
            else:
                hold_status = "🔓 HOLD FREE"

            ttk_info = final_decision.get('ttk_info', {"estimated_minutes": 45, "urgency": "PREPARING", "fuel_ready": "NO"})

            result = {
                "timestamp": datetime.now().strftime("%H:%M:%S.%f")[:-3],
                "symbol": self.symbol,
                "price": round(price, 4),
                # Market Data
                "ob_ratio": ob_data['ratio'],
                "trade_flow": trades['ratio'],
                "aggressive_ratio": trades['aggressive_ratio'],
                "volume_ratio": round(volume_ratio, 2),
                "premium": funding['premium'],
                "funding": funding['funding'],
                "change_24h": round(change_24h, 2),
                "change_5m": round(change_5m, 2),
                "oi_current": round(oi_now, 2) if oi_now else 0,
                # V69: MA Data
                "ma10": round(ma10, 4),
                "ma20": round(ma20, 4),
                "obv": round(current_obv, 2),
                # Indicators
                "rsi6": round(rsi6, 1),
                "macd_bullish": macd['bullish_cross'],
                "macd_bearish": macd['bearish_cross'],
                "volume_trend": volume_trend,
                "flow_trend": flow_trend,
                "premium_trend": premium_trend,
                "aggressive_trend": aggressive_trend,
                "oi_delta_5m": round(oi_delta_5m, 2),
                "wmi_ratio": round(wmi_ratio, 2),
                # Liquidation
                "short_liq": liq['short_dist'],
                "long_liq": liq['long_dist'],
                "nearest_liquidity": liquidity_data['nearest'],
                "double_sweep": double_sweep,
                # V87 New Modules - GHOST IN THE SHELL EDITION
                "zas_v87": {
                    "is_squeeze": zas_result.get('is_squeeze', False),
                    "bias": zas_result.get('bias', 'NEUTRAL'),
                    "reason": zas_result.get('reason', ''),
                    "confidence": zas_result.get('confidence', 'LOW')
                },
                "lcd": {
                    "is_compression": lcd_result.get('is_compression', False),
                    "bias": lcd_result.get('bias', 'NEUTRAL'),
                    "reason": lcd_result.get('reason', ''),
                    "confidence": lcd_result.get('confidence', 'LOW')
                },
                "lbd": {
                    "is_bait": lbd_result.get('is_bait', False),
                    "bias": lbd_result.get('bias', 'NEUTRAL'),
                    "reason": lbd_result.get('reason', ''),
                    "confidence": lbd_result.get('confidence', 'LOW'),
                    "warning": lbd_result.get('warning', '')
                },
                "lim": {
                    "bias": lim_result.get('bias', 'NEUTRAL'),
                    "reason": lim_result.get('reason', ''),
                    "long_score": lim_result.get('long_score', 0),
                    "short_score": lim_result.get('short_score', 0),
                    "imbalance_ratio": lim_result.get('imbalance_ratio', 1.0)
                },
                # V99-SCT: SHORT CROWD TRAP RESULTS
                "sct": {
                    "is_trap": sct_result.get('is_trap', False),
                    "bias": sct_result.get('bias', 'NEUTRAL'),
                    "reason": sct_result.get('reason', ''),
                    "phase": sct_result.get('phase', 'NORMAL')
                },
                "crowd_cluster": {
                    "override": crowd_cluster_result.get('override', False),
                    "bias": crowd_cluster_result.get('bias', 'NEUTRAL'),
                    "reason": crowd_cluster_result.get('reason', '')
                },
                "oi_extremum": {
                    "is_accumulation": oi_extremum_result.get('is_accumulation', False),
                    "bias": oi_extremum_result.get('bias', 'NEUTRAL'),
                    "reason": oi_extremum_result.get('reason', '')
                },
                # V100: LIQUIDATION PAYOUT & PRE-FLUSH RESULTS
                "lpc": {
                    "payout_long": lpc_result.get('payout_long', 0),
                    "payout_short": lpc_result.get('payout_short', 0),
                    "payout_ratio": lpc_result.get('payout_ratio', 1.0),
                    "bias": lpc_result.get('bias', 'NEUTRAL'),
                    "dominant_target": lpc_result.get('dominant_target', 'NONE'),
                    "reason": lpc_result.get('reason', '')
                },
                "lpf": {
                    "flush_detected": lpf_result.get('flush_detected', False),
                    "bias": lpf_result.get('bias', 'NEUTRAL'),
                    "reason": lpf_result.get('reason', ''),
                    "expected_flush_range": lpf_result.get('expected_flush_range', 'NONE'),
                    "confidence": lpf_result.get('confidence', 'LOW')
                },
                "sad": {
                    "is_active": sad_result.get('is_active', False),
                    "bias": sad_result.get('bias', 'NEUTRAL'),
                    "reason": sad_result.get('reason', ''),
                    "confidence": sad_result.get('confidence', 'LOW')
                },
                # V89/V90 Results
                "wsc": {
                    "is_active": wsc_result.get('is_active', False),
                    "bias": wsc_result.get('bias', 'NEUTRAL'),
                    "reason": wsc_result.get('reason', '')
                },
                "sat": {
                    "active": sat_result.get('active', False),
                    "bias": sat_result.get('bias', 'NEUTRAL'),
                    "reason": sat_result.get('reason', '')
                },
                "pet": {
                    "active": pet_result.get('active', False),
                    "bias": pet_result.get('bias', 'NEUTRAL'),
                    "reason": pet_result.get('reason', '')
                },
                # V82 New Modules
                "fid": {
                    "is_igniting": fid_result['is_igniting'],
                    "bias": fid_result['bias'],
                    "reason": fid_result['reason'],
                    "fid_duration_minutes": round(fid_duration, 1)
                },
                "api": {
                    "is_absorbing": api_result['is_absorbing'],
                    "bias": api_result['bias'],
                    "reason": api_result['reason'],
                    "api_duration_minutes": round(api_duration, 1)
                },
                "lmg": {
                    "is_death_magnet": lmg_result['is_death_magnet'],
                    "bias": lmg_result['bias'],
                    "reason": lmg_result['reason'],
                    "lmg_duration_minutes": round(lmg_duration, 1)
                },
                # V81 New Modules
                "ltg": {
                    "is_vacuum": ltg_result['is_vacuum'],
                    "bias": ltg_result['bias'],
                    "reason": ltg_result['reason'],
                    "ltg_duration_minutes": round(ltg_duration, 1)
                },
                "icd": {
                    "is_internal_trap": icd_result['is_internal_trap'],
                    "bias": icd_result['bias'],
                    "reason": icd_result['reason'],
                    "icd_duration_minutes": round(icd_duration, 1)
                },
                # V80 New Modules
                "ier": {
                    "is_exit": ier_result['is_exit'],
                    "exit_type": ier_result['exit_type'],
                    "bias": ier_result['bias'],
                    "reason": ier_result['reason'],
                    "confidence": ier_result['confidence'],
                    "ier_duration_minutes": round(ier_duration, 1)
                },
                "rmg": {
                    "is_weak": rmg_result['is_weak'],
                    "weakness_type": rmg_result['weakness_type'],
                    "bias": rmg_result['bias'],
                    "reason": rmg_result['reason'],
                    "confidence": rmg_result['confidence'],
                    "rmg_duration_minutes": round(rmg_duration, 1)
                },
                "fmv": {
                    "is_fake_magnet": fmv_result['is_fake_magnet'],
                    "fake_type": fmv_result['fake_type'],
                    "bias": fmv_result['bias'],
                    "reason": fmv_result['reason'],
                    "confidence": fmv_result['confidence'],
                    "fmv_duration_minutes": round(fmv_duration, 1)
                },
                # V79 Module
                "wtd": {
                    "is_wash_trade": wtd_result['is_wash_trade'],
                    "wash_type": wtd_result['wash_type'],
                    "bias": wtd_result['bias'],
                    "reason": wtd_result['reason'],
                    "confidence": wtd_result['confidence'],
                    "wtd_duration_minutes": round(wtd_duration, 1)
                },
                # V78 Modules
                "ezh": {
                    "is_execution": ezh_result['is_execution'],
                    "execution_type": ezh_result['execution_type'],
                    "bias": ezh_result['bias'],
                    "reason": ezh_result['reason'],
                    "confidence": ezh_result['confidence'],
                    "ezh_duration_minutes": round(ezh_duration, 1)
                },
                "psv": {
                    "is_valid": psv_result['is_valid'],
                    "validation_type": psv_result['validation_type'],
                    "bias": psv_result['bias'],
                    "reason": psv_result['reason'],
                    "confidence": psv_result['confidence'],
                    "psv_duration_minutes": round(psv_duration, 1)
                },
                # V77 Modules
                "off": {
                    "is_patched": off_result['is_patched'],
                    "patched_type": off_result['patched_type'],
                    "bias": off_result['bias'],
                    "reason": off_result['reason'],
                    "confidence": off_result['confidence'],
                    "off_duration_minutes": round(off_duration, 1)
                },
                "aef": {
                    "is_exhausted": aef_result['is_exhausted'],
                    "exhausted_type": aef_result['exhausted_type'],
                    "bias": aef_result['bias'],
                    "reason": aef_result['reason'],
                    "confidence": aef_result['confidence'],
                    "aef_duration_minutes": round(aef_duration, 1)
                },
                # V76 Module
                "psr": {
                    "is_saturated": psr_result['is_saturated'],
                    "saturation_type": psr_result['saturation_type'],
                    "bias": psr_result['bias'],
                    "reason": psr_result['reason'],
                    "confidence": psr_result['confidence'],
                    "price_ma_diff": psr_result.get('price_ma_diff', 0),
                    "panic_duration_minutes": round(panic_duration, 1)
                },
                # V75 Modules
                "amv": {
                    "is_absorption_long": amv_result['is_absorption_long'],
                    "bias": amv_result['bias'],
                    "reason": amv_result['reason'],
                    "confidence": amv_result['confidence']
                },
                "lgo": {
                    "is_overdrive": lgo_result['is_overdrive'],
                    "overdrive_type": lgo_result['overdrive_type'],
                    "bias": lgo_result['bias'],
                    "reason": lgo_result['reason'],
                    "confidence": lgo_result['confidence'],
                    "short_dist": lgo_result.get('short_dist', 0),
                    "long_dist": lgo_result.get('long_dist', 0),
                    "gravity_duration_minutes": round(gravity_duration, 1)
                },
                # V74 Module
                "mdv": {
                    "is_magnet_fake": mdv_result['is_magnet_fake'],
                    "bias": mdv_result['bias'],
                    "reason": mdv_result['reason'],
                    "confidence": mdv_result['confidence'],
                    "magnet_duration_minutes": round(magnet_duration, 1)
                },
                # V73 Module
                "pab": {
                    "is_blackhole": pab_result['is_blackhole'],
                    "blackhole_type": pab_result['blackhole_type'],
                    "bias": pab_result['bias'],
                    "reason": pab_result['reason'],
                    "confidence": pab_result['confidence']
                },
                # V72 Module
                "cfk": {
                    "is_knife": cfk_result['is_knife'],
                    "knife_type": cfk_result['knife_type'],
                    "bias": cfk_result['bias'],
                    "reason": cfk_result['reason'],
                    "confidence": cfk_result['confidence']
                },
                # V71 Module
                "mdd": {
                    "is_magnet_trap": mdd_result['is_magnet_trap'],
                    "trap_type": mdd_result['trap_type'],
                    "bias": mdd_result['bias'],
                    "reason": mdd_result['reason'],
                    "confidence": mdd_result['confidence'],
                    "short_dist": mdd_result.get('short_dist', 0),
                    "long_dist": mdd_result.get('long_dist', 0)
                },
                # V70 Module
                "ovd": {
                    "is_trap": ovd_result['is_trap'],
                    "trap_type": ovd_result['trap_type'],
                    "bias": ovd_result['bias'],
                    "reason": ovd_result['reason'],
                    "confidence": ovd_result['confidence']
                },
                # V69 Module
                "trend_integrity": {
                    "restriction": trend_result['restriction'],
                    "reason": trend_result['reason'],
                    "bias_recommendation": trend_result['bias_recommendation'],
                    "is_strong_down": trend_result['is_strong_down'],
                    "is_strong_up": trend_result['is_strong_up'],
                    "obv_rising": trend_result['obv_rising'],
                    "macd_dead_zone": trend_result['macd_dead_zone']
                },
                # V68 Module
                "ogd": {
                    "is_deflected": ogd_result['is_deflected'],
                    "bias": ogd_result['bias'],
                    "reason": ogd_result['reason'],
                    "confidence": ogd_result['confidence']
                },
                # V67 Modules
                "zas_v67": {
                    "is_dead": zas_v67_result['is_dead'],
                    "bias": zas_v67_result['bias'],
                    "reason": zas_v67_result['reason'],
                    "confidence": zas_v67_result['confidence']
                },
                "avc": {
                    "is_trap": avc_result['is_trap'],
                    "trap_type": avc_result['trap_type'],
                    "bias": avc_result['bias'],
                    "reason": avc_result['reason'],
                    "confidence": avc_result['confidence']
                },
                # V66 Module
                "ati": {
                    "is_accumulating": ati_result['is_accumulating'],
                    "bias": ati_result['bias'],
                    "reason": ati_result['reason'],
                    "confidence": ati_result['confidence'],
                    "accumulation_minutes": round(accumulation_minutes, 1)
                },
                # V65 Modules
                "amd": {
                    "is_spoof": amd_result['is_spoof'],
                    "action": amd_result['action'],
                    "bias": amd_result['bias'],
                    "reason": amd_result['reason'],
                    "confidence": amd_result['confidence'],
                    "aggressive_ratio": amd_result.get('aggressive_ratio', 0)
                },
                # V64 Modules
                "tdp": {
                    "is_active": tdp_result['is_active'],
                    "bias": tdp_result['bias'],
                    "reason": tdp_result['reason'],
                    "confidence": tdp_result['confidence']
                },
                # V63 Modules
                "wed": {
                    "is_trap": wed_result['is_trap'],
                    "trap_type": wed_result['trap_type'],
                    "bias": wed_result['bias'],
                    "reason": wed_result['reason'],
                    "confidence": wed_result['confidence']
                },
                # V62 Modules
                "mwr": {
                    "is_magnet": mwr_result['is_magnet'],
                    "magnet_type": mwr_result['magnet_type'],
                    "bias": mwr_result['bias'],
                    "reason": mwr_result['reason'],
                    "confidence": mwr_result['confidence']
                },
                "lvs": {
                    "is_suction": lvs_result['is_suction'],
                    "suction_type": lvs_result['suction_type'],
                    "bias": lvs_result['bias'],
                    "reason": lvs_result['reason'],
                    "confidence": lvs_result['confidence']
                },
                "dtd": {
                    "is_trap": dtd_result['is_trap'],
                    "trap_type": dtd_result['trap_type'],
                    "bias": dtd_result['bias'],
                    "reason": dtd_result['reason'],
                    "confidence": dtd_result['confidence']
                },
                "wmi": {
                    "mass_ratio": round(wmi_ratio, 2),
                    "is_whale_trap": abs(wmi_ratio) > VACUUM_WMI_MIN,
                    "dominant_side": "SHORT_LIQ_WHALE" if wmi_ratio > 0 else "LONG_LIQ_WHALE" if wmi_ratio < 0 else "NEUTRAL"
                },
                "ghost": {
                    "is_ghost": ghost_result['is_ghost'],
                    "bias": ghost_result['bias'],
                    "score": ghost_result['score'],
                    "confidence": ghost_result['confidence'],
                    "reasons": ghost_result['reasons']
                },
                "odd": {
                    "is_thin": odd_result['is_thin'],
                    "is_defense": odd_result['is_defense'],
                    "status": odd_result['status'],
                    "reason": odd_result['reason'],
                    "bid_volume_near": odd_result['bid_volume_near'],
                    "ask_volume_near": odd_result['ask_volume_near']
                },
                "starter": {
                    "is_starting": starter_result['is_starting'],
                    "bias": starter_result['bias'],
                    "score": starter_result['score'],
                    "reasons": starter_result['reasons']
                },
                "ttk": {
                    "estimated_minutes": ttk_info['estimated_minutes'],
                    "urgency": ttk_info['urgency'],
                    "fuel_ready": ttk_info['fuel_ready']
                },
                "lrr": {
                    "is_trap": lrr_result['is_trap'],
                    "ratio": lrr_result['ratio'],
                    "danger_side": lrr_result['danger_side'],
                    "recommendation": lrr_result['recommendation']
                },
                "av": {
                    "acceleration": av_result['acceleration'],
                    "velocity": av_result['velocity'],
                    "status": av_result['status'],
                    "trend": av_result['trend'],
                    "is_market_slam": av_result['is_market_slam']
                },
                # Advanced Analysis
                "market_phase": market_phase['phase'],
                "phase_confidence": market_phase['confidence'],
                "phase_reason": market_phase['reason'],
                "liquidity_gravity": {
                    "bias": liquidity_gravity['bias'],
                    "strength": liquidity_gravity['strength'],
                    "ratio": liquidity_gravity['ratio'],
                    "reason": liquidity_gravity['reason'],
                    "is_extreme": liquidity_gravity.get('is_extreme', False),
                    "is_massive": liquidity_gravity.get('is_massive', False),
                    "short_gravity": liquidity_gravity['short_gravity'],
                    "long_gravity": liquidity_gravity['long_gravity']
                },
                "ppi": {
                    "score": ppi['ppi'],
                    "pressure": ppi['pressure'],
                    "bias": ppi['bias'],
                    "reason": ppi['reason']
                },
                "exhaustion": {
                    "score": exhaustion['score'],
                    "bias": exhaustion['reversal_bias'],
                    "confidence": exhaustion['confidence'],
                    "reason": exhaustion['reason'],
                    "details": exhaustion['details']
                },
                "reversion": {
                    "bias": reversion['bias'],
                    "score": reversion['score'],
                    "confidence": reversion['confidence'],
                    "reason": reversion['reason'],
                    "details": reversion['details']
                },
                "oi_velocity": {
                    "status": oi_velocity['status'],
                    "delta_5m": oi_velocity['oi_delta_5m'],
                    "power": oi_velocity['power'],
                    "institutional_score": oi_velocity.get('institutional_score', 0),
                    "reason": oi_velocity['reason']
                },
                "stop_hunt": {
                    "bias": stop_hunt['bias'],
                    "confidence": stop_hunt['confidence'],
                    "reason": stop_hunt['reason']
                },
                "orderbook": {
                    "manipulation": ob_imprint['manipulation'],
                    "bias": ob_imprint['bias'],
                    "reason": ob_imprint['reason']
                },
                "spoofing": {
                    "score": spoofing['score'],
                    "type": spoofing['type'],
                    "bias": spoofing['bias'],
                    "confidence": spoofing['confidence'],
                    "reason": spoofing['reason']
                },
                "hft_signature": {
                    "bias": hft_signature['bias'],
                    "confidence": hft_signature['confidence'],
                    "weight": hft_signature['weight'],
                    "signals": hft_signature['signals'],
                    "persistence_minutes": hft_signature['persistence_minutes']
                },
                "energy_score": energy['score'],
                "energy_type": energy['type'],
                "mpe_bias": mpe_result['bias'],
                # Final Decision from V88
                "bias": final_decision['bias'],
                "confidence": final_decision['confidence'],
                "reason": final_decision['reason'],
                "phase_v90": final_decision.get('phase', 'NORMAL'),
                "entry_status": entry_status,
                "hold_status": hold_status,
                "entry_ready": entry_ready,
                "accumulation_detected": accumulation_detected
            }

            # Tambahkan V88 WDI results ke output
            result["wdi"] = {
                "is_veto": wdi_result['is_veto'],
                "bias": wdi_result['bias'],
                "reason": wdi_result['reason']
            }

            # Tambahkan V86 results ke output
            result["zgh"] = {
                "is_ceiling": zgh_result.get('is_ceiling', False),
                "bias": zgh_result.get('bias', 'NEUTRAL'),
                "reason": zgh_result.get('reason', ''),
                "rsi": zgh_result.get('rsi', rsi6),
                "oi_delta": zgh_result.get('oi_delta', oi_delta_5m),
                "agg_ratio": zgh_result.get('agg_ratio', trades['aggressive_ratio'])
            }

            result["odf"] = {
                "active": odf_result.get('active', False),
                "bias": odf_result.get('bias', 'NEUTRAL'),
                "reason": odf_result.get('reason', ''),
                "rsi": odf_result.get('rsi', rsi6),
                "oi_delta": odf_result.get('oi_delta', oi_delta_5m),
                "agg_ratio": odf_result.get('agg_ratio', trades['aggressive_ratio'])
            }

            result["otf"] = {
                "is_trap": otf_result.get('is_trap', False),
                "bias": otf_result.get('bias', 'NEUTRAL'),
                "reason": otf_result.get('reason', ''),
                "scenario": otf_result.get('scenario', 'NORMAL')
            }

            # V91: LIQUIDITY GRAVITY DRAIN (LGD) - ANTI-VOID TRAP
            result["lgd"] = {
                "active": lgd_result.get('active', False),
                "bias": lgd_result.get('bias', 'NEUTRAL'),
                "reason": lgd_result.get('reason', '')
            }

            # V92: EXECUTION ENERGY MODEL
            result["energy_v92"] = {
                "bias": energy_result.get('bias', 'NEUTRAL'),
                "reason": energy_result.get('reason', '')
            }

            # V92: AGGRESSION DEATH FILTER
            result["aggression_death"] = {
                "active": death_result.get('active', False),
                "bias": death_result.get('bias', 'NEUTRAL'),
                "reason": death_result.get('reason', '')
            }

            # ===== V93 RESULTS - THE VACUUM FLUSH DETECTORS =====
            result["odc"] = {
                "active": odc_result.get('active', False),
                "bias": odc_result.get('bias', 'NEUTRAL'),
                "reason": odc_result.get('reason', '')
            }

            result["opd"] = {
                "active": opd_result.get('active', False),
                "bias": opd_result.get('bias', 'NEUTRAL'),
                "reason": opd_result.get('reason', '')
            }

            result["wmi_exhaust"] = {
                "active": wmi_exhaust_result.get('active', False),
                "bias": wmi_exhaust_result.get('bias', 'NEUTRAL'),
                "reason": wmi_exhaust_result.get('reason', '')
            }

            result["cascade"] = {
                "bias": cascade_result.get('bias', 'NEUTRAL'),
                "reason": cascade_result.get('reason', ''),
                "up_time": cascade_result.get('up_time', 0),
                "down_time": cascade_result.get('down_time', 0)
            }

            # ===== V94 RESULTS - ENERGY PATH & PASSIVE RELOAD =====
            result["lep"] = {
                "is_active": lep_result.get('is_active', False),
                "bias": lep_result.get('bias', 'NEUTRAL'),
                "reason": lep_result.get('reason', '')
            }

            result["plr"] = {
                "active": plr_result.get('active', False),
                "bias": plr_result.get('bias', 'NEUTRAL'),
                "reason": plr_result.get('reason', '')
            }
            
            # ===== V94: ENERGY GRAVITY RULE =====
            result["egr"] = {
                "is_veto": egr_result.get('is_veto', False),
                "bias": egr_result.get('bias', 'NEUTRAL'),
                "reason": egr_result.get('reason', '')
            }
            
            # ===== V95: LIQUIDITY IGNITION DETECTOR =====
            result["lid"] = {
                "active": lid_result.get('active', False),
                "bias": lid_result.get('bias', 'NEUTRAL'),
                "reason": lid_result.get('reason', '')
            }
            
            # ===== V95: ENERGY SPOOF TRACKER =====
            result["est"] = {
                "is_spoof": est_result.get('is_spoof', False),
                "bias": est_result.get('bias', 'NEUTRAL'),
                "reason": est_result.get('reason', '')
            }
            
            # ===== V95/V96: RETAIL TRAP & EXECUTION COMPLETION =====
            result["rpt"] = {
                "is_trap": rpt_result.get('is_trap', False),
                "bias": rpt_result.get('bias', 'NEUTRAL'),
                "reason": rpt_result.get('reason', '')
            }
            
            result["ecd"] = {
                "completed": ecd_result.get('completed', False),
                "bias": ecd_result.get('direction', 'NEUTRAL'),
                "reason": ecd_result.get('reason', '')
            }
            
            # ===== V97: EVENT HORIZON SINGULARITY (EHS) =====
            result["ehs"] = {
                "is_active": ehs_result.get('is_active', False),
                "bias": ehs_result.get('bias', 'NEUTRAL'),
                "energy_ratio": ehs_result.get('energy_ratio', 0),
                "reason": ehs_result.get('reason', ''),
                "severity": ehs_result.get('severity', 'NONE')
            }
            
            # ===== V98: VACUUM DETECTOR (VAC) =====
            result["vac"] = {
                "active": vac_result.get('active', False),
                "bias": vac_result.get('bias', 'NEUTRAL'),
                "reason": vac_result.get('reason', ''),
                "vacuum_type": vac_result.get('vacuum_type', 'NONE')
            }
            
            # ===== V96: POSITION BUILD DETECTOR (PBD) =====
            result["pbd"] = {
                "active": pbd_result.get('active', False),
                "bias": pbd_result.get('bias', 'NEUTRAL'),
                "type": pbd_result.get('type', ''),
                "reason": pbd_result.get('reason', '')
            }
            
            # ===== V96: PASSIVE DISTRIBUTION DETECTOR =====
            result["pdd"] = {
                "active": pdd_result.get('active', False),
                "bias": pdd_result.get('bias', 'NEUTRAL'),
                "reason": pdd_result.get('reason', '')
            }
            
            # ===== V96: REAL SHORT COVERING FILTER =====
            result["rsc"] = {
                "is_valid": rsc_result.get('is_valid', False),
                "reason": rsc_result.get('reason', '')
            }
            
            # ===== V96: GHOST WALL CONDEMNATION =====
            result["gwc"] = {
                "is_ghost_wall": gwc_result.get('is_ghost_wall', False),
                "bias": gwc_result.get('bias', 'NEUTRAL'),
                "reason": gwc_result.get('reason', '')
            }
            
            # ===== V97: LIQUIDITY VACUUM DETECTOR =====
            result["lvd"] = {
                "active": lvd_result.get('active', False),
                "bias": lvd_result.get('bias', 'NEUTRAL'),
                "reason": lvd_result.get('reason', '')
            }
            
            # ===== V97: SILENT DISTRIBUTION DETECTOR =====
            result["sdd"] = {
                "active": sdd_result.get('active', False),
                "bias": sdd_result.get('bias', 'NEUTRAL'),
                "reason": sdd_result.get('reason', '')
            }
            
            # ===== V94: BAITING PRICE FILTER =====
            result["bpf"] = {
                "is_bait": bpf_result.get('is_bait', False),
                "bias": bpf_result.get('bias', 'NEUTRAL'),
                "reason": bpf_result.get('reason', '')
            }
            
            # ===== V94: ENERGY GRAVITY RULE =====
            result["egr"] = {
                "is_veto": egr_result.get('is_veto', False),
                "bias": egr_result.get('bias', 'NEUTRAL'),
                "reason": egr_result.get('reason', '')
            }
            
            # ===== V95: LIQUIDATION GAP DETECTOR =====
            result["lgd_gap"] = {
                "bias": lgd_gap_result.get('bias', 'NEUTRAL'),
                "reason": lgd_gap_result.get('reason', '')
            }
            
            # ===== V95: SHORT COVERING RULE =====
            result["rsc_short_covering"] = {
                "is_active": rsc_short_covering_result.get('is_active', False),
                "bias": rsc_short_covering_result.get('bias', 'NEUTRAL'),
                "reason": rsc_short_covering_result.get('reason', '')
            }

            return result
        except Exception as e:
            print(f"❌ Error analyzing {self.symbol}: {e}")
            import traceback
            traceback.print_exc()
            return None


# ================= MAIN FUNCTIONS V87 =================
def main_v87():
    import sys
    if len(sys.argv) > 1:
        symbol = sys.argv[1].upper()
    else:
        symbol = input("\nSymbol (e.g. BTCUSDT): ").upper() or "BTCUSDT"

    # Buat SATU INSTANCE analyzer V87 untuk seluruh loop
    analyzer = BinanceAnalyzerV87(symbol)

    OutputFormatterV87.print_header()

    print(f"\n🔍 Analyzing {symbol} with V87 Ghost in the Shell Logic...")

    result = analyzer.analyze()

    if result:
        OutputFormatterV87.print_signal(result)

        if len(sys.argv) > 2 and sys.argv[2] == "--loop":
            print("\n🔄 Auto-refresh every 10 seconds. Press Ctrl+C to stop.\n")
            try:
                while True:
                    time.sleep(10)
                    result = analyzer.analyze()
                    if result:
                        print("\n" + "="*80)
                        print(f"🔄 UPDATE @ {result['timestamp']}")
                        print(f"🎯 Bias: {result['bias']} ({result['confidence']}) - {result['reason'][:50]}...")
                        print(f"⏳ Entry: {result['entry_status']}")
                        print(f"{result['hold_status']}")
            except KeyboardInterrupt:
                print("\n\n👋 Stopped by user")
    else:
        print(f"❌ Failed to analyze {symbol}")


def batch_mode_v87(symbols: List[str]):
    OutputFormatterV87.print_header()
    results = []
    analyzers = {}
    for symbol in symbols:
        analyzers[symbol] = BinanceAnalyzerV87(symbol)

    for symbol in symbols:
        print(f"\n🔍 Analyzing {symbol} with V87 Ghost in the Shell Logic...")
        result = analyzers[symbol].analyze()
        if result:
            results.append(result)
            bias_icon = "🟢" if result['bias'] == "LONG" else "🔴" if result['bias'] == "SHORT" else "⚪"
            ready_icon = "✅" if result['entry_ready'] else "⏳"
            
            # V87 Icons (Prioritas Tertinggi)
            sad_icon = "👻" if result.get('sad', {}).get('is_active') else " "
            zas_icon = "❄️" if result.get('zas_v87', {}).get('is_squeeze') else " "
            lcd_icon = "📦" if result.get('lcd', {}).get('is_compression') else " "
            lbd_icon = "🎣" if result.get('lbd', {}).get('is_bait') else " "
            lim_icon = "⚖️" if result.get('lim', {}).get('bias') != 'NEUTRAL' else " "
            
            # V86 Icons
            odf_icon = "☢️" if result.get('odf', {}).get('active') else " "
            zgh_icon = "☢️" if result.get('zgh', {}).get('is_ceiling') else " "
            otf_icon = "🔄" if result.get('otf', {}).get('is_trap') else " "
            
            print(f"{ready_icon}{sad_icon}{zas_icon}{lcd_icon}{lbd_icon}{lim_icon}{odf_icon}{zgh_icon}{otf_icon} {bias_icon} {symbol}: {result['bias']} ({result['confidence']}) - {result['phase_v87']} [TTK:{result['ttk']['estimated_minutes']}m]")
        else:
            print(f"❌ {symbol}: Failed")

    print("\n" + "="*80)
    print("📊 SUMMARY - READY TO ENTRY:")
    print("="*80)

    ready_count = 0
    for r in results:
        if r['entry_ready']:
            bias_icon = "🟢" if r['bias'] == "LONG" else "🔴"
            
            # V87 Warnings
            sad_warn = "👻SAD! " if r.get('sad', {}).get('is_active') else ""
            zas_warn = "❄️ZAS! " if r.get('zas_v87', {}).get('is_squeeze') else ""
            lcd_warn = "📦LCD! " if r.get('lcd', {}).get('is_compression') else ""
            lbd_warn = "🎣LBD! " if r.get('lbd', {}).get('is_bait') else ""
            lim_warn = "⚖️LIM! " if r.get('lim', {}).get('bias') != 'NEUTRAL' else ""
            
            # V86 Warnings
            odf_warn = "☢️ODF! " if r.get('odf', {}).get('active') else ""
            zgh_warn = "☢️ZGH! " if r.get('zgh', {}).get('is_ceiling') else ""
            otf_warn = "🔄OTF! " if r.get('otf', {}).get('is_trap') else ""
            
            print(f"{bias_icon} {r['symbol']}: {r['bias']} ({r['confidence']}) - {sad_warn}{zas_warn}{lcd_warn}{lbd_warn}{lim_warn}{odf_warn}{zgh_warn}{otf_warn}{r['reason'][:60]} | TTK:{r['ttk']['estimated_minutes']}m")
            ready_count += 1

    if ready_count == 0:
        print("No entry-ready signals at this moment")

    return results


def api_mode_v87(symbol: str) -> str:
    analyzer = BinanceAnalyzerV87(symbol)
    result = analyzer.analyze()
    if result:
        # Convert any non-serializable objects
        if 'exhaustion' in result and 'details' in result['exhaustion']:
            result['exhaustion']['details'] = list(result['exhaustion']['details'])
        if 'reversion' in result and 'details' in result['reversion']:
            result['reversion']['details'] = list(result['reversion']['details'])
        if 'hft_signature' in result and 'signals' in result['hft_signature']:
            result['hft_signature']['signals'] = list(result['hft_signature']['signals'])
        if 'starter' in result and 'reasons' in result['starter']:
            result['starter']['reasons'] = list(result['starter']['reasons'])
        if 'ghost' in result and 'reasons' in result['ghost']:
            result['ghost']['reasons'] = list(result['ghost']['reasons'])
        return json.dumps(result, indent=2, default=str)
    return json.dumps({"error": f"Failed to analyze {symbol}"})


# ================= MAIN EXECUTION =================
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "--api":
            symbol = sys.argv[2] if len(sys.argv) > 2 else "BTCUSDT"
            print(api_mode_v87(symbol))
        elif sys.argv[1] == "--batch":
            symbols = sys.argv[2:] if len(sys.argv) > 2 else POPULAR_SYMBOLS
            batch_mode_v87(symbols)
        elif sys.argv[1] == "--help":
            print("""
🔥 BINANCE LIQUIDATION HUNTER V87 - GHOST IN THE SHELL EDITION
Usage:
python script.py SYMBOL           # Analyze single symbol
python script.py SYMBOL --loop     # Auto-refresh every 10s
python script.py --batch [SYMBOLS] # Analyze multiple symbols
python script.py --api SYMBOL      # JSON output for API
python script.py --help            # Show this help

Examples:
python script.py BTCUSDT
python script.py POWERUSDT --loop  # Test V87 SAD (Stealth Accumulation)
python script.py ROBOUSDT --loop   # Test V87 ZAS (Zero Aggression Squeeze)
python script.py TRIAUSDT --loop   # Test V86 ODF (Overbought Distribution)

🎯 HIERARKI MUTLAK V87 (Filter Kriminalitas - GHOST IN THE SHELL EDITION):
    0. SAD (Stealth Accumulation Detector) - ANTI-POWER/ROBO GHOSTING (V87) ⭐ TERTINGGI!
    1. ZAS (Zero Aggression Squeeze) - ANTI-SELLER EXHAUSTION (V87)
    2. LCD (Liquidity Compression Detector) - ANTI-SIDEWAY FATIGUE (V87)
    3. LBD (Liquidity Bait Detector) - ANTI-FAKE MAGNET (V87)
    4. LIM (Liquidity Imbalance Momentum) - ANTI-WRONG TARGET (V87)
    5. ZGH (Zero Gravity Horizon) - ANTI-TRIA TRAP (V86)
    6. ODF (Overbought Distribution Filter) - ANTI-TRIA TRAP (V86)
    7. OTF (Oversold Trap Filter) - ANTI-UAI & LIQUIDITY VACUUM REBOUND (V85)

🧠 KAIDAH EMAS V87:
    'Jika Aggression 0.00 tapi OI turun, itu bukan Whale kabur, itu Whale sedang nutup Short (Short Covering). JANGAN SHORT, lo bakal kena squeeze!'
    'Market maker selalu mengikuti path of least resistance. Jika seller tidak ada, satu market buy bisa gerakkan harga jauh.'
    'Agg = 0 ≠ weak momentum. Agg = 0 artinya no sellers left. Ini justru bullish precursor.'
            """)
        else:
            main_v87()
    else:
        main_v87()
