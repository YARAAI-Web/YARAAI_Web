rule auto_rule_20250726183833_8841 {
  strings:
    $o0 = "GetStringTypeA" wide ascii nocase
    $o1 = "Handler" wide ascii nocase
    $o2 = "_msize" wide ascii nocase
    $o3 = "dword_471028" wide ascii nocase
  condition:
    4 of ($o*)
}