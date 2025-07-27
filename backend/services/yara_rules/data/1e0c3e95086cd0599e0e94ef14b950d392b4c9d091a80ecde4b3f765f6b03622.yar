rule auto_rule_20250726082351_4806 {
  strings:
    $o0 = "dword_4295CC" wide ascii nocase
    $o1 = "xE851" wide ascii nocase
    $o2 = "x912C" wide ascii nocase
    $o3 = "dword_4298C5" wide ascii nocase
    $o4 = "dword_429969" wide ascii nocase
  condition:
    4 of ($o*)
}

rule auto_rule_20250726082354_5873 {
  strings:
    $o0 = "dword_42994D" wide ascii nocase
    $o1 = "dword_4298CD" wide ascii nocase
    $o2 = "xED244576" wide ascii nocase
    $o3 = "x16A2" wide ascii nocase
    $o4 = "dword_429608" wide ascii nocase
  condition:
    4 of ($o*)
}

rule combined_rule_20250726082358_9044 {
  condition:
    auto_rule_20250726082351_4806 or auto_rule_20250726082354_5873
}