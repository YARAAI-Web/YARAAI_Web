rule auto_rule_20250726123527_7550 {
  strings:
    $o0 = "UnwindUp1_0" wide ascii nocase
    $o1 = "_CrtCheckMemory" wide ascii nocase
  condition:
    all of them
}