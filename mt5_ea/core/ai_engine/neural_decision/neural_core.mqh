#ifndef NEURAL_CORE
#define NEURAL_CORE

#include "neural_weights.mqh"
#include "neural_signals.mqh"

double CalculateAIScore()
{

   double score = 0;

   score += Signal_RSI() * weight_rsi;
   score += Signal_EMA() * weight_ema;
   score += Signal_MACD() * weight_macd;
   score += Signal_Breakout() * weight_breakout;
   score += Signal_Mean() * weight_mean;

   return(score);

}

int AIDecision()
{

   double score = CalculateAIScore();

   if(score > 0.3)
      return(1); // BUY

   if(score < -0.3)
      return(-1); // SELL

   return(0); // HOLD

}

#endif
