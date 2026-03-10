#!/usr/bin/env python3
"""
🔥 BINANCE LIQUIDATION HUNTER V87 - THE LIQUIDITY PATHFINDER (GHOST IN THE SHELL EDITION)
💀 Modul Baru: Zero Aggression Squeeze, Liquidity Compression, Liquidity Bait, 
    Liquidity Imbalance Momentum, Stealth Accumulation Detector

🧠 Kaidah Pamungkas V87:
    "Agg = 0 TIDAK SELALU berarti weak momentum. Itu artinya SELLER EXHAUSTION!"
    "Market maker selalu mengikuti path of least resistance - largest liquidity pool, bukan nearest!"
    "Liquidity Compression terjadi 1-12 jam sebelum move 5-10% - jangan tertipu sideway!"
    "Time-Decay Psychology: Retail cuma tahan 1-2 jam, Whale pakai 9-11 jam fatigue trap!"
"""
from typing import Dict, Optional

# ================= V87 CONFIG =================
# Zero Aggression Squeeze (ZAS) Config
ZAS_AGG_MAX = 0.0                    # Max Aggression untuk Zero Aggression
ZAS_FLOW_MAX = 1.5                   # Max Flow untuk seller exhaustion
ZAS_RSI_MIN = 20                     # Min RSI untuk neutral zone
ZAS_RSI_MAX = 65                     # Max RSI untuk neutral zone

# Liquidity Compression Detector (LCD) Config
LCD_AGG_MAX = 0.05                   # Max Aggression untuk compression
LCD_FLOW_MAX = 1.2                   # Max Flow untuk compression
LCD_OI_DELTA_MAX = 1.0               # Max |OI Delta| untuk compression
LCD_RSI_MIN = 20                     # Min RSI untuk compression
LCD_RSI_MAX = 65                     # Max RSI untuk compression

# Liquidity Bait Detector (LBD) Config
LBD_SHORT_DIST_MAX = 0.5             # Max short distance untuk bait (<0.5%)
LBD_FLOW_MAX = 1.0                   # Max Flow untuk bait
LBD_AGG_MAX = 1.0                    # Max Aggression untuk bait
LBD_OI_DELTA_MAX = 1.0               # Max |OI Delta| untuk bait

# Stealth Accumulation Detector (SAD) Config
SAD_AGG_MAX = 0.1                    # Max Aggression untuk stealth
SAD_CHANGE_MAX = 0.1                 # Max price change untuk stealth
SAD_WMI_MIN = 20                     # Min WMI untuk short liq target
SAD_OI_DELTA_MAX = 0.0               # Max OI Delta (harus turun)


# ================= V87: ZERO AGGRESSION SQUEEZE (ZAS) =================
class ZeroAggressionSqueezeV87:
    """
    V87: Mendeteksi 'Zero Aggression Squeeze' - kondisi ketika tidak ada aggressive seller
    
    KASUS POWERUSDT & ROBOUSDT:
        Data: Agg 0.00x, Flow 0.33-1.17x, RSI 26-54, OI flat/turun sedikit
        Bot V86 memilih: RMG_WEAK_MOMENTUM → SHORT (Karena Agg 0.00x = weak momentum)
        Tapi market: PUMP +4% sampai +8% setelah 9-11 jam!
        
        🧠 Error Utama: Bot menganggap Agg 0.00x = weak momentum/dump
        Masalahnya: Agg 0.00x = TIDAK ADA AGGRESSIVE SELLER (seller exhaustion)!
        
        🔬 Interpretasi Sebenarnya:
        - Agg = 0 artinya seller sudah habis
        - Market maker sedang freeze orderbook untuk akumulasi
        - Pattern: Liquidity Freeze → Liquidity Build (30-120 menit) → Squeeze (+4-8%)
        
        ⚡ RULE ZAS:
            - Jika Agg == 0 AND Flow < 1.5 AND RSI 20-65 → bias = LONG
            - Ini adalah Seller Exhaustion - tidak ada seller left!
    """
    
    @staticmethod
    def analyze(agg_ratio: float, flow: float, rsi: float, oi_delta: float = None) -> Dict:
        """
        Args:
            agg_ratio: Aggressive Ratio (0.00x = zero aggression)
            flow: Trade Flow ratio (< 1.5 = low volume)
            rsi: RSI 6 period (20-65 = neutral zone)
            oi_delta: OI Delta 5m (optional, untuk konfirmasi)
        
        Returns:
            Dict dengan is_squeeze, bias, reason, confidence
        """
        is_squeeze = False
        bias = "NEUTRAL"
        reason = "Normal conditions"
        confidence = "LOW"
        
        # Cek Zero Aggression condition
        if (
            agg_ratio <= ZAS_AGG_MAX and
            flow < ZAS_FLOW_MAX and
            ZAS_RSI_MIN < rsi < ZAS_RSI_MAX
        ):
            is_squeeze = True
            bias = "LONG"  # DILARANG SHORT! Ini squeeze setup!
            confidence = "SUPREME"
            
            oi_info = ""
            if oi_delta is not None:
                if oi_delta < 0:
                    oi_info = f" OI Δ {oi_delta:.2f}% (short covering via limit). "
                elif oi_delta > 0:
                    oi_info = f" OI Δ +{oi_delta:.2f}% (new positions building). "
                else:
                    oi_info = " OI flat (positions stable). "
            
            reason = (
                f"ZAS_ZERO_AGGRESSION: Agg {agg_ratio}x (NO SELLERS LEFT!) + "
                f"Flow {flow:.2f}x (seller exhaustion) + "
                f"RSI {rsi:.1f} (neutral zone{oi_info})"
                f"→ Market Maker sedang freeze orderbook untuk akumulasi. "
                f"Squeeze +4-8% incoming setelah 30-120 menit liquidity build!"
            )
        
        return {
            "is_squeeze": is_squeeze,
            "bias": bias,
            "reason": reason,
            "confidence": confidence,
            "phase": "LIQUIDITY_FREEZE" if is_squeeze else "NORMAL"
        }


# ================= V87: LIQUIDITY COMPRESSION DETECTOR (LCD) =================
class LiquidityCompressionDetectorV87:
    """
    V87: Mendeteksi 'Liquidity Compression' - market dikompres sebelum eksplosi besar
    
    STRUKTUR LIQUIDITY COMPRESSION:
        - Price → flat/sideway
        - OI → sedikit turun/flat
        - Flow → kecil (<1.2)
        - Agg → hampir 0 (≤0.05)
        - RSI → netral (20-65)
        
    Market terlihat seperti dead market, padahal:
        - Liquidity sedang dikompres
        - Terjadi 1-12 jam sebelum move 5-12%
        - Market maker mematikan agresi untuk stop volatility
    
    SEQUENCE MANIPULASI:
        Phase 1 — Liquidity Compression: Agg↓, Flow↓, Price flat
        Phase 2 — Position Build: Retail short/close position, OI flat/turun
        Phase 3 — Expansion: Market buy burst, move +5% sampai +12%
    
    ⚡ RULE LCD:
        - Jika Agg ≤ 0.05 AND Flow < 1.2 AND |OI| < 1 AND RSI 20-65 → bias = LONG
        - Ini adalah Liquidity Compression sebelum expansion!
    """
    
    @staticmethod
    def analyze(agg_ratio: float, flow: float, oi_delta: float, rsi: float) -> Dict:
        """
        Args:
            agg_ratio: Aggressive Ratio (≤0.05 = compressed)
            flow: Trade Flow ratio (<1.2 = low)
            oi_delta: OI Delta 5m (|Δ| < 1 = flat/stable)
            rsi: RSI 6 period (20-65 = neutral)
        
        Returns:
            Dict dengan is_compression, bias, reason, confidence
        """
        is_compression = False
        bias = "NEUTRAL"
        reason = "Normal conditions"
        confidence = "LOW"
        
        # Cek Liquidity Compression condition
        if (
            agg_ratio <= LCD_AGG_MAX and
            flow < LCD_FLOW_MAX and
            abs(oi_delta) < LCD_OI_DELTA_MAX and
            LCD_RSI_MIN < rsi < LCD_RSI_MAX
        ):
            is_compression = True
            bias = "LONG"  # Bias long karena compression biasanya precede pump
            confidence = "HIGH"
            
            reason = (
                f"LCD_LIQUIDITY_COMPRESSION: Agg {agg_ratio}x (frozen) + "
                f"Flow {flow:.2f}x (low) + "
                f"OI Δ {oi_delta:.2f}% (flat/compressed) + "
                f"RSI {rsi:.1f} (neutral) "
                f"→ Market sedang dikompres 1-12 jam sebelum eksplosi +5-12%! "
                f"Market maker mematikan agresi untuk build liquidity!"
            )
        
        return {
            "is_compression": is_compression,
            "bias": bias,
            "reason": reason,
            "confidence": confidence,
            "phase": "COMPRESSION_ZONE" if is_compression else "NORMAL"
        }


# ================= V87: LIQUIDITY BAIT DETECTOR (LBD) =================
class LiquidityBaitDetectorV87:
    """
    V87: Mendeteksi 'Liquidity Bait' - magnet palsu untuk memancing bot
    
    CARA BINANCE MEMANCING BOT:
        Market maker sengaja membuat kondisi:
        - Short liq 0.3-0.5% (sangat dekat)
        - Long liq 3-4% (jauh tapi besar)
        
        Bot liquidation membaca: target = short liq (karena jarak dekat)
        HFT menghitung: expected_reward = liquidity_size / distance
        - Short liq: 2M / 0.4% = 5M reward density
        - Long liq: 20M / 4% = 5M reward density TAPI lebih besar total!
        
        Jadi HFT akan: pump sedikit → build more longs → baru dump 5-12%
    
    SEQUENCE LIQUIDITY BAIT:
        Phase 1 — Magnet Creation: Short liq sangat dekat (<0.5%)
        Phase 2 — Liquidity Farming: MM tidak sentuh magnet, buat range
        Phase 3 — Real Target: Setelah long liquidity cukup, dump 5-12%
    
    4 TANDA LIQUIDITY BAIT:
        1️⃣ Distance terlalu dekat: liq < 0.5%
        2️⃣ Flow rendah: flow < 1.0 (tidak ada dorongan nyata)
        3️⃣ Aggression rendah: Agg < 1.0 (tidak ada aggressive buyer)
        4️⃣ OI tidak turun: OI flat (bukan liquidation event)
    
    ⚡ RULE LBD:
        - Jika short_dist < 0.5 AND Flow < 1.0 AND Agg < 1.0 AND |OI| < 1 → bias = SHORT (tapi JANGAN ENTRY!)
        - Ini adalah Fake Magnet - MM akan pump dulu baru dump!
    """
    
    @staticmethod
    def analyze(
        short_dist: float,
        long_dist: float,
        flow: float,
        agg_ratio: float,
        oi_delta: float
    ) -> Dict:
        """
        Args:
            short_dist: Distance to short liquidation (%)
            long_dist: Distance to long liquidation (%)
            flow: Trade Flow ratio
            agg_ratio: Aggressive Ratio
            oi_delta: OI Delta 5m
        
        Returns:
            Dict dengan is_bait, bias, reason, confidence
        """
        is_bait = False
        bias = "NEUTRAL"
        reason = "Normal conditions"
        confidence = "LOW"
        
        # Cek Liquidity Bait condition
        if (
            short_dist < LBD_SHORT_DIST_MAX and
            flow < LBD_FLOW_MAX and
            agg_ratio < LBD_AGG_MAX and
            abs(oi_delta) < LBD_OI_DELTA_MAX
        ):
            is_bait = True
            bias = "SHORT"  # Tapi JANGAN ENTRY! Ini warning saja
            confidence = "HIGH"
            
            reason = (
                f"LBD_LIQUIDITY_BAIT: Short Liq {short_dist:.2f}% (TERLALU DEKAT!) + "
                f"Flow {flow:.2f}x (no momentum) + "
                f"Agg {agg_ratio:.2f}x (no aggression) + "
                f"OI Δ {oi_delta:.2f}% (not liquidation) "
                f"→ Ini FAKE MAGNET! Jangan short! "
                f"MM akan pump dulu untuk build long liquidity, baru dump 5-12%!"
            )
        
        return {
            "is_bait": is_bait,
            "bias": bias,
            "reason": reason,
            "confidence": confidence,
            "phase": "BAIT_ZONE" if is_bait else "NORMAL",
            "warning": "DO NOT ENTRY - WAIT FOR REAL SWEEP" if is_bait else ""
        }


# ================= V87: LIQUIDITY IMBALANCE MOMENTUM (LIM) =================
class LiquidityImbalanceMomentumV87:
    """
    V87: Mengukur imbalance momentum untuk menentukan arah sweep yang benar
    
    FORMULA HFT:
        LIM = (liquidation_density × position_build_rate) / resistance
        
        Disederhanakan:
        LIM = (OI velocity × liquidation gradient) / aggression resistance
    
    KENAPA INI PENTING:
        Liquidation sweep terjadi ketika imbalance momentum terbentuk.
        
        Contoh:
        - Short liq = 2M, distance = 0.5%
        - Long liq = 20M, distance = 4%
        
        Bot biasa: target = short liq (jarak dekat)
        HFT: long_score >> short_score → target = long liq (lebih besar!)
    
    3 KOMPONEN LIM:
        1️⃣ Liquidation Gradient: size / distance
        2️⃣ OI Velocity: OI delta per second (position build speed)
        3️⃣ Aggression Resistance: agg > 2 = high resistance, agg < 1 = low resistance
    
    ⚡ RULE LIM:
        - long_score = long_gradient * max(oi_velocity, 0.1) / max(agg, 0.1)
        - short_score = short_gradient * max(oi_velocity, 0.1) / max(agg, 0.1)
        - Jika long_score > short_score → bias = LONG (Short liq imbalance building)
        - Jika short_score > long_score → bias = SHORT (Long liq imbalance building)
    """
    
    @staticmethod
    def analyze(
        short_gradient: float,
        long_gradient: float,
        oi_velocity: float,
        agg_ratio: float
    ) -> Dict:
        """
        Args:
            short_gradient: Short liquidation gradient (size/distance)
            long_gradient: Long liquidation gradient (size/distance)
            oi_velocity: OI velocity (delta per second, use 5m delta / 300)
            agg_ratio: Aggressive Ratio (resistance factor)
        
        Returns:
            Dict dengan long_score, short_score, bias, reason
        """
        # Hitung scores dengan protection dari division by zero
        safe_oi_vel = max(abs(oi_velocity), 0.1)
        safe_agg = max(agg_ratio, 0.1)
        
        long_score = long_gradient * safe_oi_vel / safe_agg
        short_score = short_gradient * safe_oi_vel / safe_agg
        
        # Tentukan bias berdasarkan score comparison
        if long_score > short_score * 1.2:  # 20% threshold untuk significance
            bias = "LONG"
            reason = (
                f"LIM_LONG_IMBALANCE: Long Score {long_score:.2f} >> Short Score {short_score:.2f} | "
                f"Long gradient {long_gradient:.2f} vs Short gradient {short_gradient:.2f} | "
                f"OI Velocity {oi_velocity:.4f}/s | Agg Resistance {agg_ratio:.2f}x | "
                f"→ Short liquidation imbalance building → Price akan NAIK sapu short liq!"
            )
        elif short_score > long_score * 1.2:
            bias = "SHORT"
            reason = (
                f"LIM_SHORT_IMBALANCE: Short Score {short_score:.2f} >> Long Score {long_score:.2f} | "
                f"Short gradient {short_gradient:.2f} vs Long gradient {long_gradient:.2f} | "
                f"OI Velocity {oi_velocity:.4f}/s | Agg Resistance {agg_ratio:.2f}x | "
                f"→ Long liquidation imbalance building → Price akan TURUN sapu long liq!"
            )
        else:
            bias = "NEUTRAL"
            reason = (
                f"LIM_BALANCED: Long Score {long_score:.2f} ≈ Short Score {short_score:.2f} | "
                f"No clear imbalance → Wait for clearer signal"
            )
        
        return {
            "long_score": long_score,
            "short_score": short_score,
            "bias": bias,
            "reason": reason,
            "imbalance_ratio": max(long_score, short_score) / max(min(long_score, short_score), 0.01),
            "phase": "IMBALANCE_BUILDING" if bias != "NEUTRAL" else "BALANCED"
        }


# ================= V87: STEALTH ACCUMULATION DETECTOR (SAD) =================
class StealthAccumulationDetectorV87:
    """
    V87: Mendeteksi 'Stealth Accumulation' - Whale beli diam-diam via Limit Order
    
    KASUS POWER & ROBO:
        Data: Agg 0.00x (gak ada buyer agresif), Harga stabil (Change < 0.1%),
              OI turun tipis (-0.9%), WMI positif (Short Liq di atas)
        Bot V86 ke-trigger: EXIT_LIQUIDITY_TRAP → SHORT (Karena Agg 0.00x)
        Tapi market: Sideway 9-11 jam → BOOM +4-8%!
    
    🧠 KRIMINALITAS BINANCE:
        The Aggression Ghosting:
            - Whale TIDAK pasang market buy (biar Agg tetap 0)
            - Whale pasang LIMIT BUY segunung (invisible di orderbook)
            - Hasil: Agg 0.00x tapi harga nggak turun!
        
        The 9-Hour Fatigue Trap:
            - Mereka sideway-in harga 9-11 jam
            - Psikologi retail: cuma tahan 1-2 jam
            - Lewat dari itu: panic close atau nambah Short karena "gak turun-turun"
            - Begitu retail Short numpuk: TEMBAK KE ATAS!
    
    WMI BAIT:
        - Di POWER: WMI 43.7x (Short Liq di atas)
        - Jarak Short Liq cuma 0.41%
        - Bot ngira MM bakal dump dulu
        - Padahal dengan WMI positif, target MM itu DI ATAS!
    
    KAIDAH EMAS V87:
        "Jika Aggression 0.00 tapi OI turun, itu bukan Whale kabur, 
         itu Whale sedang nutup Short (Short Covering). JANGAN SHORT, lo bakal kena squeeze!"
    
    ⚡ RULE SAD:
        - Jika Agg < 0.1 AND |change_5m| < 0.1 AND WMI > 20 AND OI turun → bias = LONG
        - Ini adalah Whale Short Covering via Limit Order (bukan exit!)
    """
    
    @staticmethod
    def analyze(
        agg_ratio: float,
        change_5m: float,
        oi_delta: float,
        wmi: float
    ) -> Dict:
        """
        Args:
            agg_ratio: Aggressive Ratio (<0.1 = stealth mode)
            change_5m: Price change 5m (|Δ| < 0.1% = frozen)
            oi_delta: OI Delta 5m (<0 = short covering)
            wmi: WMI Ratio (>20 = short liq target above)
        
        Returns:
            Dict dengan is_stealth, bias, reason, confidence
        """
        is_stealth = False
        bias = "NEUTRAL"
        reason = "Normal conditions"
        confidence = "LOW"
        
        # Cek Stealth Accumulation condition
        if (
            agg_ratio < SAD_AGG_MAX and
            abs(change_5m) < SAD_CHANGE_MAX and
            wmi > SAD_WMI_MIN and
            oi_delta < SAD_OI_DELTA_MAX
        ):
            is_stealth = True
            bias = "LONG"  # DILARANG SHORT! Ini stealth accumulation!
            confidence = "SUPREME"
            
            reason = (
                f"SAD_STEALTH_ACCUMULATION: Agg {agg_ratio}x (GHOST MODE!) + "
                f"Price Change {change_5m:.2f}% (frozen) + "
                f"WMI {wmi:.1f}x (short liq target above) + "
                f"OI Δ {oi_delta:.2f}% (short covering via limit) "
                f"→ Whale sedang Short Covering diam-diam via Limit Buy! "
                f"Ini BUKAN Exit Trap, ini SPRING LOADING! "
                f"Fatigue Trap 9-11 jam sebelum BOOM +4-8%!"
            )
        
        return {
            "is_stealth": is_stealth,
            "bias": bias,
            "reason": reason,
            "confidence": confidence,
            "phase": "STEALTH_PUMP_LOADING" if is_stealth else "NORMAL"
        }


# ================= V87: CONFLICT RESOLVER HIERARCHY =================
class ConflictResolverV87:
    """
    V87: Resolve konflik dengan hierarki prioritas mutlak V87
    
    URUTAN PRIORITAS MUTLAK V87 (THE GHOST IN THE SHELL HIERARCHY):
        0. SAD (Stealth Accumulation Detector) - ANTI-POWER/ROBO GHOSTING ⭐ TERTINGGI!
        1. ZAS (Zero Aggression Squeeze) - ANTI-SELLER EXHAUSTION TRAP ⭐
        2. LCD (Liquidity Compression Detector) - ANTI-SIDEWAY FATIGUE TRAP ⭐
        3. LBD (Liquidity Bait Detector) - ANTI-FAKE MAGNET ⭐
        4. LIM (Liquidity Imbalance Momentum) - ANTI-WRONG TARGET ⭐
        5. ODF (Overbought Distribution Filter) - ANTI-TRIA TRAP (V86)
        6. ZGH (Zero Gravity Horizon) - ANTI-TRIA TRAP (V86)
        7. OTF (Oversold Trap Filter) - ANTI-UAI & LIQUIDITY VACUUM REBOUND (V85)
        ... (lanjutan hierarchy V86)
    """
    
    @staticmethod
    def resolve(
        sad_result: Dict,
        zas_result: Dict,
        lcd_result: Dict,
        lbd_result: Dict,
        lim_result: Dict,
        odf_result: Dict = None,
        zgh_result: Dict = None,
        otf_result: Dict = None,
        **kwargs
    ) -> Dict:
        """
        Resolve konflik dengan prioritas V87
        
        Returns:
            Dict final decision dengan bias, confidence, reason
        """
        
        # ============================================
        # 🟢 PRIORITAS 0 (TERTINGGI): V87 STEALTH ACCUMULATION DETECTOR
        # ANTI-POWER/ROBO GHOSTING - Whale beli diam-diam!
        # ============================================
        if sad_result and sad_result.get('is_stealth'):
            return {
                "bias": "LONG",
                "confidence": "SUPREME",
                "reason": f"V87_SAD_STEALTH_ACCUMULATION: {sad_result['reason']}",
                "phase": "STEALTH_PUMP_LOADING",
                "ttk_info": {"estimated_minutes": 540, "urgency": "PATIENCE_REQUIRED", "fuel_ready": "LOADING"}
            }
        
        # ============================================
        # 🟢 PRIORITAS 1: V87 ZERO AGGRESSION SQUEEZE
        # ANTI-SELLER EXHAUSTION - Tidak ada seller left!
        # ============================================
        if zas_result and zas_result.get('is_squeeze'):
            return {
                "bias": "LONG",
                "confidence": "SUPREME",
                "reason": f"V87_ZAS_ZERO_AGGRESSION: {zas_result['reason']}",
                "phase": "LIQUIDITY_FREEZE",
                "ttk_info": {"estimated_minutes": 90, "urgency": "BUILDING", "fuel_ready": "PREPARING"}
            }
        
        # ============================================
        # 🟢 PRIORITAS 2: V87 LIQUIDITY COMPRESSION
        # ANTI-SIDEWAY FATIGUE - Market dikompres sebelum eksplosi!
        # ============================================
        if lcd_result and lcd_result.get('is_compression'):
            return {
                "bias": "LONG",
                "confidence": "HIGH",
                "reason": f"V87_LCD_LIQUIDITY_COMPRESSION: {lcd_result['reason']}",
                "phase": "COMPRESSION_ZONE",
                "ttk_info": {"estimated_minutes": 360, "urgency": "COMPRESSING", "fuel_ready": "BUILDING"}
            }
        
        # ============================================
        # 🟡 PRIORITAS 3: V87 LIQUIDITY BAIT (WARNING ONLY)
        # ANTI-FAKE MAGNET - Jangan entry, tunggu real sweep!
        # ============================================
        if lbd_result and lbd_result.get('is_bait'):
            # Return NEUTRAL dengan warning - jangan entry!
            return {
                "bias": "NEUTRAL",
                "confidence": "HIGH",
                "reason": f"V87_LBD_LIQUIDITY_BAIT: {lbd_result['reason']} (WAIT FOR REAL SWEEP!)",
                "phase": "BAIT_ZONE",
                "warning": "DO NOT ENTRY - FAKE MAGNET DETECTED",
                "ttk_info": {"estimated_minutes": 0, "urgency": "WAIT", "fuel_ready": "NO"}
            }
        
        # ============================================
        # 🟡 PRIORITAS 4: V87 LIQUIDITY IMBALANCE MOMENTUM
        # ANTI-WRONG TARGET - Ikuti imbalance yang benar!
        # ============================================
        if lim_result and lim_result.get('bias') != 'NEUTRAL':
            imbalance_ratio = lim_result.get('imbalance_ratio', 1.0)
            confidence = "HIGH" if imbalance_ratio > 2.0 else "MEDIUM"
            
            return {
                "bias": lim_result['bias'],
                "confidence": confidence,
                "reason": f"V87_LIM_IMBALANCE: {lim_result['reason']}",
                "phase": lim_result.get('phase', 'IMBALANCE_BUILDING'),
                "ttk_info": {"estimated_minutes": 30, "urgency": "BUILDING", "fuel_ready": "YES" if imbalance_ratio > 2.0 else "NO"}
            }
        
        # ============================================
        # FALLBACK KE V86 MODULES (jika tersedia)
        # ============================================
        if odf_result and odf_result.get('active'):
            return {
                "bias": odf_result['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V86_ODF_OVERBOUGHT_DISTRIBUTION: {odf_result['reason']}",
                "phase": "ZERO_GRAVITY_HORIZON"
            }
        
        if zgh_result and zgh_result.get('is_ceiling'):
            return {
                "bias": zgh_result['bias'],
                "confidence": zgh_result['confidence'],
                "reason": f"V86_ZGH_ZERO_GRAVITY: {zgh_result['reason']}",
                "phase": "DISTRIBUTION_TOP"
            }
        
        if otf_result and otf_result.get('is_trap'):
            return {
                "bias": otf_result['bias'],
                "confidence": "ABSOLUTE",
                "reason": f"V85_OTF_OVERSOLD_TRAP: {otf_result['reason']}",
                "phase": "ANTI_LIQUIDITY_TRAP"
            }
        
        # Default: No clear signal
        return {
            "bias": "NEUTRAL",
            "confidence": "LOW",
            "reason": "No V87/V86 signature detected - Wait for clearer signal",
            "phase": "NORMAL"
        }


# ================= OUTPUT FORMAT V87 =================
class OutputFormatterV87:
    """Format output untuk V87 dengan prioritas tertinggi SAD (Stealth Accumulation Detector)"""
    
    @staticmethod
    def print_header():
        print("\n" + "="*80)
        print("🔥 BINANCE LIQUIDATION HUNTER V87 - THE LIQUIDITY PATHFINDER (GHOST IN THE SHELL EDITION)")
        print("="*80)
        print("\n🧠 ANALISA KEGAGALAN V86 (Kenapa Bot Salah Arah?)")
        print("   📍 Kasus POWERUSDT & ROBOUSDT (The Zero Aggression Trap):")
        print("      📊 Data: Agg 0.00x, Flow 0.33-1.17x, RSI 26-54, OI flat/turun")
        print("      📊 Bot V86 memilih: RMG_WEAK_MOMENTUM → SHORT")
        print("      📊 Tapi market: PUMP +4-8% setelah 9-11 jam!")
        print("      ")
        print("      🧠 Error Utama: Zero Aggression Bias")
        print("      Masalahnya: Agg 0.00x = SELLER EXHAUSTION, bukan weak momentum!")
        print("      ")
        print("      🔬 Clue yang Bot Lewatkan:")
        print("      - Agg 0.00x = TIDAK ADA AGGRESSIVE SELLER")
        print("      - Flow < 1.5 = seller exhaustion")
        print("      - RSI 20-65 = neutral zone")
        print("      - OI flat/turun = short covering via limit")
        print("      ")
        print("      ⚡ Signal Penting:")
        print("      - Agg == 0 AND Flow < 1.5 AND RSI 20-65 = ZERO AGGRESSION SQUEEZE")
        print("      - Ini adalah Liquidity Compression sebelum eksplosi +5-12%!")
        print("\n🛡️ THE SUPREME REFINEMENT: V87 MODULES")
        print("   📍 SAD (Stealth Accumulation Detector) - ANTI-POWER/ROBO GHOSTING ⭐")
        print("   📍 ZAS (Zero Aggression Squeeze) - ANTI-SELLER EXHAUSTION ⭐")
        print("   📍 LCD (Liquidity Compression Detector) - ANTI-SIDEWAY FATIGUE ⭐")
        print("   📍 LBD (Liquidity Bait Detector) - ANTI-FAKE MAGNET ⭐")
        print("   📍 LIM (Liquidity Imbalance Momentum) - ANTI-WRONG TARGET ⭐")
        print("\n🎯 HIERARKI MUTLAK V87:")
        print("   0. SAD → 1. ZAS → 2. LCD → 3. LBD → 4. LIM → 5. ODF (V86) → ...")
        print("="*80 + "\n")
        print("🧠 KAIDAH EMAS V87:")
        print("   'Agg = 0 TIDAK SELALU berarti weak momentum. Itu artinya SELLER EXHAUSTION!'")
        print("   'Market maker selalu mengikuti largest liquidity pool, bukan nearest!'")
        print("   'Liquidity Compression terjadi 1-12 jam sebelum move 5-10%!'")
        print("   'Time-Decay Psychology: Retail 1-2 jam, Whale 9-11 jam fatigue trap!'\\n")
    
    @staticmethod
    def format_signal(symbol: str, result: Dict) -> str:
        """Format signal untuk API output"""
        output = {
            "symbol": symbol,
            "timestamp": result.get('timestamp', ''),
            "bias": result.get('bias', 'NEUTRAL'),
            "confidence": result.get('confidence', 'LOW'),
            "reason": result.get('reason', ''),
            "phase": result.get('phase', 'NORMAL'),
            "v87_modules": {
                "sad": result.get('sad', {}),
                "zas": result.get('zas', {}),
                "lcd": result.get('lcd', {}),
                "lbd": result.get('lbd', {}),
                "lim": result.get('lim', {})
            },
            "ttk_info": result.get('ttk_info', {}),
            "entry_status": "READY" if result.get('confidence') in ['SUPREME', 'ABSOLUTE', 'HIGH'] else "WAIT",
            "hold_status": "HOLD POSITION" if result.get('confidence') in ['SUPREME', 'ABSOLUTE'] else "NO POSITION"
        }
        return output


# ================= MAIN TESTING FUNCTION =================
def test_v87_modules():
    """Test semua modul V87 dengan data contoh"""
    
    print("\n" + "="*80)
    print("🧪 TESTING V87 MODULES")
    print("="*80)
    
    # Test Case 1: POWERUSDT Style (Zero Aggression)
    print("\n📊 TEST CASE 1: POWERUSDT Style (Zero Aggression Squeeze)")
    print("-"*60)
    zas_result = ZeroAggressionSqueezeV87.analyze(
        agg_ratio=0.0,
        flow=0.33,
        rsi=54,
        oi_delta=0.10
    )
    print(f"Result: {zas_result}")
    
    # Test Case 2: ROBOUSDT Style (Stealth Accumulation)
    print("\n📊 TEST CASE 2: ROBOUSDT Style (Stealth Accumulation)")
    print("-"*60)
    sad_result = StealthAccumulationDetectorV87.analyze(
        agg_ratio=0.0,
        change_5m=0.05,
        oi_delta=-0.92,
        wmi=43.7
    )
    print(f"Result: {sad_result}")
    
    # Test Case 3: Liquidity Compression
    print("\n📊 TEST CASE 3: Liquidity Compression")
    print("-"*60)
    lcd_result = LiquidityCompressionDetectorV87.analyze(
        agg_ratio=0.02,
        flow=0.8,
        oi_delta=0.3,
        rsi=45
    )
    print(f"Result: {lcd_result}")
    
    # Test Case 4: Liquidity Bait
    print("\n📊 TEST CASE 4: Liquidity Bait (Fake Magnet)")
    print("-"*60)
    lbd_result = LiquidityBaitDetectorV87.analyze(
        short_dist=0.41,
        long_dist=4.0,
        flow=0.7,
        agg_ratio=0.5,
        oi_delta=0.2
    )
    print(f"Result: {lbd_result}")
    
    # Test Case 5: Liquidity Imbalance
    print("\n📊 TEST CASE 5: Liquidity Imbalance Momentum")
    print("-"*60)
    lim_result = LiquidityImbalanceMomentumV87.analyze(
        short_gradient=5.0,  # 2M / 0.4%
        long_gradient=5.0,   # 20M / 4%
        oi_velocity=0.005,
        agg_ratio=0.8
    )
    print(f"Result: {lim_result}")
    
    # Test Conflict Resolver
    print("\n📊 TEST CASE 6: Conflict Resolver V87")
    print("-"*60)
    resolver_result = ConflictResolverV87.resolve(
        sad_result=sad_result,
        zas_result=zas_result,
        lcd_result=lcd_result,
        lbd_result=lbd_result,
        lim_result=lim_result
    )
    print(f"Final Decision: {resolver_result}")
    
    print("\n" + "="*80)
    print("✅ V87 MODULES TEST COMPLETED")
    print("="*80 + "\n")


if __name__ == "__main__":
    test_v87_modules()
