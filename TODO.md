# TODO

## Now

- Make a `Parents` factory

## Next

- Strip `View` of extra fields

- Eliminate need for special injector props treatment by making a container in the partial which contains props

  - Then, change wired.dataclasses injector to get props if present and use them

## Soon

- Move `template` from view dataclass field to part of the decorator arguments

## Eventually

## Done

- Get rid of `IUrl` singleton perhaps by making request.path unneeded
