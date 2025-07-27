rule auto_rule_20250726171556_7474 {
  strings:
    $o0 = "init" wide ascii nocase
    $o1 = "MmGetSystemRoutineAddress" wide ascii nocase
    $o2 = "KeInitializeMutex" wide ascii nocase
    $o3 = "word_1EF22" wide ascii nocase
  condition:
    4 of ($o*)
}