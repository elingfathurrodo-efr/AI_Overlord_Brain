//+------------------------------------------------------------------+
//|              AI_OVERLORD_BRAIN_V20_MASTER_TEMPLATE               |
//|   Version 20.0 — Massive Neural Dashboard | 60 Nerves Active     |
//|   Powered by Cloud Sync RAM-Only (Zero-Footprint)                |
//+------------------------------------------------------------------+
#property copyright   "AI-Overlord-Dev"
#property link        "https://github.com"
#property version     "20.00"
#property description "AI OVERLORD BRAIN — Full Autonomous Cloud Engine"
#property strict

#include <Trade\Trade.mqh>
#include <Trade\PositionInfo.mqh>

// ═══════════════════════════════════════════════════════════════════
//  INPUT PARAMETERS (Dapat diubah di MT5)
// ═══════════════════════════════════════════════════════════════════
input group "═══ GITHUB CLOUD CONFIG ═══"
input string  InpToken        = "TEST_TOKEN"; 
input string  InpRepo         = "REPO_AKAN_DIISI_OTOMATIS";
input string  InpFilePath     = "logic.json";
input int     InpSyncSec      = 3;        // Sinkronisasi RAM (Detik)

input group "═══ NEURAL ARCHITECTURE ═══"
input bool    InpAutoTrade    = true;     // Aktifkan Autopilot
input double  InpNeuralSens   = 0.95;     // Sensitivitas Saraf

input group "═══ RISK MANAGEMENT ═══"
input double  InpLot          = 0.01;
input int     InpMagic        = 882199;
input int     InpSL           = 400;      // Point
input int     InpTP           = 800;      // Point

// ═══════════════════════════════════════════════════════════════════
//  GLOBAL DATA & STRUCTURES
// ═══════════════════════════════════════════════════════════════════
CTrade         m_trade;
string         G_Memory_JSON  = "";  
string         G_Signal_CMD   = "IDLE";
bool           G_CloudError   = false;

struct Nerve {
   double pulse;
   color  node_color;
};
Nerve G_SystemNerves[60];

// ═══════════════════════════════════════════════════════════════════
//  BASE64 RAM DECODER
// ═══════════════════════════════════════════════════════════════════
string Base64Decode(string base64) {
   string b64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
   string decoded = "";
   int char_array_4[4], char_array_3[3];
   int i = 0, j = 0, in_len = StringLen(base64);

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
   if(InpToken == "TEST_TOKEN" || InpToken == "") {
      G_CloudError = true;
      return;
   }

   string url = "https://api.github.com/repos/" + InpRepo + "/contents/" + InpFilePath;
   string auth = "Authorization: token " + InpToken + "\r\nUser-Agent: MT5-AI-Overlord\r\n";
   char post[], result[];
   string headers;

   int res = WebRequest("GET", url, auth, 5000, post, result, headers);

   if(res == 200) {
      G_CloudError = false;
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
   } else {
      G_CloudError = true;
   }
}

// ═══════════════════════════════════════════════════════════════════
//  VISUAL DASHBOARD ENGINE
// ═══════════════════════════════════════════════════════════════════
void RenderDashboard() {
   CreateRect("AI_BG", 5, 5, 1150, 850, C'5,5,5', C'40,40,40', 1);
   CreateLabel("AI_Title", 30, 45, "AI OVERLORD BRAIN — ULTIMATE CLOUD NEURAL (60 NERVES)", "Impact", 20, clrWhite);

   for(int i=0; i<60; i++) {
      int col = i / 15;
      int row = i % 15;
      int x = 30 + (col * 275);
      int y = 100 + (row * 48);
      string n = "Nerve_" + (string)i;
      
      G_SystemNerves[i].pulse = MathRand() % 100;
      color c = (G_SystemNerves[i].pulse > 85) ? clrLime : (G_SystemNerves[i].pulse < 15) ? clrRed : clrDeepSkyBlue;

      CreateRect(n+"_bg", x, y, 260, 42, C'15,15,15', c, 1);
      CreateLabel(n+"_id", x+10, y+14, "NERVE_UNIT_0x" + (string)(i+1024), "Consolas", 8, clrGray);
      CreateLabel(n+"_vl", x+200, y+14, (string)G_SystemNerves[i].pulse + "%", "Consolas", 10, c);
   }

   // Status Panel
   color statusColor = G_CloudError ? clrRed : clrLime;
   string statusMsg = G_CloudError ? "CLOUD DISCONNECTED / TOKEN MISSING" : "CLOUD SYNC: ACTIVE";
   
   CreateRect("InfBox", 855, 550, 265, 260, C'10,15,10', statusColor, 1);
   CreateLabel("StatL", 870, 570, statusMsg, "Arial Bold", 9, statusColor);
   CreateLabel("InfS", 870, 680, "SIGNAL: " + G_Signal_CMD, "Impact", 30, (G_Signal_CMD=="IDLE" ? clrWhite : clrGold));
}

// ═══════════════════════════════════════════════════════════════════
//  CORE SYSTEM FUNCTIONS
// ═══════════════════════════════════════════════════════════════════
int OnInit() {
   if(!TerminalInfoInteger(TERMINAL_DLL_ALLOWED)) {
      Alert("Error: Izinkan DLL di Settings MT5!");
      return(INIT_FAILED);
   }
   m_trade.SetExpertMagicNumber(InpMagic);
   EventSetTimer(1);
   return(INIT_SUCCEEDED);
}

void OnDeinit(const int reason) {
   EventKillTimer();
   ObjectsDeleteAll(0, "AI_");
   for(int i=0; i<60; i++) ObjectsDeleteAll(0, "Nerve_" + (string)i);
}

void OnTimer() {
   if(TimeCurrent() % InpSyncSec == 0) SyncCloudToRAM();
   
   if(InpAutoTrade && !G_CloudError) {
      bool buy_exists = false, sell_exists = false;
      for(int i=PositionsTotal()-1; i>=0; i--) {
         if(PositionGetSymbol(i)==_Symbol && PositionGetInteger(POSITION_MAGIC)==InpMagic) {
            if(PositionGetInteger(POSITION_TYPE)==POSITION_TYPE_BUY) buy_exists = true;
            if(PositionGetInteger(POSITION_TYPE)==POSITION_TYPE_SELL) sell_exists = true;
         }
      }

      if(G_Signal_CMD == "BUY" && !buy_exists) {
         CloseAll(); m_trade.Buy(InpLot, _Symbol, 0, 0, 0, "AI-OVERLORD");
      }
      if(G_Signal_CMD == "SELL" && !sell_exists) {
         CloseAll(); m_trade.Sell(InpLot, _Symbol, 0, 0, 0, "AI-OVERLORD");
      }
   }
   RenderDashboard();
   ChartRedraw();
}

void CreateRect(string name, int x, int y, int w, int h, color bg, color border, int sz) {
   ObjectCreate(0, name, OBJ_RECTANGLE_LABEL, 0, 0, 0);
   ObjectSetInteger(0, name, OBJPROP_XDISTANCE, x);
   ObjectSetInteger(0, name, OBJPROP_YDISTANCE, y);
   ObjectSetInteger(0, name, OBJPROP_XSIZE, w);
   ObjectSetInteger(0, name, OBJPROP_YSIZE, h);
   ObjectSetInteger(0, name, OBJPROP_BGCOLOR, bg);
   ObjectSetInteger(0, name, OBJPROP_BORDER_COLOR, border);
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
      if(PositionGetSymbol(i)==_Symbol && PositionGetInteger(POSITION_MAGIC)==InpMagic)
         m_trade.PositionClose(PositionGetInteger(POSITION_TICKET));
   }
}
