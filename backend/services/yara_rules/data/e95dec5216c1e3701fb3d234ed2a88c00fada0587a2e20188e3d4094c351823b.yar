rule auto_rule_20250727011407_1515 {
  strings:
    $o0 = "__sbh_alloc_new_group" wide ascii nocase
    $o1 = "_fpmath" wide ascii nocase
    $o2 = "__ld12mul" wide ascii nocase
    $o3 = "cChannels" wide ascii nocase
  condition:
    4 of ($o*)
}