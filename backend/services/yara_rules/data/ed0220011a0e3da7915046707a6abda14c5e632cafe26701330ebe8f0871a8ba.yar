rule auto_rule_20250727003604_9317 {
  strings:
    $o0 = "UnwindUp6_0" wide ascii nocase
    $o1 = "dword_407018" wide ascii nocase
    $o2 = "dword_45AA28" wide ascii nocase
    $o3 = "RtlUnwind" wide ascii nocase
    $o4 = "dword_45AE10" wide ascii nocase
  condition:
    4 of ($o*)
}