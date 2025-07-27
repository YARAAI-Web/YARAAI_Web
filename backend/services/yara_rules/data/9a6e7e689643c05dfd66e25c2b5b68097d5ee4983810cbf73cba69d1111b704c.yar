rule auto_rule_20250726233934_6390 {
  strings:
    $o0 = "__crtMessageBoxA" wide ascii nocase
    $o1 = "UnwindUp2_0" wide ascii nocase
    $o2 = "dword_461538" wide ascii nocase
    $o3 = "dword_460D48" wide ascii nocase
    $o4 = "GetStringTypeW" wide ascii nocase
  condition:
    4 of ($o*)
}