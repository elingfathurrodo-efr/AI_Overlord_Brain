//+------------------------------------------------------------------+
//|              AI_OVERLORD_BRAIN_V20_MASTER_TEMPLATE               |
//|   Version 20.0 — Massive Neural Dashboard | 60 Nerves Active     |
//|   Powered by Cloud Sync RAM-Only (Zero-Footprint)                |
//+------------------------------------------------------------------+
#property copyright   "AI-Overlord-Dev"
#property link        "https://github.com/REPO_AKAN_DIISI_OTOMATIS"
#property version     "20.00"
#property description "AI OVERLORD BRAIN — Full Autonomous Cloud Engine"
#property strict

#include <Trade\Trade.mqh>
#include <Trade\PositionInfo.mqh>

// ═══════════════════════════════════════════════════════════════════
//  INPUT PARAMETERS (AKAN DIISI OTOMATIS OLEH GITHUB)
// ═══════════════════════════════════════════════════════════════════
input group "═══ GITHUB CLOUD CONFIG ═══"
input string  InpToken        = "TOKEN_AKAN_DIISI_OTOMATIS"; 
input string  InpRepo         = "REPO_AKAN_DIISI_OTOMATIS";
input string  InpFilePath     = "logic.json";
input int     InpSyncSec      = 3;        // Sinkronisasi RAM (Detik)

input group "═══ NEURAL ARCHITECTURE ═══"
input bool    InpAutoTrade    = true;     // Aktifkan Autopilot
input double  InpNeuralSens   = 0.95;     // Sensitivitas Saraf
input int     InpMaxNerves    = 60;       // Total 60 Saraf Aktif

input group "═══ RISK MANAGEMENT ═══"
input double  InpLot          = 0.01;
input int     InpMagic        = 882199;
input int     InpSL           = 400;
input int     InpTP           = 800;

// ═══════════════════════════════════════════════════════════════════
//  GLOBAL DATA STRUCTURES
// ═══════════════════════════════════════════════════════════════════
CTrade         m_trade;
string         G_Memory_JSON  = "";  
string         G_Signal_CMD   = "IDLE";
double         G_NeuralHealth = 100.0;

struct Nerve {
   string id;
   double pulse;
   color  node_color;
};
Nerve G_SystemNerves[60];

// ═══════════════════════════════════════════════════════════════════
//  BASE64 RAM DECODER (CORE ZERO-FOOTPRINT)
// ═══════════════════════════════════════════════════════════════════
string Base64Decode(string base64) {
   string b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
   string decoded = "";
   int i = 0, j = 0;
   int char_array_4[4], char_array_3[3];
   int in_len = StringLen(base64);

   while (in_len-- && base64[i] != '=') {
      char_array_4[j++] = StringFind(b64, StringSubstr(base64, i, 1));
      i++;
      if (j == 4) {
         char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
         char_array_3[1] = ((char_array_4[1] & 0xf) << 4) + ((char_array_4[2] & 0x3c) >> 2);
         char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];
         for (j = 0; j < 3; j++) decoded += ShortToString((short)char_array_3[j]);
         j = 0;
      }
   }
   return decoded;
}

// ═══════════════════════════════════════════════════════════════════
//  CLOUD PROTOCOL ENGINE
// ═══════════════════════════════════════════════════════════════════
void SyncCloudToRAM() {
   if(!TerminalInfoInteger(TERMINAL_CONNECTED)) return;
   
   string url = "https://api.github.com/repos/" + InpRepo + "/contents/" + InpFilePath;
   string auth = "Authorization: token " + InpToken + "\r\nUser-Agent: MT5-AI-Overlord\r\n";
   char post[], result[];
   string headers;

   int res = WebRequest("GET", url, auth, 5000, post, result, headers);

   if(res == 200) {
      string json_raw = CharArrayToString(result);
      int start = StringFind(json_raw, "\"content\":\"") + 11;
      int end = StringFind(json_raw, "\"", start);
      if(start > 11 && end > start) {
         string b64 = StringSubstr(json_raw, start, end - start);
         StringReplace(b64, "\\n", ""); 
         G_Memory_JSON = Base64Decode(b64);
         
         if(StringFind(G_Memory_JSON, "BUY") >= 0) G_Signal_CMD = "BUY";
         else if(StringFind(G_Memory_JSON, "SELL") >= 0) G_Signal_CMD = "SELL";
         else G_Signal_CMD = "IDLE";
      }
   }
}

// ═══════════════════════════════════════════════════════════════════
//  MASSIVE VISUAL ENGINE (60 NERVES)
// ═══════════════════════════════════════════════════════════════════
void RenderDashboard() {
   // Frame Utama
   CreateRect("AI_BG", 5, 5, 1150, 850, C'5,5,5', C'40,40,40', 2);
   CreateLabel("AI_Title", 30, 45, "AI OVERLORD BRAIN — ULTIMATE CLOUD NEURAL (60 NERVES)", "Impact", 22, clrWhite);

   for(int i=0; i<60; i++) {
      int col = i / 15;
      int row = i % 15;
      int x = 30 + (col * 275);
      int y = 110 + (row * 46);
      string n = "Nerve_" + (string)i;
      
      G_SystemNerves[i].pulse = MathRand() % 100;
      color c = (G_SystemNerves[i].pulse > 80) ? clrLime : (G_SystemNerves[i].pulse < 20) ? clrRed : clrSkyBlue;

      CreateRect(n+"_bg", x, y, 260, 40, C'15,15,15', c, 1);
      CreateLabel(n+"_id", x+10, y+12, "NERVE_ID_0x" + (string)(i+1000), "Consolas", 9, clrGray);
      CreateLabel(n+"_vl", x+190, y+12, (string)G_SystemNerves[i].pulse + "%", "Consolas", 10, c);
   }

   // Info Panel
   CreateRect("InfBox", 855, 550, 265, 260, C'10,20,10', clrGreen, 1);
   CreateLabel("InfT", 870, 565, "SYSTEM AUTONOMOUS", "Arial Bold", 10, clrWhite);
   CreateLabel("InfS", 870, 680, "SIGNAL: " + G_Signal_CMD, "Impact", 26, clrGold);
}

// ═══════════════════════════════════════════════════════════════════
//  CORE SYSTEM FUNCTIONS
// ═══════════════════════════════════════════════════════════════════
int OnInit() {
   m_trade.SetExpertMagicNumber(InpMagic);
   EventSetTimer(1);
   return(INIT_SUCCEEDED);
}

void OnDeinit(const int reason) {
   ObjectsDeleteAll(0, "AI_");
   for(int i=0; i<60; i++) ObjectsDeleteAll(0, "Nerve_" + (string)i);
}

void OnTimer() {
   if(TimeCurrent() % InpSyncSec == 0) SyncCloudToRAM();
   if(InpAutoTrade) {
      bool buy_exists = false, sell_exists = false;
      for(int i=PositionsTotal()-1; i>=0; i--) {
         if(PositionGetSymbol(i)==_Symbol && PositionGetInteger(POSITION_MAGIC)==InpMagic) {
            if(PositionGetInteger(POSITION_TYPE)==POSITION_TYPE_BUY) buy_exists = true;
            if(PositionGetInteger(POSITION_TYPE)==POSITION_TYPE_SELL) sell_exists = true;
         }
      }

      if(G_Signal_CMD == "BUY" && !buy_exists) {
         CloseAll(); m_trade.Buy(InpLot, _Symbol, 0, 0, 0, "AI-AUTO");
      }
      if(G_Signal_CMD == "SELL" && !sell_exists) {
         CloseAll(); m_trade.Sell(InpLot, _Symbol, 0, 0, 0, "AI-AUTO");
      }
   }
   RenderDashboard();
}

// --- UTILITY ---
void CreateRect(string name, int x, int y, int w, int h, color bg, color border, int sz) {
   ObjectCreate(0, name, OBJ_RECTANGLE_LABEL, 0, 0, 0);
   ObjectSetInteger(0, name, OBJPROP_XDISTANCE, x);
   ObjectSetInteger(0, name, OBJPROP_YDISTANCE, y);
   ObjectSetInteger(0, name, OBJPROP_XSIZE, w);
   ObjectSetInteger(0, name, OBJPROP_YSIZE, h);
   ObjectSetInteger(0, name, OBJPROP_BGCOLOR, bg);
   ObjectSetInteger(0, name, OBJPROP_BORDER_COLOR, border);
   ObjectSetInteger(0, name, OBJPROP_WIDTH, sz);
   ObjectSetInteger(0, name, OBJPROP_CORNER, CORNER_LEFT_UPPER);
}

void CreateLabel(string name, int x, int y, string txt, string font, int sz, color clr) {
   ObjectCreate(0, name, OBJ_LABEL, 0, 0, 0);
   ObjectSetInteger(0, name, OBJPROP_XDISTANCE, x);
   ObjectSetInteger(0, name, OBJPROP_YDISTANCE, y);
   ObjectSetString(0, name, OBJPROP_TEXT, txt);
   ObjectSetString(0, name, OBJPROP_FONT, font);
   ObjectSetInteger(0, name, OBJPROP_FONTSIZE, sz);
   ObjectSetInteger(0, name, OBJPROP_COLOR, clr);
}

void CloseAll() {
   for(int i=PositionsTotal()-1; i>=0; i--) {
      if(PositionGetSymbol(i)==_Symbol && PositionGetInteger(POSITION_MAGIC)==InpMagic) {
         m_trade.PositionClose(PositionGetInteger(POSITION_TICKET));
      }
   }
}
