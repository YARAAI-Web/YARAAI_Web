rule auto_rule_20250726175848_2913 {
  strings:
    $o0 = "DefMDIChildProcA" wide ascii nocase
    $o1 = "dwTime" wide ascii nocase
    $o2 = "hMonitor" wide ascii nocase
    $o3 = "GetMonitorInfoA" wide ascii nocase
    $o4 = "AnimateWindow" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726175851_8255 {
  strings:
    $o0 = "byte_41DA2C" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726175855_6396 {
  condition:
    auto_rule_20250726175848_2913 or auto_rule_20250726175851_8255
}