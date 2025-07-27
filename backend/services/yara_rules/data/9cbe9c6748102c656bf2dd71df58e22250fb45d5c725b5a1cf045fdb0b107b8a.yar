rule auto_rule_20250726102141_8189 {
  strings:
    $o0 = "ReturnValue" wide ascii nocase
    $o1 = "dword_45CFC0" wide ascii nocase
    $o2 = "dword_45CF48" wide ascii nocase
    $o3 = "UnwindUp4_0" wide ascii nocase
    $o4 = "x402801" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726102144_9776 {
  strings:
    $o0 = "waveInClose" wide ascii nocase
    $o1 = "Handler" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726102147_7517 {
  condition:
    auto_rule_20250726102141_8189 or auto_rule_20250726102144_9776
}