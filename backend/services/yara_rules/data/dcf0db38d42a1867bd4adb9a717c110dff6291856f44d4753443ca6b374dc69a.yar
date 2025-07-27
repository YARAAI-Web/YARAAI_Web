rule auto_rule_20250726185120_6068 {
  strings:
    $o0 = "_itoa" wide ascii nocase
    $o1 = "_flushall" wide ascii nocase
    $o2 = "dword_4672F4" wide ascii nocase
    $o3 = "dword_46730C" wide ascii nocase
    $o4 = "InterlockedIncrement" wide ascii nocase
  condition:
    4 of ($o*)
}