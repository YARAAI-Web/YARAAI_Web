rule auto_rule_20250726170702_7091 {
  strings:
    $o0 = "CodePagea" wide ascii nocase
    $o1 = "AddAtomA" wide ascii nocase
    $o2 = "ProcessWindowStation" wide ascii nocase
    $o3 = "SuspendThread" wide ascii nocase
  condition:
    4 of ($o*)
}