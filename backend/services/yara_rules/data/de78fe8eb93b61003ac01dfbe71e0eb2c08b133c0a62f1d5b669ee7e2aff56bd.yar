rule auto_rule_20250727002759_2949 {
  strings:
    $o0 = "dword_4C1658" wide ascii nocase
    $o1 = "dword_4C1728" wide ascii nocase
    $o2 = "dword_4C111C" wide ascii nocase
    $o3 = "GetForegroundWindow" wide ascii nocase
  condition:
    4 of ($o*)
}