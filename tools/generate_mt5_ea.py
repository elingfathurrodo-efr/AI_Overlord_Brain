import os

ea = """
// AI GENERATED EA
#include <Trade/Trade.mqh>
CTrade trade;

void OnTick()
{
   Print("AI EA running");
}
"""

os.makedirs("mt5_ea", exist_ok=True)

with open("mt5_ea/AI_TRADER.mq5","w") as f:
    f.write(ea)

print("EA generated")
