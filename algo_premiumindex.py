#!/usr/bin/env python3
"""
🔥 BINANCE LIQUIDATION HUNTER V80 - THE BLACK BOX DISMANTLER
💀 Analisa Kegagalan V79 (Kenapa OPN, BARD & RIVER Tetap Loss?)
    Kasus OPN & BARD (The Neutral RSI Siphon):
        Data: RSI di area 39-51. Bot V79 mikir: "Ini masih jauh dari Overbought, masih bisa naik makan Magnet Short."
        Kenapa Loss? MM melakukan "Flow Inflation" (Flow 2.0x - 7.3x). Mereka melakukan order beli besar 
        tapi OI (Open Interest) justru STAGNAN atau TURUN (OPN +0.38%, BARD -0.67%).
        Artinya: Volume beli yang dilihat itu palsu/wash trade. Tidak ada posisi baru yang dibuka oleh institusi.
        Itu cuma umpan buat bot retail biar Entry Long.
    Kasus RIVER (The Gravity Decoy):
        Data: Short Liq +0.49% (Dekat banget!). Bot V79 terpicu GRAVITY_WARNING.
        Kenapa Loss? MM naruh likuidasi besar di jarak super dekat tapi TIDAK PERNAH DITABRAK.
        Mereka pakai gravitasi itu buat nahan harga di atas (High RSI 72) biar bot tidak berani SHORT,
        padahal MM lagi distribusi barang pelan-pelan.
🛡️ THE SUPREME COMMANDER: V80 "THE BLACK BOX DISMANTLER"
    Modul 1: "Institutional Exit Radar" (IER) - BARU!
        - Mendeteksi Whale yang sedang Exit (Cuci Tangan).
        - Jika Flow terlihat Bullish (>2.0x) tapi OI Delta mampet (<1.0%),
        artinya Whale tidak sedang buka posisi baru, tapi sedang menutup posisi (Distribusi).
        - Jangan tertipu Magnet Short di atas!
    Modul 2: "RSI Momentum Guard" (RMG) - BARU!
        - Mencegah Long di area 'RSI No Man's Land' (39-72).
        - Jika RSI > 50 tapi Agresi retail (Agg) < 1.0, harga tidak punya tenaga untuk nembus magnet atas.
        - MM akan ambil jalan termudah: DUMP ke bawah.
    Modul 3: "The Fake Magnet Vacuum" (FMV) - INTEGRATION
        - Kombinasi IER + RMG untuk mendeteksi "The Fake Magnet Vacuum"
        - Binance sengaja menciptakan magnet sebagai Likuiditas Tiruan untuk menarik bot LONG masuk,
        tepat sebelum mereka membanting harga.
🎯 HIERARKI MUTLAK V80 (THE HIERARCHY OF INSTITUTIONAL DECEPTION):
    1. EZH (Execution Zone Hunter) - ANTI-RIVER MAGNETIC SLINGSHOT
    2. WTD (Wash Trade Detector) - ANTI-KITE FALSE BRIDGE
    3. IER (Institutional Exit Radar) - NEW! ANTI-OPN/BARD FALSE FLOW
    4. RMG (RSI Momentum Guard) - NEW! ANTI-RIVER GRAVITY DECOY
    5. PSV (Panic Sell Validator) - ANTI-OPN ENDLESS FLOOR
    6. OFF (Overdrive Flow Filter) - ANTI-HUSDT TRAP
    7. AEF (Aggressive Exhaustion Filter) - ANTI-PHA TRAP
    8. PSR (Panic Saturation Reversal) - ANTI-HUMA DRIFT TRAP
    9. AMV (Absorption Momentum Validator) - ANTI-HUMA TRAP
    10. LGO (Liquidation Gravity Overdrive) - ANTI-RIVER NUCLEAR
    11. MDV (Magnet Decay Validator) - ANTI-RIVER SPOOF
    12. PAB (Passive Absorption Blackhole) - ANTI-SIREN TRAP
    13. CFK (Catching Falling Knives) - ANTI-ROBO TRAP
    14. MDD (Magnet Distance Dominance) - ANTI-RIVER TRAP
    15. OVD (Orderbook Vacuum Defense) - ANTI-PHA TRAP
    16. Trend Integrity (V69) - ANTI-PIPPIN/PHA/POWER
    17. Gravity Deflection (OGD) - ANTI-PIPPIN TRAP (V68)
    18. Zero Aggression Slaughter (ZAS) - ANTI-DEADSTICK (V67)
    19. Absorption Validity Check (AVC) - ANTI-EXIT LIQUIDITY TRAP (V67)
    20. Aggression-Mass Divergence (AMD) - ANTI-SPOOF PROTECTION (V65)
    21. The DYL Particle (TDP) - ABSOLUTE OVERRIDE (V64)
    22. Temporal Accumulation Index (ATI) - WHALE PATIENCE LOADING (V66)
    23. Wall Erasure Detection (WED) - GRAVITY MANDATE (V63)
    24. Magnet Wall Reversal (MWR) (V62)
    25. The Ghost Whisperer (LVS) (V61)
    26. The Absorption Shield (DTD) (V60)
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

# ================= CONFIG V80 (THE BLACK BOX DISMANTLER) =================
# ================= CONFIG V81 (LIQUIDITY QUANTUM) =================
LTG_FLOW_VACUUM_MIN = 50.0                    # Minimal Flow untuk deteksi Liquidity Vacuum
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
        
        if trade_flow > 50.0:  # Flow super anomali (Kasus KITE)
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
        
        if trade_flow > 2.0 and agg_ratio < 2.0 and abs(oi_delta) < 0.5:
            is_internal_trap = True
            bias = "LONG"
            reason = f"ICD_TRAP: Flow {trade_flow:.1f}x tinggi tapi agresi retail mati ({agg_ratio:.2f}x). Whale sedang Position Flipping! Bias IER SHORT dibatalkan. BIAS LONG!"
            
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
            if trade_flow > 2.0:  # WAJIB ADA FLOW WHALE
                is_exhausted = True
                bias = "LONG"
                exhausted_type = "PANIC_SELL_EXHAUSTION"
                confidence = "ABSOLUTE"
                reason = (f"PANIC_SELL_EXHAUSTION: Retail panic sell (Agg {agg_ratio:.2f}x) di RSI {rsi6:.1f} (oversold). "
                        f"Whale nampung beneran (Flow {trade_flow:.2f}x > 2.0x). SIAP REVERSAL LONG!")
            else:
                is_exhausted = True
                bias = "SHORT"  # JIKA FLOW RENDAH, INI FALLING KNIFE!
                exhausted_type = "CONTINUATION_DUMP"
                confidence = "ABSOLUTE"
                reason = (f"CONTINUATION_DUMP: RSI {rsi6:.1f} nol tapi Whale gak nampung (Flow {trade_flow:.2f}x < 2.0x). "
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
    """
    @staticmethod
    def analyze(short_dist: float, long_dist: float, rsi6: float, trade_flow: float) -> Dict:
        """
        Args:
            short_dist: Jarak ke likuidasi SHORT (dalam persen)
            long_dist: Jarak ke likuidasi LONG (dalam persen)
            rsi6: RSI 6 period
            trade_flow: Rasio volume beli/jual
        Returns:
            Dict dengan is_overdrive, bias, reason, confidence
        """
        is_overdrive = False
        bias = "NEUTRAL"
        reason = "Normal distance"
        confidence = "LOW"
        overdrive_type = "NONE"

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
            flow_consistent = all(f > 2.0 for f in flow_history[-3:])

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
            if ask_volume_near < ODD_VOLUME_MIN and bid_volume_near > ask_volume_near * 3:
                is_thin = True
                status = "ASK_THINNING"
                reason = f"Ask side tipis ({ask_volume_near:.0f}), Bid side tebal ({bid_volume_near:.0f}) - Jalan ke atas terbuka"
            # Deteksi defense (bandar menahan harga)
            elif ask_volume_near > ODD_VOLUME_MIN * 2 and bid_volume_near < ask_volume_near * 0.3:
                is_defense = True
                status = "HEAVY_CEILING"
                reason = f"Heavy Ceiling terdeteksi! Ask volume {ask_volume_near:.0f} - Harga ditahan"
        else:  # target_side == "LONG_LIQ" (target ke bawah)
            # Untuk ke bawah, kita perlu bid side tipis (hambatan kecil)
            if bid_volume_near < ODD_VOLUME_MIN and ask_volume_near > bid_volume_near * 3:
                is_thin = True
                status = "BID_THINNING"
                reason = f"Bid side tipis ({bid_volume_near:.0f}), Ask side tebal ({ask_volume_near:.0f}) - Jalan ke bawah terbuka"
            # Deteksi defense (bandar menahan harga)
            elif bid_volume_near > ODD_VOLUME_MIN * 2 and ask_volume_near < bid_volume_near * 0.3:
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
        if rsi6 < ABSORPTION_RSI_MAX and aggressive_ratio > 3.0 and abs(change_5m) < 0.5 and oi_delta_5m < 0:
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
            "fuel_ready": "YES" if abs(oi_delta) > 2.0 else "NO"
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
            if aggressive_ratio < 0.2 or trade_flow < 0.5:
                is_divergent = True
                action = "CANCEL_LONG"
                reason = f"BEARISH_DIVERGENCE: Mau Long, tapi Agresi {aggressive_ratio}x Bearish!"
            elif av_status == "BEARISH_ACCELERATION":
                is_divergent = True
                action = "CANCEL_LONG"
                reason = f"BEARISH_DIVERGENCE: Market Slam terdeteksi!"
        elif bias == "SHORT":
            if aggressive_ratio > 3.0 or trade_flow > 2.5:
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
            if short_dist < 1.0 and gravity_bias == "LONG" and aggressive_ratio < 0.3:
                signals.append(f"SILENT LOADING: Gravity EXTREME + Agg rendah")
                weight += 60
                final_bias = "LONG"
            elif long_dist < 1.0 and gravity_bias == "SHORT" and aggressive_ratio < 0.3:
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
        elif trade_flow > 2.0:
            flow_component = 1.0
        elif trade_flow < FLOW_EXTREME_SELL:
            flow_component = -2.0
        elif trade_flow < 0.5:
            flow_component = -1.0

        if rsi6 < RSI_FORBID_SHORT and flow_component < 0:
            flow_component = 0
        if rsi6 > RSI_FORBID_LONG and flow_component > 0:
            flow_component = 0

        aggressive_component = 0
        if aggressive_trades > 2.0:
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
        if aggressive < 0.1 and trade_flow < 0.3:
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
        elif bid_wall and trade_flow < 0.5:
            if oi_delta_5m > OI_ACCUMULATION_THRESHOLD:
                manipulation = "REAL_ACCUMULATION"
                bias = "LONG"
                reason = f"Bid wall + OI naik = REAL ACCUMULATION"
            else:
                manipulation = "SPOOF_SUPPORT"
                bias = "SHORT"
                reason = f"Bid wall detected tapi OI flat - fake support!"
        elif ask_wall and trade_flow > 2.0:
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

# ================= STATE MANAGER V80 =================
class StateManagerV80:
    """
    V80: Enhanced state manager dengan V80 modules (IER, RMG, FMV)
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
        self.ltg_history = deque(maxlen=10)  # V81 baru!
        self.icd_history = deque(maxlen=10)  # V81 baru!
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
        self.accumulation_flow_threshold = 2.0
        self.accumulation_duration_minutes = 0

        # Bid/Ask history untuk ODD
        self.bid_history = deque(maxlen=10)
        self.ask_history = deque(maxlen=10)

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
        if all(a < 0.1 for a in recent):
            return "NO_BUYERS"
        elif all(a > 2.0 for a in recent):
            return "AGGRESSIVE_BUY"
        elif all(a < 0.3 for a in recent):
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

# ================= MARKET STATE ENGINE V80 =================
class MarketStateEngineV80:
    """
    V80: Market phase dengan prioritas tertinggi (HIERARKI MUTLAK V80):
    0.0: EZH (Execution Zone Hunter) - ANTI-RIVER MAGNETIC SLINGSHOT (V78)
    0.1: WTD (Wash Trade Detector) - ANTI-KITE FALSE BRIDGE (V79)
    0.2: IER (Institutional Exit Radar) - ANTI-OPN/BARD FALSE FLOW (NEW V80!)
    0.3: RMG (RSI Momentum Guard) - ANTI-RIVER GRAVITY DECOY (NEW V80!)
    0.4: FMV (Fake Magnet Vacuum) - KOMBINASI IER + RMG (NEW V80!)
    0.5: PSV (Panic Sell Validator) - ANTI-OPN ENDLESS FLOOR (V78)
    0.6: OFF (Overdrive Flow Filter) - ANTI-HUSDT TRAP (V77)
    0.7: AEF (Aggressive Exhaustion Filter) - ANTI-PHA TRAP (V77)
    0.8: PSR (Panic Saturation Reversal) - ANTI-HUMA DRIFT TRAP (V76)
    0.9: AMV (Absorption Momentum Validator) - ANTI-HUMA TRAP (V75)
    0.10: LGO (Liquidation Gravity Overdrive) - ANTI-RIVER NUCLEAR (V75)
    0.11: MDV (Magnet Decay Validator) - ANTI-RIVER SPOOF (V74)
    0.12: PAB (Passive Absorption Blackhole) - ANTI-SIREN TRAP (V73)
    0.13: CFK (Catching Falling Knives) - ANTI-ROBO TRAP (V72)
    0.14: MDD (Magnet Distance Dominance) - ANTI-RIVER TRAP (V71)
    0.15: OVD (Orderbook Vacuum Defense) - ANTI-PHA TRAP (V70)
    0.16: TREND INTEGRITY (V69)
    0.17: OGD (Gravity Deflection) - ANTI-PIPPIN TRAP (V68)
    0.18: ZAS (Zero Aggression Slaughter) - ANTI-DEADSTICK (V67)
    0.19: AVC (Absorption Validity Check) - ANTI-EXIT LIQUIDITY TRAP (V67)
    0.20: AMD (Aggression-Mass Divergence) - ANTI-SPOOF (V65)
    0.21: TDP (The DYL Particle) - ABSOLUTE OVERRIDE (V64)
    0.22: ATI (Temporal Accumulation Index) - WHALE PATIENCE LOADING (V66)
    0.23: WED (Wall Erasure Detection) - FAKE FLOOR/CEILING (V63)
    0.24: MWR (Magnet Wall Reversal) (V62)
    0.25: LVS (Low-Volume Suction) (V61)
    0.26: DTD (Divergence Trap Detector) (V60)
    """
    @staticmethod
    def detect_state(data: Dict, state_mgr, liquidity_gravity, ppi, spoofing,
                    reversion, oi_velocity, hft_signature, lrr_result, av_result,
                    starter_result, ghost_result, dtd_result, lvs_result,
                    mwr_result, wed_result, tdp_result, amd_result, ati_result,
                    zas_result, avc_result, ogd_result, trend_result, ovd_result,
                    mdd_result, cfk_result, pab_result, mdv_result, amv_result, lgo_result,
                    psr_result, off_result, aef_result, ezh_result, psv_result,
                    wtd_result, ier_result, rmg_result, fmv_result, ltg_result, icd_result):  # V80 baru!
        rsi6 = safe_get(data, 'rsi6', 50)
        short_liq = safe_get(data, 'short_liq_dist', 99)
        long_liq = safe_get(data, 'long_liq_dist', 99)
        trade_flow = safe_get(data, 'trade_flow', 1.0)
        aggressive_ratio = safe_get(data, 'aggressive_ratio', 1.0)
        wmi_ratio = safe_get(data, 'wmi_ratio', 0)

        # ============================================
        # PRIORITAS BARU V81: LIQUIDITY THINNING GUARD (LTG)
        # ============================================
        if ltg_result['is_vacuum']:
            return {
                "phase": "LIQUIDITY_VACUUM",
                "bias": "LONG",
                "confidence": "ABSOLUTE",
                "reason": ltg_result['reason'],
                "multiplier": 30.0  # Prioritas tertinggi!
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
    def calculate(data: Dict, state_mgr: StateManagerV80) -> Dict:
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

# ================= CONFLICT RESOLVER V80 =================
class ConflictResolverV80:
    """
    V80: Resolve konflik dengan hierarki prioritas mutlak V80
    URUTAN PRIORITAS MUTLAK V80 (THE HIERARCHY OF INSTITUTIONAL DECEPTION):
        1. EZH (Execution Zone Hunter) - ANTI-RIVER MAGNETIC SLINGSHOT (V78)
        2. WTD (Wash Trade Detector) - ANTI-KITE FALSE BRIDGE (V79)
        3. IER (Institutional Exit Radar) - ANTI-OPN/BARD FALSE FLOW (NEW V80!)
        4. RMG (RSI Momentum Guard) - ANTI-RIVER GRAVITY DECOY (NEW V80!)
        5. FMV (Fake Magnet Vacuum) - KOMBINASI IER + RMG (NEW V80!)
        6. PSV (Panic Sell Validator) - ANTI-OPN ENDLESS FLOOR (V78)
        7. OFF (Overdrive Flow Filter) - ANTI-HUSDT TRAP (V77)
        8. AEF (Aggressive Exhaustion Filter) - ANTI-PHA TRAP (V77)
        9. PSR (Panic Saturation Reversal) - ANTI-HUMA DRIFT TRAP (V76)
        10. AMV (Absorption Momentum Validator) - ANTI-HUMA TRAP (V75)
        11. LGO (Liquidation Gravity Overdrive) - ANTI-RIVER NUCLEAR (V75)
        12. MDV (Magnet Decay Validator) - ANTI-RIVER SPOOF (V74)
        13. PAB (Passive Absorption Blackhole) - ANTI-SIREN TRAP (V73)
        14. CFK (Catching Falling Knives) - ANTI-ROBO TRAP (V72)
        15. MDD (Magnet Distance Dominance) - ANTI-RIVER TRAP (V71)
        16. OVD (Orderbook Vacuum Defense) - ANTI-PHA TRAP (V70)
        17. Trend Integrity (V69) - ANTI-PIPPIN/PHA/POWER
        18. Gravity Deflection (OGD) - ANTI-PIPPIN TRAP (V68)
        19. Zero Aggression Slaughter (ZAS) - ANTI-DEADSTICK (V67)
        20. Absorption Validity Check (AVC) - ANTI-EXIT LIQUIDITY TRAP (V67)
        21. Aggression-Mass Divergence (AMD) - ANTI-SPOOF PROTECTION (V65)
        22. The DYL Particle (TDP) - ABSOLUTE OVERRIDE (V64)
        23. Temporal Accumulation Index (ATI) - WHALE PATIENCE LOADING (V66)
        24. Wall Erasure Detection (WED) - GRAVITY MANDATE (V63)
        25. Magnet Wall Reversal (MWR) (V62)
        26. The Ghost Whisperer (LVS) (V61)
        27. The Absorption Shield (DTD) (V60)
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
                ltg_result: Dict = None, icd_result: Dict = None):  # V81 baru!
        # ============================================
        # PRIORITAS 0 (TERTINGGI): LIQUIDITY THINNING GUARD (V81)
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
        # PRIORITAS 1: INTERNAL CROSS DETECTOR (V81)
        # ============================================
        if icd_result and icd_result['is_internal_trap']:
            return {
                "bias": icd_result['bias'],
                "confidence": "ABSOLUTE",
                "reason": icd_result['reason'],
                "phase": "INTERNAL_CROSS_TRAP",
                "ttk_info": {"estimated_minutes": 1, "urgency": "IMMINENT", "fuel_ready": "YES"}
            }

        # ============================================
        # PRIORITAS 2: EXECUTION ZONE HUNTER (V78) - LANJUTAN EXISTING
        # ============================================
        # ... existing code ...
        # ============================================
        # PRIORITAS 1: EXECUTION ZONE HUNTER (V78) - ANTI-RIVER MAGNETIC SLINGSHOT
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
        # PRIORITAS 2: WASH TRADE DETECTOR (V79) - ANTI-KITE FALSE BRIDGE
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
        # PRIORITAS 3: INSTITUTIONAL EXIT RADAR (V80) - ANTI-OPN/BARD FALSE FLOW
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
        # PRIORITAS 4: RSI MOMENTUM GUARD (V80) - ANTI-RIVER GRAVITY DECOY
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
        # PRIORITAS 5: FAKE MAGNET VACUUM (V80) - KOMBINASI IER + RMG
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
        # PRIORITAS 6: PANIC SELL VALIDATOR (V78) - ANTI-OPN ENDLESS FLOOR
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
        # PRIORITAS 7: OVERDRIVE FLOW FILTER (V77) - ANTI-HUSDT TRAP
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
        # PRIORITAS 8: AGGRESSIVE EXHAUSTION FILTER (V77) - ANTI-PHA TRAP
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
        # PRIORITAS 9: PANIC SATURATION REVERSAL (V76) - ANTI-HUMA DRIFT TRAP
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
        # PRIORITAS 10: ABSORPTION MOMENTUM VALIDATOR (V75) - ANTI-HUMA TRAP
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
        # PRIORITAS 11: LIQUIDATION GRAVITY OVERDRIVE (V75) - ANTI-RIVER NUCLEAR
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
        # PRIORITAS 12: MAGNET DECAY VALIDATOR (V74) - ANTI-RIVER SPOOF
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
        # PRIORITAS 13: PASSIVE ABSORPTION BLACKHOLE (V73) - ANTI-SIREN TRAP
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
        # PRIORITAS 14: CATCHING FALLING KNIVES (V72) - ANTI-ROBO TRAP
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
        # PRIORITAS 15: MAGNET DISTANCE DOMINANCE (V71) - ANTI-RIVER TRAP
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
        # PRIORITAS 16: ORDERBOOK VACUUM DEFENSE (V70) - ANTI-PHA TRAP
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
        # PRIORITAS 17: TREND INTEGRITY (V69) - ANTI-PIPPIN/PHA/POWER
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
                if oi_delta_5m < 5.0:
                    return {
                        "bias": "SHORT",
                        "confidence": "SUPREME",
                        "reason": trend_result['reason'],
                        "phase": "MACD_DEAD_ZONE",
                        "ttk_info": {"estimated_minutes": 3, "urgency": "IMMINENT", "fuel_ready": "NO"}
                    }

        # ============================================
        # PRIORITAS 18: GRAVITY DEFLECTION (V68) - ANTI-PIPPIN TRAP
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
        # PRIORITAS 19: ZERO AGGRESSION SLAUGHTER (V67)
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
        # PRIORITAS 20: ABSORPTION VALIDITY CHECK (V67)
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
        # PRIORITAS 21: AGGRESSION-MASS DIVERGENCE (V65) - ANTI-SPOOF PROTECTION
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
        # PRIORITAS 22: THE DYL PARTICLE (V64) - ABSOLUTE OVERRIDE
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
        # PRIORITAS 23: TEMPORAL ACCUMULATION INDEX (V66) - ANTI-SAHARA TRAP
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
        # PRIORITAS 24: WALL ERASURE DETECTION (V63) - THE GRAVITY MANDATE
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
        # PRIORITAS 25: MAGNET WALL REVERSAL (V62)
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
        # PRIORITAS 26: THE GHOST WHISPERER (V61)
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
        # PRIORITAS 27: THE ABSORPTION SHIELD (V60)
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
        # PRIORITAS 28: THE VACUUM OVERRIDE
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
        # PRIORITAS 29: ANTI-SLAUGHTER RULE
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
        # PRIORITAS 30: THE SAFETY VALVE
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
            if pnr['bias'] == "LONG" and aggressive_ratio < 0.5:
                return {
                    "bias": "SHORT",
                    "confidence": "HIGH",
                    "reason": f"NO_FUEL_LONG: PNR Long dekat tapi Agresi {aggressive_ratio}x kering.",
                    "phase": "FAKE_BREAKOUT",
                    "ttk_info": ttk
                }
            if pnr['bias'] == "SHORT" and aggressive_ratio > 2.0:
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
        # PRIORITAS 31: GHOST INTENT DETECTOR
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
        # PRIORITAS 32: ENGINE STARTER
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
        # PRIORITAS 33: MAGNET RULE
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
        # PRIORITAS 34: GRAVITY SPOOF DETECTION
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
        # PRIORITAS 35: HFT SIGNATURE
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
        # PRIORITAS 36: OI CONFIRMATION
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
        # PRIORITAS 37: MEAN REVERSION
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
        # PRIORITAS 38: LIQUIDITY PATH
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

# ================= BINANCE ANALYZER V80 =================
class BinanceAnalyzerV80:
    """
    V80: Main analyzer dengan prioritas tertinggi:
        1. EZH (Execution Zone Hunter) - ANTI-RIVER MAGNETIC SLINGSHOT (V78)
        2. WTD (Wash Trade Detector) - ANTI-KITE FALSE BRIDGE (V79)
        3. IER (Institutional Exit Radar) - ANTI-OPN/BARD FALSE FLOW (NEW V80!)
        4. RMG (RSI Momentum Guard) - ANTI-RIVER GRAVITY DECOY (NEW V80!)
        5. FMV (Fake Magnet Vacuum) - KOMBINASI IER + RMG (NEW V80!)
        6. PSV (Panic Sell Validator) - ANTI-OPN ENDLESS FLOOR (V78)
        7. OFF (Overdrive Flow Filter) - ANTI-HUSDT TRAP (V77)
        dst...
    """
    def __init__(self, symbol: str):
        self.symbol = symbol.upper()
        self.fetcher = BinanceFetcher(symbol)
        self.state_mgr = StateManagerV80()
        self.market_state = MarketStateEngineV80()
        self.energy_calc = EnergyCalculatorV61()
        self.conflict_resolver = ConflictResolverV80()
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
        self.zas = ZeroAggressionSlaughterV67()
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
            # V81: Liquidity Thinning Guard
            ltg_result = self.ltg.analyze(
                trades['ratio'],
                ask_vol,
                bid_vol
            )
            # V81: Internal Cross Detector
            icd_result = self.icd.analyze(
                trades['ratio'],
                trades['aggressive_ratio'],
                oi_delta_5m
            )

            # Track persistence V81
            ltg_key = f"LTG_{trades['ratio']:.2f}"
            ltg_duration = self.state_mgr.track_ltg_persistence(ltg_key, time.time())
            icd_key = f"ICD_{trades['ratio']:.2f}_{trades['aggressive_ratio']:.2f}"
            icd_duration = self.state_mgr.track_icd_persistence(icd_key, time.time())
            # ====================================

            # WMI untuk Vacuum Override
            wmi_data = {
                'mass_ratio': wmi_ratio,
                'is_whale_trap': abs(wmi_ratio) > VACUUM_WMI_MIN,
                'dominant_side': "SHORT_LIQ_WHALE" if wmi_ratio > 0 else "LONG_LIQ_WHALE" if wmi_ratio < 0 else "NEUTRAL"
            }

            oi_velocity = self.oi_tracker.analyze(
                oi_now, oi_then or oi_now, change_5m, trades['ratio']
            )

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

            lvs_result = self.lvs.analyze(
                trades['aggressive_ratio'],
                trades['ratio'],
                change_5m,
                wmi_ratio
            )

            mwr_result = self.mwr.analyze(
                odd_result,
                rsi6,
                wmi_ratio,
                target_side
            )

            wed_result = self.wed.analyze(
                odd_result,
                wmi_ratio,
                rsi6,
                oi_delta_5m
            )

            tdp_result = self.tdp.analyze(
                oi_delta_5m,
                wmi_ratio,
                rsi6
            )

            amd_result = self.amd.analyze(
                wmi_ratio,
                trades['aggressive_ratio'],
                trades['ratio'],
                oi_delta_5m
            )

            ati_result = self.ati.analyze(
                trades['ratio'],
                rsi6,
                wmi_ratio,
                oi_delta_5m,
                accumulation_minutes / 60,
                self.state_mgr.get_flow_history()
            )

            zas_result = self.zas.analyze(
                trades['aggressive_ratio'],
                wmi_ratio,
                change_5m
            )

            avc_result = self.avc.analyze(
                trades['ratio'],
                trades['aggressive_ratio'],
                change_5m,
                oi_delta_5m
            )

            ogd_result = self.ogd.analyze(
                wmi_ratio,
                rsi6,
                liq['long_dist'] if wmi_ratio < 0 else liq['short_dist']
            )

            trend_result = self.trend.analyze(
                price,
                ma10,
                ma20,
                self.state_mgr.get_obv_history(),
                macd
            )

            ovd_result = self.ovd.analyze(
                odd_result,
                rsi6,
                trades['aggressive_ratio'],
                liq['short_dist'],
                liq['long_dist']
            )

            mdd_result = self.mdd.analyze(
                liq['short_dist'],
                liq['long_dist'],
                rsi6,
                trades['ratio']
            )

            cfk_result = self.cfk.analyze(
                wmi_ratio,
                rsi6,
                oi_delta_5m,
                trades['aggressive_ratio'],
                trades['ratio']
            )

            pab_result = self.pab.analyze(
                trades['ratio'],
                trades['aggressive_ratio'],
                rsi6,
                wmi_ratio,
                oi_delta_5m
            )

            mdv_result = self.mdv.analyze(
                mdd_result,
                amd_result,
                oi_delta_5m,
                self.state_mgr.magnet_first_seen.get(magnet_key, 0),
                time.time()
            )

            amv_result = self.amv.analyze(
                oi_delta_5m,
                trades['aggressive_ratio'],
                change_5m,
                trades['ratio']
            )

            lgo_result = self.lgo.analyze(
                liq['short_dist'],
                liq['long_dist'],
                rsi6,
                trades['ratio']
            )

            psr_result = self.psr.analyze(
                trades['aggressive_ratio'],
                price,
                ma10,
                ma20,
                rsi6,
                trades['ratio'],
                wmi_ratio
            )

            off_result = self.off.analyze(
                lgo_result,
                trades['ratio'],
                rsi6,
                trades['aggressive_ratio']
            )

            aef_result = self.aef.analyze(
                trades['aggressive_ratio'],
                rsi6,
                oi_delta_5m,
                liq['short_dist'],
                liq['long_dist'],
                trades['ratio']
            )

            # V78: EXECUTION ZONE HUNTER (EZH)
            ezh_result = self.ezh.analyze(
                liq['short_dist'],
                liq['long_dist'],
                rsi6,
                trades['ratio']
            )

            # V78: PANIC SELL VALIDATOR (PSV)
            psv_result = self.psv.analyze(
                rsi6,
                trades['ratio'],
                trades['aggressive_ratio'],
                oi_delta_5m
            )

            # V79: WASH TRADE DETECTOR (WTD)
            wtd_result = self.wtd.analyze(
                trades['ratio'],
                rsi6,
                oi_delta_5m
            )

            # V80: INSTITUTIONAL EXIT RADAR (IER)
            ier_result = self.ier.analyze(
                trades['ratio'],
                oi_delta_5m,
                trades['aggressive_ratio']
            )

            # V80: RSI MOMENTUM GUARD (RMG)
            rmg_result = self.rmg.analyze(
                rsi6,
                trades['aggressive_ratio'],
                liq['short_dist']
            )

            # V80: FAKE MAGNET VACUUM (FMV)
            fmv_result = self.fmv.analyze(
                ier_result,
                rmg_result,
                rsi6,
                trades['ratio'],
                oi_delta_5m,
                trades['aggressive_ratio'],
                liq['short_dist']
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
                zas_result, avc_result, ogd_result, trend_result, ovd_result,
                mdd_result, cfk_result, pab_result, mdv_result, amv_result, lgo_result,
                psr_result, off_result, aef_result, ezh_result, psv_result,
                wtd_result, ier_result, rmg_result, fmv_result,
                ltg_result, icd_result  # V81 baru!
            )

            liquidity_data = {
                "nearest": "SHORT" if liq['short_dist'] < liq['long_dist'] else "LONG",
                "short_dist": liq['short_dist'],
                "long_dist": liq['long_dist']
            }

            vbt_result = self.vbt.analyze(price, self.state_mgr.price_history, volume_ratio)

            final = self.conflict_resolver.resolve(
                market_phase, energy, mpe_result['bias'],
                trades['ratio'], liquidity_data, ppi,
                exhaustion, stop_hunt, ob_imprint,
                spoofing, reversion, oi_velocity,
                hft_signature, rsi6, change_5m, volume_ratio,
                funding['premium'], trades['aggressive_ratio'],
                liquidity_gravity['short_gravity'], liquidity_gravity['long_gravity'],
                liq['short_dist'], liq['long_dist'],
                liq['short_vol'], liq['long_vol'],
                price, self.state_mgr, data, odd_result, ghost_result,
                oi_5m_ago=oi_5m_ago_value,
                wmi=wmi_data,
                dtd_result=dtd_result,
                lvs_result=lvs_result,
                mwr_result=mwr_result,
                wed_result=wed_result,
                tdp_result=tdp_result,
                amd_result=amd_result,
                ati_result=ati_result,
                zas_result=zas_result,
                avc_result=avc_result,
                ogd_result=ogd_result,
                trend_result=trend_result,
                ovd_result=ovd_result,
                mdd_result=mdd_result,
                cfk_result=cfk_result,
                pab_result=pab_result,
                mdv_result=mdv_result,
                amv_result=amv_result,
                lgo_result=lgo_result,
                psr_result=psr_result,
                off_result=off_result,
                aef_result=aef_result,
                ezh_result=ezh_result,
                psv_result=psv_result,
                wtd_result=wtd_result,
                ier_result=ier_result,
                rmg_result=rmg_result,
                fmv_result=fmv_result,
                ltg_result=ltg_result,   # V81 baru!
                icd_result=icd_result     # V81 baru!
            )

            entry_ready = self.state_mgr.update_entry(final['bias'])
            if entry_ready and self.state_mgr.can_enter(final['bias'], market_phase['phase']):
                self.state_mgr.execute_entry(final['bias'], price, rsi6)
                entry_status = "✅ READY TO ENTRY!"
            else:
                entry_status = f"⏳ WAITING ({len(self.state_mgr.entry_signals)}/{CONFIRM_DEFAULT})"

            time_since_entry = self.state_mgr.time_since_entry()
            if time_since_entry < 5 and self.state_mgr.last_entry_bias != "NEUTRAL":
                hold_remaining = 5 - time_since_entry
                hold_status = f"🔒 HOLD LOCK: {hold_remaining:.1f}m remaining"
            else:
                hold_status = "🔓 HOLD FREE"

            ttk_info = final.get('ttk_info', {"estimated_minutes": 45, "urgency": "PREPARING", "fuel_ready": "NO"})

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
                "oi_current": round(oi_now, 2),
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
                # V81 New Modules (PRIORITAS TERTINGGI!)
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
                # V80 New Modules (PRIORITAS TERTINGGI 3-5)
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
                    "price_ma_diff": psr_result['price_ma_diff'],
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
                "zas": {
                    "is_dead": zas_result['is_dead'],
                    "bias": zas_result['bias'],
                    "reason": zas_result['reason'],
                    "confidence": zas_result['confidence']
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
                # Final Decision
                "bias": final['bias'],
                "confidence": final['confidence'],
                "reason": final['reason'],
                "entry_status": entry_status,
                "hold_status": hold_status,
                "entry_ready": entry_ready,
                "accumulation_detected": accumulation_detected
            }

            return result
        except Exception as e:
            print(f"❌ Error analyzing {self.symbol}: {e}")
            import traceback
            traceback.print_exc()
            return None

# ================= OUTPUT FORMATTER V80 =================
class OutputFormatterV80:
    """Format output untuk V80 dengan hierarki prioritas mutlak: LTG > ICD > EZH > WTD > IER > RMG > FMV > PSV ..."""
    @staticmethod
    def print_header():
        print("\n" + "="*80)
        print("🔥 BINANCE LIQUIDATION HUNTER V81 - THE LIQUIDITY QUANTUM")
        print("="*80)
        print("\n🧠 ANALISA FORENSIK V80 (KENAPA V80 MASIH KENA BANTAI?)")
        print("   📍 Kasus HUMAUSDT (The OI Absorption Trap):")
        print("      📊 Data: Flow 3.0x, Agg 1.86x, OI Δ +0.04%.")
        print("      📊 Masalah: Bot baca IER_EXIT (Whale cuci gudang). Tapi agresi retail (Agg 1.86x) SANGAT RENDAH dibanding Flow.")
        print("      📊 Kelicikan HFT: Whale beli dari Whale lain (Internal Cross) untuk memicu algoritma SHORT bot retail.")
        print("   📍 Kasus KITEUSDT (The Slingshot Overstretch):")
        print("      📊 Data: Flow 99.0x (Gila!), RSI 87.4, OI Δ -0.15%.")
        print("      📊 Masalah: Bot baca EZH & WTD. Tapi Flow 99.0x itu adalah 'Liquidity Vacuum'.")
        print("      📊 Kelicikan HFT: MM sengaja mengosongkan sisi ASK sehingga satu transaksi kecil bikin Flow terlihat ribuan persen.")
        print("\n🛡️ THE SUPREME OVERRIDE: V81 'THE LIQUIDITY QUANTUM'")
        print("   📍 NEW MODUL 1: LIQUIDITY THINNING GUARD (LTG) - ANTI-KITE VACUUM TRAP")
        print("      📍 'Jika Flow > 50.0x (Anomali Total), abaikan semua sinyal SHORT. Harga akan terus melayang (Infinity Squeeze).'")
        print("   📍 NEW MODUL 2: INTERNAL CROSS DETECTOR (ICD) - ANTI-HUMA POSITION FLIPPING")
        print("      📍 'Jika Flow > 2.0x TAPI Aggressive Ratio < 2.0x, Whale sedang Position Flipping! Abaikan sinyal SHORT dari IER!'")
        print("\n🎯 NEW HIERARKI MUTLAK V81 (Prioritas Baru):")
        print("   1. LTG (Liquidity Thinning Guard) - Jika Flow > 50x, paksa LONG (Infinity Squeeze)")
        print("   2. ICD (Internal Cross Detector) - Validasi apa IER beneran exit atau cuma sandiwara Whale")
        print("   3. EZH (Execution Zone Hunter) - ANTI-RIVER MAGNETIC SLINGSHOT")
        print("   4. WTD (Wash Trade Detector) - ANTI-KITE FALSE BRIDGE")
        print("   5. IER (Institutional Exit Radar) - ANTI-OPN/BARD FALSE FLOW")
        print("   6. RMG (RSI Momentum Guard) - ANTI-RIVER GRAVITY DECOY")
        print("   7. FMV (Fake Magnet Vacuum) - KOMBINASI IER + RMG")
        print("   8. PSV (Panic Sell Validator) - ANTI-OPN ENDLESS FLOOR")
        print("="*80 + "\n")
        print("🧠 KAIDAH EMAS V81: 'Jangan pernah nge-SHORT koin yang sisi atasnya kosong (Flow > 50x). MM nggak butuh bensin buat naik, mereka cuma butuh ketiadaan lawan.'\n")

    @staticmethod
    def print_signal(result: Dict):
        print("="*80)
        print(f"🔥 {result['symbol']} @ {result['timestamp']}")
        print(f"💰 Price: ${result['price']:.4f}")
        print("="*80)

        # PRIORITAS 1: LIQUIDITY THINNING GUARD (LTG) - V81
        if result['ltg']['is_vacuum']:
            print(f"\n💨💨💨 LIQUIDITY VACUUM DETECTED! KITE STYLE!")
            print(f"   📌 {result['ltg']['reason']}")
            print(f"   📊 Flow: {result['trade_flow']:.1f}x (ANOMALI!) | Ask Volume: {result.get('odd', {}).get('ask_volume_near', 0):.0f}")
            print(f"   📊 Sisi ASK kosong! Harga akan melayang tanpa hambatan (Infinity Squeeze)!")
            print(f"   ⏱️ LTG terdeteksi selama: {result['ltg']['ltg_duration_minutes']:.1f} menit")

        # PRIORITAS 2: INTERNAL CROSS DETECTOR (ICD) - V81
        elif result['icd']['is_internal_trap']:
            print(f"\n🔄🔄🔄 INTERNAL CROSS TRAP DETECTED! HUMA STYLE!")
            print(f"   📌 {result['icd']['reason']}")
            print(f"   📊 Flow: {result['trade_flow']:.1f}x (TINGGI!) | Agg: {result['aggressive_ratio']:.2f}x (RENDAH!)")
            print(f"   📊 Whale sedang Position Flipping! IER_EXIT adalah Jebakan!")
            print(f"   ⏱️ ICD terdeteksi selama: {result['icd']['icd_duration_minutes']:.1f} menit")

        # PRIORITAS 3: EXECUTION ZONE HUNTER (EZH)
        elif result['ezh']['is_execution'] and result['ezh']['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
            if result['ezh']['execution_type'] == "SHORT_EXECUTION_ZONE":
                print(f"\n🎯🎯🎯 MAGNETIC SLINGSHOT DETECTED! RIVER STYLE!")
                print(f"   📌 {result['ezh']['reason']}")
                print(f"   📊 Short Liq: {result['short_liq']}% (SUDAH TERSENTUH!) | RSI: {result['rsi6']}")
                print(f"   📊 MM sudah sapu likuidasi, siap-siap dump besar-besaran!")
                print(f"   ⏱️ EZH terdeteksi selama: {result['ezh']['ezh_duration_minutes']:.1f} menit")
            elif result['ezh']['execution_type'] == "LONG_EXECUTION_ZONE":
                print(f"\n🎯🎯🎯 EXECUTION REBOUND DETECTED!")
                print(f"   📌 {result['ezh']['reason']}")
                print(f"   📊 Long Liq: {result['long_liq']}% (SUDAH TERSENTUH!) | RSI: {result['rsi6']}")
                print(f"   📊 MM sudah sapu likuidasi bawah, siap-siap rebound besar!")

        # PRIORITAS 4: WASH TRADE DETECTOR (WTD)
        elif result['wtd']['is_wash_trade'] and result['wtd']['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
            if result['wtd']['wash_type'] == "WASH_TRADE_DISTRIBUTION":
                print(f"\n🎭🎭🎭 WASH TRADE DISTRIBUTION DETECTED! KITE STYLE!")
                print(f"   📌 {result['wtd']['reason']}")
                print(f"   📊 Flow: {result['trade_flow']:.1f}x (RAKSASA!) | RSI: {result['rsi6']} (TINGGI!)")
                print(f"   📊 Ini BUKAN akumulasi Whale asli, ini Jebakan Volume Palsu!")
                print(f"   ⏱️ WTD terdeteksi selama: {result['wtd']['wtd_duration_minutes']:.1f} menit")

        # PRIORITAS 5: INSTITUTIONAL EXIT RADAR (IER)
        elif result['ier']['is_exit'] and result['ier']['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
            if result['ier']['exit_type'] == "INSTITUTIONAL_EXIT":
                print(f"\n🏦🏦🏦 INSTITUTIONAL EXIT DETECTED! OPN/BARD STYLE!")
                print(f"   📌 {result['ier']['reason']}")
                print(f"   📊 Flow: {result['trade_flow']:.1f}x (TINGGI!) | OI Δ: {result['oi_delta_5m']:.2f}% (MAMPET!)")
                print(f"   📊 Whale sedang cuci gudang/exit ke retail! Magnet atas adalah jebakan!")
                print(f"   ⏱️ IER terdeteksi selama: {result['ier']['ier_duration_minutes']:.1f} menit")

        # PRIORITAS 6: RSI MOMENTUM GUARD (RMG)
        elif result['rmg']['is_weak'] and result['rmg']['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
            if result['rmg']['weakness_type'] == "GRAVITY_DECOY":
                print(f"\n🎣🎣🎣 GRAVITY DECOY DETECTED! RIVER STYLE!")
                print(f"   📌 {result['rmg']['reason']}")
                print(f"   📊 RSI: {result['rsi6']} (Neutral-High) | Agg: {result['aggressive_ratio']:.2f}x (RENDAH!)")
                print(f"   📊 Short Liq {result['short_liq']}% hanya umpan! Gak ada tenaga buat makan magnet atas.")
                print(f"   ⏱️ RMG terdeteksi selama: {result['rmg']['rmg_duration_minutes']:.1f} menit")

        # PRIORITAS 7: FAKE MAGNET VACUUM (FMV)
        elif result['fmv']['is_fake_magnet'] and result['fmv']['confidence'] in ["ABSOLUTE", "SUPREME"]:
            if result['fmv']['fake_type'] in ["FAKE_MAGNET_VACUUM_OPN", "FAKE_MAGNET_VACUUM_RIVER"]:
                print(f"\n🧲🧲🧲 FAKE MAGNET VACUUM DETECTED!")
                print(f"   📌 {result['fmv']['reason']}")
                print(f"   📊 Strategi kotor bandar: Menciptakan magnet sebagai Likuiditas Tiruan!")
                print(f"   📊 Binance sengaja tarik bot LONG masuk dengan umpan Magnet, sebelum banting harga!")
                print(f"   ⏱️ FMV terdeteksi selama: {result['fmv']['fmv_duration_minutes']:.1f} menit")

        # PRIORITAS 8: PANIC SELL VALIDATOR (PSV)
        elif result['psv']['is_valid'] and result['psv']['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"]:
            if result['psv']['validation_type'] == "FALLING_KNIFE_CONTINUATION":
                print(f"\n🔪🔪🔪 ENDLESS FLOOR DETECTED! OPN STYLE!")
                print(f"   📌 {result['psv']['reason']}")
                print(f"   📊 RSI: {result['rsi6']} (0.0!) | Flow: {result['trade_flow']:.2f}x (RENDAH!)")
                print(f"   📊 Whale gak nampung, ini FALLING KNIFE ASLI!")
                print(f"   ⏱️ PSV terdeteksi selama: {result['psv']['psv_duration_minutes']:.1f} menit")
            elif result['psv']['validation_type'] == "REAL_EXHAUSTION":
                print(f"\n🟢🟢🟢 TRUE BOTTOM DETECTED!")
                print(f"   📌 {result['psv']['reason']}")
                print(f"   📊 RSI: {result['rsi6']} (oversold) | Flow: {result['trade_flow']:.2f}x (WHALE NAMPUNG!)")

        # DECISION
        print(f"\n{'='*40}")
        bias_color = "🟢" if result['bias'] == "LONG" else "🔴" if result['bias'] == "SHORT" else "⚪"
        if result['confidence'] == "ABSOLUTE":
            conf_icon = "☢️☢️☢️"
        elif result['confidence'] == "SUPREME":
            conf_icon = "🔥🔥🔥"
        elif result['confidence'] == "HIGH":
            conf_icon = "🔥🔥"
        else:
            conf_icon = "🔥"

        print(f"{bias_color} FINAL BIAS: {result['bias']}")
        print(f"{conf_icon} CONFIDENCE: {result['confidence']}")
        print(f"📌 REASON: {result['reason']}")
        print(f"⏳ ENTRY: {result['entry_status']}")
        print(f"{result['hold_status']}")

        if result['entry_ready']:
            print(f"\n{'✅'*10} ENTRY READY! {'✅'*10}")

        # V81 Key Metrics (PRIORITAS TERTINGGI)
        print(f"\n{'='*40}")
        print("📊 V81 THE LIQUIDITY QUANTUM METRICS:")

        # LTG Status (Prioritas 1)
        if result['ltg']['is_vacuum']:
            print(f"💨 LTG Liquidity Vacuum: ACTIVE")
            print(f"   {result['ltg']['reason']}")
            print(f"   ⏱️ Durasi LTG: {result['ltg']['ltg_duration_minutes']:.1f}m")
        else:
            print(f"⚪ LTG Liquidity Vacuum: INACTIVE")

        # ICD Status (Prioritas 2)
        if result['icd']['is_internal_trap']:
            print(f"🔄 ICD Internal Cross: ACTIVE")
            print(f"   {result['icd']['reason']}")
            print(f"   ⏱️ Durasi ICD: {result['icd']['icd_duration_minutes']:.1f}m")
        else:
            print(f"⚪ ICD Internal Cross: INACTIVE")

        # V80 Key Metrics
        print(f"\n📊 V80 THE BLACK BOX DISMANTLER METRICS:")

        # IER Status (Prioritas 5)
        if result['ier']['is_exit']:
            ier_color = "🏦" if result['ier']['confidence'] in ["ABSOLUTE", "SUPREME"] else "⚠️"
            print(f"{ier_color} IER Institutional Exit: ACTIVE ({result['ier']['exit_type']})")
            print(f"   {result['ier']['reason']}")
            print(f"   Flow: {result['trade_flow']:.1f}x | OI Δ: {result['oi_delta_5m']:.2f}%")
            print(f"   ⏱️ Durasi IER: {result['ier']['ier_duration_minutes']:.1f}m")
        else:
            print(f"⚪ IER Institutional Exit: INACTIVE")

        # RMG Status (Prioritas 6)
        if result['rmg']['is_weak']:
            rmg_color = "🎣" if result['rmg']['confidence'] in ["ABSOLUTE", "SUPREME"] else "⚠️"
            print(f"{rmg_color} RMG Momentum Guard: ACTIVE ({result['rmg']['weakness_type']})")
            print(f"   {result['rmg']['reason']}")
            print(f"   RSI: {result['rsi6']} | Agg: {result['aggressive_ratio']:.2f}x")
            print(f"   ⏱️ Durasi RMG: {result['rmg']['rmg_duration_minutes']:.1f}m")
        else:
            print(f"⚪ RMG Momentum Guard: INACTIVE")

        # FMV Status (Prioritas 7)
        if result['fmv']['is_fake_magnet']:
            fmv_color = "🧲" if result['fmv']['confidence'] in ["ABSOLUTE", "SUPREME"] else "⚠️"
            print(f"{fmv_color} FMV Fake Magnet Vacuum: ACTIVE ({result['fmv']['fake_type']})")
            print(f"   {result['fmv']['reason']}")
            print(f"   ⏱️ Durasi FMV: {result['fmv']['fmv_duration_minutes']:.1f}m")
        else:
            print(f"⚪ FMV Fake Magnet Vacuum: INACTIVE")

        # EZH Status (Prioritas 3)
        if result['ezh']['is_execution']:
            ezh_color = "🎯" if result['ezh']['confidence'] in ["ABSOLUTE", "SUPREME"] else "⚠️"
            print(f"{ezh_color} EZH Execution Zone: ACTIVE ({result['ezh']['execution_type']})")
            print(f"   Short Liq: {result['short_liq']}% | Long Liq: {result['long_liq']}% | RSI: {result['rsi6']}")
            print(f"   ⏱️ Durasi EZH: {result['ezh']['ezh_duration_minutes']:.1f}m")

        # WTD Status (Prioritas 4)
        if result['wtd']['is_wash_trade']:
            wtd_color = "🎭" if result['wtd']['confidence'] in ["ABSOLUTE", "SUPREME"] else "⚠️"
            print(f"{wtd_color} WTD Wash Trade: ACTIVE ({result['wtd']['wash_type']})")
            print(f"   Flow: {result['trade_flow']:.1f}x | RSI: {result['rsi6']}")
            print(f"   ⏱️ Durasi WTD: {result['wtd']['wtd_duration_minutes']:.1f}m")

        # PSV Status (Prioritas 8)
        if result['psv']['is_valid']:
            psv_color = "🔪" if result['psv']['validation_type'] == "FALLING_KNIFE_CONTINUATION" else "🟢" if result['psv']['validation_type'] == "REAL_EXHAUSTION" else "⚠️"
            print(f"{psv_color} PSV Panic Validator: ACTIVE ({result['psv']['validation_type']})")
            print(f"   RSI: {result['rsi6']} | Flow: {result['trade_flow']:.2f}x")
            print(f"   ⏱️ Durasi PSV: {result['psv']['psv_duration_minutes']:.1f}m")

        # OFF Status
        if result['off']['is_patched']:
            off_color = "🌉" if result['off']['confidence'] in ["ABSOLUTE", "SUPREME"] else "⚠️"
            print(f"{off_color} OFF Overdrive Flow: ACTIVE ({result['off']['patched_type']})")
            print(f"   ⏱️ Durasi OFF: {result['off']['off_duration_minutes']:.1f}m")

        # AEF Status
        if result['aef']['is_exhausted']:
            aef_color = "💀" if result['aef']['confidence'] in ["ABSOLUTE", "SUPREME"] else "⚠️"
            print(f"{aef_color} AEF Aggressive Exhaustion: ACTIVE ({result['aef']['exhausted_type']})")
            print(f"   ⏱️ Durasi AEF: {result['aef']['aef_duration_minutes']:.1f}m")

        print(f"🐋 WMI: {result['wmi']['mass_ratio']:.1f}x ({result['wmi']['dominant_side']})")
        print(f"👻 Ghost Intent: {'ACTIVE' if result['ghost']['is_ghost'] else 'INACTIVE'} (Score: {result['ghost']['score']})")
        print(f"⏱️ TTK Countdown: {result['ttk']['estimated_minutes']}m ({result['ttk']['urgency']})")
        print(f"⛽ Fuel Ready: {result['ttk']['fuel_ready']}")

        print(f"\n📊 LIQUIDATION METRICS:")
        print(f"🎯 Short: +{result['short_liq']}% | Long: -{result['long_liq']}%")
        print(f"📊 Flow: {result['trade_flow']}x | Agg: {result['aggressive_ratio']}x")
        print(f"📈 RSI(6): {result['rsi6']}")
        print(f"📈 OI Δ5m: {result['oi_delta_5m']}%")

        print("="*80)

# ================= MAIN FUNCTION V81 =================
def main_v81():
    import sys
    if len(sys.argv) > 1:
        symbol = sys.argv[1].upper()
    else:
        symbol = input("\nSymbol (e.g. BTCUSDT): ").upper() or "BTCUSDT"

    # Buat SATU INSTANCE analyzer V80 untuk seluruh loop
    analyzer = BinanceAnalyzerV80(symbol)

    OutputFormatterV80.print_header()

    print(f"\n🔍 Analyzing {symbol} with V81 Quantum Logic...")

    result = analyzer.analyze()

    if result:
        OutputFormatterV80.print_signal(result)

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

def batch_mode_v81(symbols: List[str]):
    OutputFormatterV80.print_header()
    results = []
    analyzers = {}
    for symbol in symbols:
        analyzers[symbol] = BinanceAnalyzerV80(symbol)

    for symbol in symbols:
        print(f"\n🔍 Analyzing {symbol} with V81 Quantum Logic...")
        result = analyzers[symbol].analyze()
        if result:
            results.append(result)
            bias_icon = "🟢" if result['bias'] == "LONG" else "🔴" if result['bias'] == "SHORT" else "⚪"
            ready_icon = "✅" if result['entry_ready'] else "⏳"
            # Safety icons - V81 dengan hierarki baru
            ltg_icon = "💨" if result['ltg']['is_vacuum'] else " "
            icd_icon = "🔄" if result['icd']['is_internal_trap'] else " "
            ezh_icon = "🎯" if result['ezh']['is_execution'] and result['ezh']['confidence'] in ["ABSOLUTE", "SUPREME"] else " "
            wtd_icon = "🎭" if result['wtd']['is_wash_trade'] and result['wtd']['confidence'] in ["ABSOLUTE", "SUPREME"] else " "
            ier_icon = "🏦" if result['ier']['is_exit'] and result['ier']['confidence'] in ["ABSOLUTE", "SUPREME"] else " "
            rmg_icon = "🎣" if result['rmg']['is_weak'] and result['rmg']['confidence'] in ["ABSOLUTE", "SUPREME"] else " "
            fmv_icon = "🧲" if result['fmv']['is_fake_magnet'] and result['fmv']['confidence'] in ["ABSOLUTE", "SUPREME"] else " "
            psv_icon = "🔪" if result['psv']['is_valid'] and result['psv']['confidence'] in ["ABSOLUTE", "SUPREME"] else " "
            off_icon = "🌉" if result['off']['is_patched'] and result['off']['confidence'] in ["ABSOLUTE", "SUPREME"] else " "
            aef_icon = "💀" if result['aef']['is_exhausted'] and result['aef']['confidence'] in ["ABSOLUTE", "SUPREME"] else " "
            psr_icon = "⚖️" if result['psr']['is_saturated'] and result['psr']['confidence'] in ["SUPREME", "ABSOLUTE"] else " "
            amv_icon = "⚖️" if result['amv']['is_absorption_long'] and result['amv']['confidence'] in ["SUPREME", "HIGH"] else " "
            lgo_icon = "🚀" if result['lgo']['is_overdrive'] and result['lgo']['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"] else " "
            mdv_icon = "⚖️" if result['mdv']['is_magnet_fake'] and result['mdv']['confidence'] in ["SUPREME", "HIGH"] else " "
            pab_icon = "🕳️" if result['pab']['is_blackhole'] and result['pab']['confidence'] == "ABSOLUTE" else " "
            cfk_icon = "🔪" if result['cfk']['is_knife'] and result['cfk']['confidence'] == "SUPREME" else " "
            mdd_icon = "🧲" if result['mdd']['is_magnet_trap'] and result['mdd']['confidence'] == "SUPREME" else " "
            ovd_icon = "💨" if result['ovd']['is_trap'] and result['ovd']['confidence'] == "SUPREME" else " "
            ti_icon = "🛡️" if result['trend_integrity']['restriction'] != "NONE" else " "
            vacuum_icon = "💨" if result['wmi']['is_whale_trap'] and abs(result['wmi']['mass_ratio']) > VACUUM_WMI_MIN else " "
            ghost_icon = "👻" if result['ghost']['is_ghost'] else " "
            engine_icon = "🚀" if result['starter']['is_starting'] else " "
            print(f"{ready_icon}{ltg_icon}{icd_icon}{ezh_icon}{wtd_icon}{ier_icon}{rmg_icon}{fmv_icon}{psv_icon}{off_icon}{aef_icon}{psr_icon}{amv_icon}{lgo_icon}{mdv_icon}{pab_icon}{cfk_icon}{mdd_icon}{ovd_icon}{ti_icon}{vacuum_icon}{ghost_icon}{engine_icon} {bias_icon} {symbol}: {result['bias']} ({result['confidence']}) - {result['market_phase']} [TTK:{result['ttk']['estimated_minutes']}m]")
        else:
            print(f"❌ {symbol}: Failed")

    print("\n" + "="*80)
    print("📊 SUMMARY - READY TO ENTRY:")
    print("="*80)

    ready_count = 0
    for r in results:
        if r['entry_ready']:
            bias_icon = "🟢" if r['bias'] == "LONG" else "🔴"
            ltg_warn = "💨LTG! " if r['ltg']['is_vacuum'] else ""
            icd_warn = "🔄ICD! " if r['icd']['is_internal_trap'] else ""
            ezh_warn = "🎯EZH! " if r['ezh']['is_execution'] and r['ezh']['confidence'] in ["ABSOLUTE", "SUPREME"] else ""
            wtd_warn = "🎭WTD! " if r['wtd']['is_wash_trade'] and r['wtd']['confidence'] in ["ABSOLUTE", "SUPREME"] else ""
            ier_warn = "🏦IER! " if r['ier']['is_exit'] and r['ier']['confidence'] in ["ABSOLUTE", "SUPREME"] else ""
            rmg_warn = "🎣RMG! " if r['rmg']['is_weak'] and r['rmg']['confidence'] in ["ABSOLUTE", "SUPREME"] else ""
            fmv_warn = "🧲FMV! " if r['fmv']['is_fake_magnet'] and r['fmv']['confidence'] in ["ABSOLUTE", "SUPREME"] else ""
            psv_warn = "🔪PSV! " if r['psv']['is_valid'] and r['psv']['confidence'] in ["ABSOLUTE", "SUPREME"] else ""
            off_warn = "🌉OFF! " if r['off']['is_patched'] and r['off']['confidence'] in ["ABSOLUTE", "SUPREME"] else ""
            aef_warn = "💀AEF! " if r['aef']['is_exhausted'] and r['aef']['confidence'] in ["ABSOLUTE", "SUPREME"] else ""
            psr_warn = "⚖️PSR! " if r['psr']['is_saturated'] and r['psr']['confidence'] in ["SUPREME", "ABSOLUTE"] else ""
            amv_warn = "⚖️AMV! " if r['amv']['is_absorption_long'] and r['amv']['confidence'] in ["SUPREME", "HIGH"] else ""
            lgo_warn = "🚀LGO! " if r['lgo']['is_overdrive'] and r['lgo']['confidence'] in ["ABSOLUTE", "SUPREME", "HIGH"] else ""
            mdv_warn = "⚖️MDV! " if r['mdv']['is_magnet_fake'] and r['mdv']['confidence'] in ["SUPREME", "HIGH"] else ""
            pab_warn = "🕳️PAB! " if r['pab']['is_blackhole'] and r['pab']['confidence'] == "ABSOLUTE" else ""
            cfk_warn = "🔪CFK! " if r['cfk']['is_knife'] and r['cfk']['confidence'] == "SUPREME" else ""
            mdd_warn = "🧲MDD! " if r['mdd']['is_magnet_trap'] and r['mdd']['confidence'] == "SUPREME" else ""
            ovd_warn = "💨OVD! " if r['ovd']['is_trap'] and r['ovd']['confidence'] == "SUPREME" else ""
            ti_warn = "🛡️TREND! " if r['trend_integrity']['restriction'] != "NONE" else ""
            vacuum_warn = "💨VACUUM! " if r['wmi']['is_whale_trap'] and abs(r['wmi']['mass_ratio']) > VACUUM_WMI_MIN else ""
            ghost_warn = "👻GHOST! " if r['ghost']['is_ghost'] else ""
            engine_warn = "🚀ENGINE! " if r['starter']['is_starting'] else ""
            print(f"{bias_icon} {r['symbol']}: {r['bias']} ({r['confidence']}) - {ltg_warn}{icd_warn}{ezh_warn}{wtd_warn}{ier_warn}{rmg_warn}{fmv_warn}{psv_warn}{off_warn}{aef_warn}{psr_warn}{amv_warn}{lgo_warn}{mdv_warn}{pab_warn}{cfk_warn}{mdd_warn}{ovd_warn}{ti_warn}{vacuum_warn}{ghost_warn}{engine_warn}{r['reason'][:60]} | TTK:{r['ttk']['estimated_minutes']}m")
            ready_count += 1

    if ready_count == 0:
        print("No entry-ready signals at this moment")

    return results

def api_mode_v81(symbol: str) -> str:
    analyzer = BinanceAnalyzerV80(symbol)
    result = analyzer.analyze()
    if result:
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

POPULAR_SYMBOLS = [
    "BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT", "DOGEUSDT",
    "RIVERUSDT", "SIRENUSDT", "POWERUSDT", "BEATUSDT", "PIPPINUSDT",
    "KITEUSDT", "JTOUSDT", "CYBERUSDT", "BERAUSDT", "ORCAUSDT", "ARCUSDT",
    "ALICEUSDT", "DUSKUSDT", "LINAUSDT", "STMXUSDT", "LYNUSDT", "SAHARAUSDT",
    "ROBOUSDT", "PHAUSDT", "HUMAUSDT", "HUSDT", "OPNUSDT", "BARDUSDT"
]

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "--api":
            symbol = sys.argv[2] if len(sys.argv) > 2 else "BTCUSDT"
            print(api_mode_v81(symbol))
        elif sys.argv[1] == "--batch":
            symbols = sys.argv[2:] if len(sys.argv) > 2 else POPULAR_SYMBOLS
            batch_mode_v81(symbols)
        elif sys.argv[1] == "--help":
            print("""
🔥 Binance Liquidation Hunter V81 - The Liquidity Quantum
Usage:
python script.py SYMBOL           # Analyze single symbol
python script.py SYMBOL --loop     # Auto-refresh every 10s
python script.py --batch [SYMBOLS] # Analyze multiple symbols
python script.py --api SYMBOL      # JSON output for API
python script.py --help            # Show this help

Examples:
python script.py BTCUSDT
python script.py KITEUSDT --loop   # Test LTG (Liquidity Thinning Guard) - V81 baru!
python script.py HUMAUSDT --loop   # Test ICD (Internal Cross Detector) - V81 baru!

New Features V81 (The Liquidity Quantum):
💨 LIQUIDITY THINNING GUARD (LTG): Deteksi Liquidity Vacuum!
    - Kasus KITE: Flow 99.0x (Anomali) karena sisi ASK kosong
    - Logic: Jika Flow > 50x, itu Liquidity Vacuum! JANGAN SHORT! HARGA AKAN MELAYANG!

    🔄 INTERNAL CROSS DETECTOR (ICD): Deteksi Position Flipping!
    - Kasus HUMA: Flow tinggi tapi Agg rendah, Whale trap bot SHORT
    - Logic: Jika Flow > 2.0x TAPI Agg < 2.0x, itu Internal Cross! IER_EXIT ADALAH Jebakan!

🎯 NEW HIERARKI MUTLAK V81 (Prioritas Baru):
    1. LTG (Liquidity Thinning Guard) - Jika Flow > 50x, paksa LONG (Infinity Squeeze)
    2. ICD (Internal Cross Detector) - Validasi IER_EXIT
    3. EZH (Execution Zone Hunter) - ANTI-RIVER MAGNETIC SLINGSHOT
    4. WTD (Wash Trade Detector) - ANTI-KITE FALSE BRIDGE
    5. IER (Institutional Exit Radar) - ANTI-OPN/BARD FALSE FLOW
    6. RMG (RSI Momentum Guard) - ANTI-RIVER GRAVITY DECOY
    7. FMV (Fake Magnet Vacuum) - KOMBINASI IER + RMG
    8. PSV (Panic Sell Validator) - ANTI-OPN ENDLESS FLOOR

🧠 KAIDAH EMAS V81:
"Jangan pernah nge-SHORT koin yang sisi atasnya kosong (Flow > 50x). 
    MM nggak butuh bensin buat naik, mereka cuma butuh ketiadaan lawan."
            """)
        else:
            main_v81()
    else:
        main_v81()
