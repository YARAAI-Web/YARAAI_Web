rule auto_rule_20250726194446_8243 {
  strings:
    $o0 = "dword_42C891" wide ascii nocase
    $o1 = "x5F07u" wide ascii nocase
    $o2 = "x4EE8" wide ascii nocase
    $o3 = "x3658000098AELL" wide ascii nocase
    $o4 = "x8FDC9A8FB91FABF2uLL" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726194449_4821 {
  strings:
    $o0 = "x7E21u" wide ascii nocase
    $o1 = "x3985" wide ascii nocase
  condition:
    all of them
}

rule combined_rule_20250726194453_0651 {
  condition:
    auto_rule_20250726194446_8243 or auto_rule_20250726194449_4821
}