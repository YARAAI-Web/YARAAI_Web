rule auto_rule_20250726213138_4237 {
  strings:
    $o0 = "dword_45AA8C" wide ascii nocase
    $o1 = "x402C40" wide ascii nocase
    $o2 = "dword_45A904" wide ascii nocase
    $o3 = "_seh_longjmp_unwind" wide ascii nocase
  condition:
    4 of ($o*)
}