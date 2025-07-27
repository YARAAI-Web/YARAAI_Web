rule auto_rule_20250727035820_8366 {
  strings:
    $o0 = "dword_4C124C" wide ascii nocase
    $o1 = "dword_4C1630" wide ascii nocase
    $o2 = "TrayIconDebug" wide ascii nocase
  condition:
    3 of ($o*)
}