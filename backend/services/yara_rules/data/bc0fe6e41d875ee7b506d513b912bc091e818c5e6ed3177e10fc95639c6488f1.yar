rule auto_rule_20250726074603_8548 {
  strings:
    $o0 = "GetTypeLibCache" wide ascii nocase
    $o1 = "_setusermatherr" wide ascii nocase
    $o2 = "OnCmdMsg" wide ascii nocase
    $o3 = "GetSuperWndProcAddr" wide ascii nocase
    $o4 = "dword_40CC60" wide ascii nocase
  condition:
    5 of ($o*)
}