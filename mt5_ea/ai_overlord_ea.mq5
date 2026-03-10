#property strict

#include "config/ai_settings.mqh"

// AI ENGINE
#include "core/ai_engine/market_reader/market_reader.mqh"
#include "core/ai_engine/neural_decision/neural_core.mqh"
#include "core/ai_engine/neural_decision/neural_loader.mqh"

#include "core/ai_engine/protection_system/equity_guard.mqh"
#include "core/ai_engine/protection_system/profit_lock.mqh"
#include "core/ai_engine/protection_system/layer_control.mqh"

#include "core/ai_engine/mining_scalping_mode/micro_scalping.mqh"
#include "core/ai_engine/mining_scalping_mode/trade_frequency_ai.mqh"

#include "learning/trade_memory.mqh"
#include "learning/performance_analyzer.mqh"

//------------------------------------
// GLOBAL VARIABLES
//------------------------------------

double lotSize;

//------------------------------------
// INIT
//------------------------------------

int OnInit()
{

   Print("AI Overlord EA Started");

   LoadNeuralWeights();

   return(INIT_SUCCEEDED);

}

//------------------------------------
// MAIN LOOP
//------------------------------------

void OnTick()
{

   if(!MarketHealthy())
      return;

   if(!EquitySafe())
      return;

   if(!ProfitProtected())
      return;

   if(!CanOpenLayer())
      return;

   if(!ScalpingAllowed())
      return;

   if(!CanTradeNow())
      return;

   int decision = AIDecision();

   lotSize = CalculateMicroLot();

   if(decision == 1)
      OpenBuy();

   if(decision == -1)
      OpenSell();

}

//------------------------------------
// BUY FUNCTION
//------------------------------------

void OpenBuy()
{

   double price = SymbolInfoDouble(_Symbol,SYMBOL_ASK);

   MqlTradeRequest req;
   MqlTradeResult res;

   ZeroMemory(req);

   req.action = TRADE_ACTION_DEAL;
   req.symbol = _Symbol;
   req.volume = lotSize;
   req.type = ORDER_TYPE_BUY;
   req.price = price;
   req.deviation = 10;

   OrderSend(req,res);

   Print("BUY executed");

}

//------------------------------------
// SELL FUNCTION
//------------------------------------

void OpenSell()
{

   double price = SymbolInfoDouble(_Symbol,SYMBOL_BID);

   MqlTradeRequest req;
   MqlTradeResult res;

   ZeroMemory(req);

   req.action = TRADE_ACTION_DEAL;
   req.symbol = _Symbol;
   req.volume = lotSize;
   req.type = ORDER_TYPE_SELL;
   req.price = price;
   req.deviation = 10;

   OrderSend(req,res);

   Print("SELL executed");

}
