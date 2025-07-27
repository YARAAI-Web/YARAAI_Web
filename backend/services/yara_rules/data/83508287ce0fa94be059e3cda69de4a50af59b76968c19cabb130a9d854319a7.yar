rule auto_rule_20250726201437_3166 {
  strings:
    $o0 = "runtime__ptr_spanSet_push" wide ascii nocase
    $o1 = "runtime_loadOptionalSyscalls" wide ascii nocase
    $o2 = "unreachableMethod" wide ascii nocase
    $o3 = "binarySearchTree" wide ascii nocase
  condition:
    4 of ($o*)
}