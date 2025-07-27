rule auto_rule_20250727013506_8295 {
  strings:
    $o0 = "dword_781C0" wide ascii nocase
    $o1 = "dword_781BC" wide ascii nocase
    $o2 = "dword_7818C" wide ascii nocase
    $o3 = "dword_7811C" wide ascii nocase
    $o4 = "dword_780EC" wide ascii nocase
  condition:
    4 of ($o*)
}