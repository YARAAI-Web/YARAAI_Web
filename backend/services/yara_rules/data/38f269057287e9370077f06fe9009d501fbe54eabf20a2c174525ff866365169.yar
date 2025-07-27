rule auto_rule_20250726203233_0886 {
  strings:
    $o0 = "CreateSemaphoreW" wide ascii nocase
    $o1 = "x600Eu" wide ascii nocase
    $o2 = "x21FD" wide ascii nocase
    $o3 = "dword_4302B9" wide ascii nocase
    $o4 = "lInitialCount" wide ascii nocase
  condition:
    4 of ($o*)
}