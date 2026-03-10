#ifndef AI_SETTINGS
#define AI_SETTINGS

//+------------------------------------------------------------------+
//| AI OVERLORD SETTINGS                                            |
//| Global configuration for EA                                     |
//+------------------------------------------------------------------+

// ================================
// LOT SETTINGS
// ================================

input double BaseLot = 0.01;
input double MaxLot  = 1.0;

// ================================
// LAYER CONTROL
// ================================

input int MaxLayers = 5;
input bool RequireNewCandleForLayer = true;

// ================================
// SPREAD PROTECTION
// ================================

input double MaxSpread = 30;

// ================================
// VOLATILITY FILTER
// ================================

input bool UseATRFilter = true;
input int ATR_Period = 14;
input double ATR_Minimum = 5;

// ================================
// AI CONTROL
// ================================

input bool EnableAI = true;
input bool EnableEvolution = true;
input bool EnablePatternRecognition = true;

// ================================
// PROTECTION SYSTEM
// ================================

input bool EnableEquityGuard = true;
input bool EnableProfitLock = true;
input bool EnableGhostTrailing = true;
input bool EnableTebasPucuk = true;

// ================================
// PROFIT LOCK SETTINGS
// ================================

input double ProfitLockStart = 2.0; // equity multiplier
input double ProfitLockRatio = 0.20;

// ================================
// EQUITY PROTECTION
// ================================

input double MaxDrawdownPercent = 30.0;

// ================================
// TRADING SESSION CONTROL
// ================================

input bool UseSessionFilter = true;

input bool TradeAsia   = true;
input bool TradeLondon = true;
input bool TradeNewYork= true;

// ================================
// SCALPING MODE
// ================================

input bool EnableMiningMode = true;
input int  ScalpingFrequency = 5;

// ================================
// AI EVOLUTION SETTINGS
// ================================

input int EvolutionCycleMinutes = 10;

#endif
