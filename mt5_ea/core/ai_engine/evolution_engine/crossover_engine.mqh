#ifndef CROSSOVER_ENGINE
#define CROSSOVER_ENGINE

#include "genome_manager.mqh"

Genome Crossover(Genome g1, Genome g2)
{

   Genome child;

   child.rsi_weight = (g1.rsi_weight + g2.rsi_weight)/2;
   child.ema_weight = (g1.ema_weight + g2.ema_weight)/2;
   child.macd_weight = (g1.macd_weight + g2.macd_weight)/2;
   child.breakout_weight = (g1.breakout_weight + g2.breakout_weight)/2;
   child.mean_weight = (g1.mean_weight + g2.mean_weight)/2;

   return(child);

}

#endif
