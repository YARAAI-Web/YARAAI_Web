rule auto_rule_20250726215338_8784 {
  strings:
    $o0 = "UnwindUp0_0" wide ascii nocase
    $o1 = "waveInClose" wide ascii nocase
    $o2 = "dword_45D3E4" wide ascii nocase
  condition:
    3 of ($o*)
}