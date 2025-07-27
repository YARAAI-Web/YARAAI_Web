rule auto_rule_20250726211218_2832 {
  strings:
    $o0 = "GlobalReAlloc" wide ascii nocase
    $o1 = "j_wcslen" wide ascii nocase
    $o2 = "IsWindowEnabled" wide ascii nocase
  condition:
    3 of ($o*)
}