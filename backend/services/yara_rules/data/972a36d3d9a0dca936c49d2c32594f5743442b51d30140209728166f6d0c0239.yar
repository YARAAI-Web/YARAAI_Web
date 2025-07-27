rule auto_rule_20250726081519_5654 {
  strings:
    $o0 = "flProtect" wide ascii nocase
    $o1 = "dword_4012F4" wide ascii nocase
    $o2 = "aStftware" wide ascii nocase
    $o3 = "uSize" wide ascii nocase
  condition:
    4 of ($o*)
}