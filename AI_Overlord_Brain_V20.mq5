// ============================================================
// AI_OVERLORD_BRAIN_V25_MASTER_TEMPLATE
//   Version 25.0 - Massive Neural Dashboard | 39 Bureaus Active
//   Powered by Cursor Sync MCP Only (Zero Oversight)
// ============================================================
#property copyright  "AI Overlord Dev"
#property link       "https://github.com"
#property version    "50.00"
#property description "AI OVERLORD BRAIN - Full Autonomous Chart Engine"
#property strict

#include <Trade/Trade.mqh>
#include <Trade/AccountInfo.mqh>

// ============================================================
// ⚙️ INPUT PARAMETERS (Auto-injected by GitHub Actions)
// ============================================================

input group "=== GUILD CLOUD API ==="
// ✅ TOKEN & REPO akan otomatis diganti oleh GitHub Actions
input string InpApiToken   = "FORGE_ARM_ALLIES_DYNAMICS_TOKEN";   // GitHub PAT Token
input string InpApiRepo    = "FORGE_ARM_ALLIES_DYNAMICS_REPO";    // Full API URL
input string InpRepoName   = "FORGE_ARM_ALLIES_DYNAMICS2";        // owner/repo
input string InpFilePath   = "logic.json";                         // Signal file path
input int    InpSyncFor    = 5;                                    // Sync interval (sec)

input group "=== NEURAL ARCHITECTURE ==="
input bool   InpAutoTrade  = true;   // All Item Activation
input double InpRiskPerc   = 0.025;  // Sensitivity per Level (% lot)

input group "=== RISK MANAGEMENT ==="
input double InpLot        = 0.01;   // Base Lot Size
input int    InpMagic      = 38439;  // Magic Number (Prime)
input int    InpTP         = 400;    // Take Profit (points)
input int    InpSL         = 200;    // Stop Loss (points)
input int    InpSlippage   = 10;     // Max Slippage

input group "=== SIGNAL FILTER ==="
input bool   InpUseBuySell = true;   // Enable BUY/SELL signal
input bool   InpUseClose   = true;   // Enable CLOSE signal
input string InpAllowedSymbols = ""; // Comma-separated (empty=all)

// ============================================================
// 📦 GLOBAL DATA & STRUCTURES
// ============================================================

struct t_trade {
   ulong  id;
   string s_Currency[999];
   string s_Signal_ORD;    // "BUY" / "SELL" / "CLOSE"
   bool   f_active;
   double price;
   double lot;
   color  node_color;
};

t_trade SystemGenius[999];
int     g_signal_count = 0;

// HTTP & Signal state
string  g_last_signal_action  = "";
string  g_last_signal_symbol  = "";
double  g_last_signal_lot     = 0.0;
string  g_last_signal_ts      = "";
datetime g_last_fetch_time    = 0;

CTrade  g_trade;

// ============================================================
// 🔐 BASE64 DECODE (untuk Auth Header GitHub API)
// ============================================================
string Base64Decode(string base64) {
   string bcd = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=";
   string decoded = "";
   int    i = 0;
   int    len = StringLen(base64);

   while (i < len) {
      int char_array_4[4];
      int char_array_3[3];
      int j = 0;

      while (j < 4 && i < len) {
         char_array_4[j] = (int)StringFind(bcd, CharToStr((uchar)base64[i]));
         i++;
         j++;
      }
      for (int k = j; k < 4; k++) char_array_4[k] = 0;

      char_array_3[0] = (char_array_4[0] << 2) + ((char_array_4[1] & 0x30) >> 4);
      char_array_3[1] = ((char_array_4[1] & 0xF) << 4) + ((char_array_4[2] & 0x3C) >> 2);
      char_array_3[2] = ((char_array_4[2] & 0x3) << 6) + char_array_4[3];

      for (int k = 0; k < j - 1; k++) decoded += CharToStr((uchar)char_array_3[k]);
   }
   return decoded;
}

// ============================================================
// 🌐 CLOUD PROTOCOL ENGINE - Fetch Signal dari GitHub
// ============================================================

bool FetchSignalFromGitHub() {
   string url     = InpApiRepo + "/contents/" + InpFilePath;
   string headers = "Authorization: token " + InpApiToken + "\r\n"
                  + "Accept: application/vnd.github+json\r\n"
                  + "User-Agent: AI-Overlord-EA/25.0\r\n";
   string result  = "";
   char   req[], res[];
   int    timeout = 5000;

   ResetLastError();
   int code = WebRequest("GET", url, headers, timeout, req, res, result);

   if (code == 200) {
      string raw_body = CharArrayToString(res);

      // Parse "content" field dari JSON response GitHub
      int pos_content = StringFind(raw_body, "\"content\"");
      if (pos_content < 0) return false;

      int pos_start = StringFind(raw_body, "\"", pos_content + 10) + 1;
      int pos_end   = StringFind(raw_body, "\"", pos_start);
      string b64    = StringSubstr(raw_body, pos_start, pos_end - pos_start);

      // Hapus \n dari base64
      StringReplace(b64, "\\n", "");
      StringReplace(b64, "\n", "");

      string json = Base64Decode(b64);
      ParseSignalJSON(json);
      return true;
   }

   Print("❌ GitHub fetch error: HTTP ", code, " | ", result);
   return false;
}

// ============================================================
// 📋 PARSE SIGNAL JSON
// ============================================================

void ParseSignalJSON(string json) {
   // Parse "action"
   int pos = StringFind(json, "\"action\"");
   if (pos >= 0) {
      int s = StringFind(json, "\"", pos + 9) + 1;
      int e = StringFind(json, "\"", s);
      g_last_signal_action = StringSubstr(json, s, e - s);
   }

   // Parse "symbol"
   pos = StringFind(json, "\"symbol\"");
   if (pos >= 0) {
      int s = StringFind(json, "\"", pos + 9) + 1;
      int e = StringFind(json, "\"", s);
      g_last_signal_symbol = StringSubstr(json, s, e - s);
   }

   // Parse "lot"
   pos = StringFind(json, "\"lot\"");
   if (pos >= 0) {
      int s = StringFind(json, ":", pos + 5) + 1;
      int e = StringFind(json, ",", s);
      if (e < 0) e = StringFind(json, "}", s);
      string lot_str = StringSubstr(json, s, e - s);
      StringTrimLeft(lot_str);
      StringTrimRight(lot_str);
      g_last_signal_lot = StringToDouble(lot_str);
   }

   // Parse "timestamp"
   pos = StringFind(json, "\"timestamp\"");
   if (pos >= 0) {
      int s = StringFind(json, "\"", pos + 12) + 1;
      int e = StringFind(json, "\"", s);
      g_last_signal_ts = StringSubstr(json, s, e - s);
   }

   Print("📡 Signal Received → Action:", g_last_signal_action,
         " | Symbol:", g_last_signal_symbol,
         " | Lot:", g_last_signal_lot,
         " | TS:", g_last_signal_ts);
}

// ============================================================
// 📤 SEND SIGNAL ke GitHub (Push logic.json)
// ============================================================

bool SendSignalToGitHub(string action, string symbol, double lot, string comment) {
   // Buat JSON content
   string timestamp = TimeToString(TimeGMT(), TIME_DATE | TIME_SECONDS);
   StringReplace(timestamp, " ", "T");

   string json_content = "{\n"
      + "  \"timestamp\": \"" + timestamp + "Z\",\n"
      + "  \"repo\": \"" + InpRepoName + "\",\n"
      + "  \"signal\": {\n"
      + "    \"action\": \"" + action + "\",\n"
      + "    \"symbol\": \"" + symbol + "\",\n"
      + "    \"lot\": " + DoubleToString(lot, 2) + ",\n"
      + "    \"comment\": \"" + comment + "\",\n"
      + "    \"issued_by\": \"EA_v25\"\n"
      + "  },\n"
      + "  \"status\": \"active\"\n"
      + "}";

   // Get current file SHA (required for update)
   string sha = GetFileSHA();

   // Encode content ke base64
   uchar  content_arr[];
   string content_b64 = "";
   StringToCharArray(json_content, content_arr, 0, StringLen(json_content));
   content_b64 = EncodeBase64(content_arr);

   // Build PUT request body
   string put_body = "{\"message\":\"🤖 EA Signal: " + action + " " + symbol + "\","
                   + "\"content\":\"" + content_b64 + "\"";
   if (sha != "") put_body += ",\"sha\":\"" + sha + "\"";
   put_body += "}";

   string url     = InpApiRepo + "/contents/" + InpFilePath;
   string headers = "Authorization: token " + InpApiToken + "\r\n"
                  + "Accept: application/vnd.github+json\r\n"
                  + "Content-Type: application/json\r\n"
                  + "User-Agent: AI-Overlord-EA/25.0\r\n";
   string result  = "";
   char   req[], res[];
   StringToCharArray(put_body, req, 0, StringLen(put_body));

   int code = WebRequest("PUT", url, headers, 5000, req, res, result);

   if (code == 200 || code == 201) {
      Print("✅ Signal sent to GitHub → ", action, " ", symbol);
      return true;
   }

   Print("❌ GitHub push error: HTTP ", code);
   return false;
}

// ============================================================
// 🔑 Helper: Get File SHA (untuk update)
// ============================================================

string GetFileSHA() {
   string url     = InpApiRepo + "/contents/" + InpFilePath;
   string headers = "Authorization: token " + InpApiToken + "\r\n"
                  + "Accept: application/vnd.github+json\r\n"
                  + "User-Agent: AI-Overlord-EA/25.0\r\n";
   string result  = "";
   char   req[], res[];

   int code = WebRequest("GET", url, headers, 5000, req, res, result);
   if (code != 200) return "";

   string body = CharArrayToString(res);
   int pos = StringFind(body, "\"sha\"");
   if (pos < 0) return "";

   int s = StringFind(body, "\"", pos + 6) + 1;
   int e = StringFind(body, "\"", s);
   return StringSubstr(body, s, e - s);
}

// ============================================================
// 🔐 Base64 Encode (helper untuk upload)
// ============================================================

string EncodeBase64(const uchar &data[]) {
   static const string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
   string result = "";
   int    len    = ArraySize(data);

   for (int i = 0; i < len; i += 3) {
      int b0 = data[i];
      int b1 = (i + 1 < len) ? data[i + 1] : 0;
      int b2 = (i + 2 < len) ? data[i + 2] : 0;

      result += StringSubstr(chars, (b0 >> 2) & 0x3F, 1);
      result += StringSubstr(chars, ((b0 & 0x3) << 4) | ((b1 >> 4) & 0xF), 1);
      result += (i + 1 < len) ? StringSubstr(chars, ((b1 & 0xF) << 2) | ((b2 >> 6) & 0x3), 1) : "=";
      result += (i + 2 < len) ? StringSubstr(chars, b2 & 0x3F, 1) : "=";
   }
   return result;
}

// ============================================================
// 🎯 EXECUTE TRADE berdasarkan Signal
// ============================================================

void ExecuteSignal() {
   if (!InpAutoTrade) return;
   if (g_last_signal_action == "") return;

   string symbol = (g_last_signal_symbol != "") ? g_last_signal_symbol : Symbol();
   double lot    = (g_last_signal_lot > 0) ? g_last_signal_lot : InpLot;

   // Cek apakah symbol diizinkan
   if (InpAllowedSymbols != "") {
      if (StringFind(InpAllowedSymbols, symbol) < 0) {
         Print("⚠️ Symbol ", symbol, " not in allowed list. Skipped.");
         return;
      }
   }

   g_trade.SetExpertMagicNumber(InpMagic);
   g_trade.SetDeviationInPoints(InpSlippage);

   double tp_price = 0, sl_price = 0;
   double ask = SymbolInfoDouble(symbol, SYMBOL_ASK);
   double bid = SymbolInfoDouble(symbol, SYMBOL_BID);
   double point = SymbolInfoDouble(symbol, SYMBOL_POINT);

   if (g_last_signal_action == "BUY" && InpUseBuySell) {
      tp_price = ask + InpTP * point;
      sl_price = ask - InpSL * point;
      if (g_trade.Buy(lot, symbol, ask, sl_price, tp_price, "AI Overlord BUY")) {
         Print("✅ BUY executed: ", symbol, " Lot:", lot);
         g_last_signal_action = ""; // Reset setelah eksekusi
      }
   }
   else if (g_last_signal_action == "SELL" && InpUseBuySell) {
      tp_price = bid - InpTP * point;
      sl_price = bid + InpSL * point;
      if (g_trade.Sell(lot, symbol, bid, sl_price, tp_price, "AI Overlord SELL")) {
         Print("✅ SELL executed: ", symbol, " Lot:", lot);
         g_last_signal_action = ""; // Reset
      }
   }
   else if (g_last_signal_action == "CLOSE" && InpUseClose) {
      CloseAllPositions(symbol);
      g_last_signal_action = ""; // Reset
   }
   else if (g_last_signal_action == "UPDATE") {
      Print("ℹ️ UPDATE signal received. No trade action.");
      g_last_signal_action = ""; // Reset
   }
}

void CloseAllPositions(string symbol) {
   for (int i = PositionsTotal() - 1; i >= 0; i--) {
      ulong ticket = PositionGetTicket(i);
      if (ticket == 0) continue;
      if (PositionGetString(POSITION_SYMBOL) == symbol &&
          PositionGetInteger(POSITION_MAGIC) == InpMagic) {
         g_trade.PositionClose(ticket);
         Print("🔴 Closed position #", ticket);
      }
   }
}

// ============================================================
// 🖥️ DASHBOARD (Visual di Chart)
// ============================================================

void DrawDashboard() {
   string prefix = "AI_OB_";

   // Background panel
   if (ObjectFind(0, prefix + "bg") < 0) {
      ObjectCreate(0, prefix + "bg", OBJ_RECTANGLE_LABEL, 0, 0, 0);
      ObjectSetInteger(0, prefix + "bg", OBJPROP_XDISTANCE, 10);
      ObjectSetInteger(0, prefix + "bg", OBJPROP_YDISTANCE, 10);
      ObjectSetInteger(0, prefix + "bg", OBJPROP_XSIZE, 320);
      ObjectSetInteger(0, prefix + "bg", OBJPROP_YSIZE, 220);
      ObjectSetInteger(0, prefix + "bg", OBJPROP_BGCOLOR, C'20,20,30');
      ObjectSetInteger(0, prefix + "bg", OBJPROP_BORDER_TYPE, BORDER_FLAT);
      ObjectSetInteger(0, prefix + "bg", OBJPROP_COLOR, clrGold);
   }

   // Title
   string title = "🤖 AI OVERLORD BRAIN V25";
   SetLabel(prefix + "title", title, 20, 25, 12, clrGold);

   // Repo info
   string repo_short = StringSubstr(InpRepoName, 0, MathMin(40, StringLen(InpRepoName)));
   SetLabel(prefix + "repo",  "📁 " + repo_short, 20, 50, 9, clrSilver);

   // Token status
   string token_status = (StringLen(InpApiToken) > 10) ? "✅ Token: Connected" : "❌ Token: Not Set";
   SetLabel(prefix + "token", token_status, 20, 70, 9,
            (StringLen(InpApiToken) > 10) ? clrLimeGreen : clrRed);

   // Last signal
   string sig_text = "📡 Last Signal: " + g_last_signal_action + " " + g_last_signal_symbol;
   SetLabel(prefix + "signal", sig_text, 20, 95, 9, clrDodgerBlue);

   // Timestamp
   SetLabel(prefix + "ts", "🕐 " + g_last_signal_ts, 20, 115, 9, clrGray);

   // Auto trade status
   string at_text = InpAutoTrade ? "🟢 AutoTrade: ON" : "🔴 AutoTrade: OFF";
   SetLabel(prefix + "at", at_text, 20, 140, 9, InpAutoTrade ? clrLimeGreen : clrRed);

   // Sync interval
   SetLabel(prefix + "sync", "⏱ Sync: " + IntegerToString(InpSyncFor) + "s", 20, 160, 9, clrWhite);

   // Account info
   double balance  = AccountInfoDouble(ACCOUNT_BALANCE);
   double equity   = AccountInfoDouble(ACCOUNT_EQUITY);
   SetLabel(prefix + "acc",
            "💰 Bal:" + DoubleToString(balance, 2) + "  Eq:" + DoubleToString(equity, 2),
            20, 185, 9, clrYellow);

   ChartRedraw(0);
}

void SetLabel(string name, string text, int x, int y, int size, color clr) {
   if (ObjectFind(0, name) < 0)
      ObjectCreate(0, name, OBJ_LABEL, 0, 0, 0);
   ObjectSetInteger(0, name, OBJPROP_XDISTANCE,  x);
   ObjectSetInteger(0, name, OBJPROP_YDISTANCE,  y);
   ObjectSetString(0,  name, OBJPROP_TEXT,        text);
   ObjectSetInteger(0, name, OBJPROP_FONTSIZE,    size);
   ObjectSetInteger(0, name, OBJPROP_COLOR,       clr);
   ObjectSetString(0,  name, OBJPROP_FONT,        "Arial Bold");
   ObjectSetInteger(0, name, OBJPROP_CORNER,      CORNER_LEFT_UPPER);
}

// ============================================================
// 📌 OnInit
// ============================================================
int OnInit() {
   Print("🚀 AI Overlord Brain V25 Initialized");
   Print("📁 Repo : ", InpRepoName);
   Print("🔑 Token: ", (StringLen(InpApiToken) > 10 ? "OK (" + IntegerToString(StringLen(InpApiToken)) + " chars)" : "❌ NOT SET"));

   if (StringLen(InpApiToken) < 10 || InpApiToken == "FORGE_ARM_ALLIES_DYNAMICS_TOKEN") {
      Print("⚠️ WARNING: Token belum diisi! Generate ulang EA via GitHub Actions.");
      Comment("⚠️ AI Overlord: Token belum diisi!\nJalankan GitHub Actions untuk auto-inject.");
   }

   g_trade.SetExpertMagicNumber(InpMagic);
   EventSetTimer(InpSyncFor);
   DrawDashboard();
   return INIT_SUCCEEDED;
}

// ============================================================
// 📌 OnDeinit
// ============================================================
void OnDeinit(const int reason) {
   EventKillTimer();
   ObjectsDeleteAll(0, "AI_OB_");
   Print("🛑 AI Overlord Brain V25 Deinitialized. Reason: ", reason);
}

// ============================================================
// 📌 OnTimer - Fetch signal periodik
// ============================================================
void OnTimer() {
   datetime now = TimeGMT();
   if (now - g_last_fetch_time < InpSyncFor) return;
   g_last_fetch_time = now;

   Print("🔄 Fetching signal from GitHub...");
   if (FetchSignalFromGitHub()) {
      ExecuteSignal();
   }
   DrawDashboard();
}

// ============================================================
// 📌 OnTick
// ============================================================
void OnTick() {
   DrawDashboard();
}

// ============================================================
// 📌 OnChartEvent - Manual trigger via chart comment
// ============================================================
void OnChartEvent(const int id, const long &lparam, const double &dparam, const string &sparam) {
   // User bisa klik chart atau kirim event manual
   if (id == CHARTEVENT_KEYDOWN) {
      if (lparam == 70) { // 'F' key = Force fetch
         Print("🔄 Force fetch signal...");
         FetchSignalFromGitHub();
         ExecuteSignal();
      }
      if (lparam == 83) { // 'S' key = Send test signal
         SendSignalToGitHub("UPDATE", Symbol(), InpLot, "Manual test from EA");
      }
   }
}
