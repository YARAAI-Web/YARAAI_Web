rule auto_rule_20250726190022_1466 {
  strings:
    $o0 = "dword_467D20" wide ascii nocase
    $o1 = "_CrtDumpMemoryLeaks" wide ascii nocase
    $o2 = "UnwindUp1_0" wide ascii nocase
    $o3 = "_aulldiv" wide ascii nocase
  condition:
    4 of ($o*)
}