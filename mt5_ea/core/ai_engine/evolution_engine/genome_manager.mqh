#ifndef GENOME_MANAGER
#define GENOME_MANAGER

struct Genome
{
   double rsi_weight;
   double ema_weight;
   double macd_weight;
   double breakout_weight;
   double mean_weight;
};

Genome activeGenome;

void InitializeGenome()
{

   activeGenome.rsi_weight = 0.25;
   activeGenome.ema_weight = 0.25;
   activeGenome.macd_weight = 0.25;
   activeGenome.breakout_weight = 0.15;
   activeGenome.mean_weight = 0.10;

}

Genome GetGenome()
{
   return(activeGenome);
}

#endif
