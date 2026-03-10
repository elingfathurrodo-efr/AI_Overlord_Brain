//+------------------------------------------------------------------+
//| AI Overlord EA                                                   |
//| Core Execution Engine                                            |
//+------------------------------------------------------------------+
#property strict

#include "config/ai_settings.mqh"

int OnInit()
{
   Print("AI Overlord EA Started");
   return(INIT_SUCCEEDED);
}

void OnTick()
{
   // Market reading
   ReadMarket();

   // Strategy decision
   EvaluateStrategy();

   // Execute trade
   ExecuteTrade();

   // Protection system
   RunProtection();
}
