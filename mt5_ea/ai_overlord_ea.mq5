//+------------------------------------------------------------------+
//| AI OVERLORD EA                                                   |
//| Autonomous AI Trading System                                     |
//| Core Execution Engine                                            |
//+------------------------------------------------------------------+
#property strict
#property version   "1.00"

// Config
#include "config/ai_settings.mqh"

// Market reader
#include "core/ai_engine/market_reader/market_reader.mqh"

// Strategy loader
#include "core/ai_engine/strategy_library/ema_strategy.mqh"

// Protection system
#include "core/ai_engine/protection_system/equity_guard.mqh"

//-------------------------------------------------------------------
// GLOBAL VARIABLES
//-------------------------------------------------------------------

double CurrentSpread;
double CurrentATR;

bool AllowTrading=true;

//-------------------------------------------------------------------
// INITIALIZATION
//-------------------------------------------------------------------

int OnInit()
{
   Print("AI Overlord EA Initialized");

   InitializeSystem();

   return(INIT_SUCCEEDED);
}

//-------------------------------------------------------------------
// DEINITIALIZATION
//-------------------------------------------------------------------

void OnDeinit(const int reason)
{
   Print("AI Overlord EA Shutdown");
}

//-------------------------------------------------------------------
// MAIN TICK
//-------------------------------------------------------------------

void OnTick()
{

   // STEP 1 - Read Market
   UpdateMarketData();

   // STEP 2 - Protection Check
   if(!CheckProtection())
      return;

   // STEP 3 - Strategy Decision
   int signal = EvaluateStrategy();

   // STEP 4 - Execute Trade
   ExecuteTrade(signal);

}

//-------------------------------------------------------------------
// SYSTEM INITIALIZATION
//-------------------------------------------------------------------

void InitializeSystem()
{

   Print("Initializing AI Engine...");

}

//-------------------------------------------------------------------
// MARKET UPDATE
//-------------------------------------------------------------------

void UpdateMarketData()
{

   CurrentSpread = GetSpread();
   CurrentATR    = GetATR();

}

//-------------------------------------------------------------------
// STRATEGY EVALUATION
//-------------------------------------------------------------------

int EvaluateStrategy()
{

   int signal = 0;

   signal = EMA_Strategy();

   return(signal);

}

//-------------------------------------------------------------------
// TRADE EXECUTION
//-------------------------------------------------------------------

void ExecuteTrade(int signal)
{

   if(signal==1)
      OpenBuy();

   if(signal==-1)
      OpenSell();

}

//-------------------------------------------------------------------
// BUY ORDER
//-------------------------------------------------------------------

void OpenBuy()
{

   double price = SymbolInfoDouble(_Symbol,SYMBOL_ASK);

   MqlTradeRequest request;
   MqlTradeResult result;

   ZeroMemory(request);
   ZeroMemory(result);

   request.action   = TRADE_ACTION_DEAL;
   request.symbol   = _Symbol;
   request.volume   = BaseLot;
   request.type     = ORDER_TYPE_BUY;
   request.price    = price;
   request.deviation= 20;

   OrderSend(request,result);

}

//-------------------------------------------------------------------
// SELL ORDER
//-------------------------------------------------------------------

void OpenSell()
{

   double price = SymbolInfoDouble(_Symbol,SYMBOL_BID);

   MqlTradeRequest request;
   MqlTradeResult result;

   ZeroMemory(request);
   ZeroMemory(result);

   request.action   = TRADE_ACTION_DEAL;
   request.symbol   = _Symbol;
   request.volume   = BaseLot;
   request.type     = ORDER_TYPE_SELL;
   request.price    = price;
   request.deviation= 20;

   OrderSend(request,result);

}

//-------------------------------------------------------------------
// PROTECTION CHECK
//-------------------------------------------------------------------

bool CheckProtection()
{

   if(!EquityGuard())
      return(false);

   return(true);

}

//+------------------------------------------------------------------+
