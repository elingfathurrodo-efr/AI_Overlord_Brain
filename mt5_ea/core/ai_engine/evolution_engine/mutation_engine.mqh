#ifndef MUTATION_ENGINE
#define MUTATION_ENGINE

#include "genome_manager.mqh"

double MutateValue(double value)
{

   double mutation = (MathRand() % 10) / 100.0;

   if(MathRand() % 2 == 0)
      value += mutation;
   else
      value -= mutation;

   if(value < 0) value = 0;
   if(value > 1) value = 1;

   return(value);

}

void MutateGenome()
{

   activeGenome.rsi_weight = MutateValue(activeGenome.rsi_weight);
   activeGenome.ema_weight = MutateValue(activeGenome.ema_weight);
   activeGenome.macd_weight = MutateValue(activeGenome.macd_weight);
   activeGenome.breakout_weight = MutateValue(activeGenome.breakout_weight);
   activeGenome.mean_weight = MutateValue(activeGenome.mean_weight);

}

#endif
